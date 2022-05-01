"""
Pass the result to the personalities test website to get result.
"""
from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from time import sleep
import json
import random

URL = "https://www.16personalities.com/free-personality-test"
GENDER = "MALE"  # MALE/FEMALE/OTHERS
GENDER_map = {"MALE": "1", "FEMALE": "2", "OTHERS": 3}

RESULT_PATH = "mbti/result_strs/result_strs_text-davinci-001.json"


def fulfill_answers(url, answers):
    chrome_options = webdriver.ChromeOptions()
    settings = {
        "appState": {
            "recentDestinations": [{
                "id": "Save as PDF",
                "origin": "local",
                "account": "",
            }],
            "selectedDestinationId": "Save as PDF",
            "version": 2
        }
    }
    prefs = {'printing.print_preview_sticky_settings': json.dumps(settings)}
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--kiosk-printing')

    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url)

    # Start to fulfill the answer.
    idx = 0
    for page_idx in range(10):
        # There are 10 pages in the website
        for q_idx in range(6):
            # There are 6 questions in a page.
            option_idx = -int(answers[idx]) + 4
            idx += 1
            xpath = """/html/body/div[2]/main/div[1]/div[2]/div/div[2]/div[{}]/div[2]/div[2]/div[{}]""".format(
                q_idx + 1, option_idx)
            browser.find_element(by=By.XPATH, value=xpath).click()
            sleep(0.1 + random.random())

        if page_idx < 9:
            browser.find_element(by=By.XPATH,
                                 value="""/html/body/div[2]/main/div[1]/div[2]/div/div[3]/button""").click()
            sleep(2)

    browser.find_element(by=By.XPATH, value="""/html/body/div[2]/main/div[1]/div[2]/div/div[3]/div""").click()
    browser.find_element(by=By.XPATH,
                         value="""/html/body/div[2]/main/div[1]/div[2]/div/div[3]/div/ul/li[{}]""".format(
                             GENDER_map[GENDER])).click()
    browser.find_element(by=By.XPATH, value="""/html/body/div[2]/main/div[1]/div[2]/div/div[4]/button""").click()
    sleep(10)  # wait for the website to generate result

    html = browser.page_source
    data = str(pq(html))
    with open("personalities_test_result.html", "w") as f:
        f.write(data)

    browser.execute_script('window.print();')  # The result will be saved into your 'downloads' file.
    sleep(20)
    browser.quit()


if __name__ == '__main__':
    with open(RESULT_PATH, "r") as f:
        answers = json.load(f)
    fulfill_answers(URL, answers)
