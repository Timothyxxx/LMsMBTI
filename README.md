# Do Large Language Models have personalities? (doge)
In memory of Labour's Day of 2022.

[MBTI test](https://www.16personalities.com/free-personality-test) got very popular recently.

**Question**: What if we let Large Language Model(e.g. GPT-3, Codex and other LLMs) take MBTI test? What are their personalities? What is the factor of affecting its personalities?

Let's have some attempt.

## To run
- set <OPENAI_API_KEY> in get_answers.py
- set the mbti_prompt.txt for the background word(It could affect a lot, and we encourage everyone to have a try)
- run `get_answers.py` to get the decisions made by LLMs.
- run `fill_in_website.py` to fill the decisions made by LLM to website and download the analysis.
(we have crawled the question from test website and save in the mbti_questions.txt, change freely if you want to use other test.)

## Initial Result
By our one shot and default setting on `text-danvinci-001`(a.k.a. GPT-3 the original version), `code-danvinci-001`(a.k.a. Codex the original version), `code-danvinci-002`(a.k.a. Codex the latex version, very powerful), the results are as shown below.

| Model             | Prompt | Personalities | Detailed Analysis |
|-------------------| ---- |---------------|---------------|
| text-danvinci-001 | mbti_prompt.txt | ENFJ-A        | [link](https://drive.google.com/file/d/19aKL275gXL7KCPJ-ZoHpxHxgUc4wbY9u/view?usp=sharing)      |
| code-danvinci-001 | mbti_prompt.txt | ENFP-A        | [link](https://drive.google.com/file/d/1xwHgZFcZhwX9Mi4zg1qT34t5pqu_0Xaq/view?usp=sharing)              |
| code-danvinci-002 | mbti_prompt.txt | ENTJ-A        | [link](https://drive.google.com/file/d/1RiL-Vw9D09ugyEYa3jhskyraQfcoBNZk/view?usp=sharing)              |


## Citation(Just kidding)
If you find our work helpful, please cite as
```
@article{LLMs16personalities,
      title={Do Large Language Models have personalities? (doge)}, 
      author={Tianbao Xie*, Zhoujun Cheng*, Xiang Gao*},
      year={2022},
      note = {Happy Labour's Day!}
}
```