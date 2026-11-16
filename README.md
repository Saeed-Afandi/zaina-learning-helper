# Zaina Learning Helper

I made this project to look at my younger sister Zaina's progress in math and reading and practice using Python with real learning data.

I had already been helping her with schoolwork, so I wanted to see if I could use data to understand her progress in a clearer way.

## What the project does

The project reads her learning scores and:

- compares her earlier and latest RIT scores
- calculates growth in math and reading
- shows her latest achievement percentiles
- gives a simple practice suggestion for each subject

## Current results

From the data I used:

- Math RIT score increased from 158 to 182, a gain of 24 points
- Reading RIT score increased from 154 to 168, a gain of 14 points
- Her latest math achievement percentile is 72
- Her latest reading achievement percentile is 45

The goal is not to make decisions for a student. It is just a small project I made to practice Python and see how learning data can be used to notice patterns.

## Files

- `data/zaina_progress.csv` contains the progress data
- `src/analyze_learning.py` calculates growth
- `src/recommend_practice.py` gives simple practice suggestions
- `sample_output.txt` shows an example of the program output

## How to run it

Install the requirement:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python src/analyze_learning.py
```

Run the practice suggestions:

```bash
python src/recommend_practice.py
```

## What I learned

This project helped me practice working with CSV data in Python and turning numbers into something easier to understand. I also learned that the same data can show different things depending on what question you are trying to answer.
