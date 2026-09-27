# Best Research Tool Experiment

## Summary

In this research project, I identify and recommend the best sources of information for different classifications of common questions. I used sources of information like:

- OpenAI's ChatGPT 5.4 Mini
- Google Gemini 3.5 Flash
- Google Search
- Microsoft Bing
- Wikipedia
- World Book Encyclopedia

The sources were chosen in different categories: AI, search engine, and encyclopedia. I wanted two of each so there were two options to compare. Having one online encyclopedia and one physical encyclopedia made it more varied and spread out.

I chose to do this project because with the new discovery of Generative AI, people have been questioning whether it is actually reliable or not, and I wanted to see if AI could potentially replace sources such as encyclopedias and maybe even search engines in the near future.

This research could benefit people who are not fully comfortable using Generative AI due to a lack of trust that it will be accurate.

The research is important because it explores new technologies and compares them to trusted, more integrated technologies that have been used in the past.


## Methodology

I first came up with a set of questions, neatly classified into categories:

- Facts
- Current facts
- Explanations
- Comparison
- Research
- Trick Questions

After choosing the questions, I automated a Python program that gathered all the online responses for me. I implemented API keys into the program.

This saved time for the alternative would be manually asking questions to the AIs and doing research on my own.

Unfortunately, there was no better way to search the physical World Book than manually, so I looked through the sets of books for every one of the 36 questions.

Data gathered from Google and Bing was to be summarized by AI to keep it concise.

Once the answers are gathered, I established a judging criteria along 4 dimensions:

- Clarity
- Completeness
- Accuracy
- Brevity

The judging was done by two judges, using another program I wrote to capture their responses. They were given the question asked to the 6 research tools and the answers. They had to choose the response that best fit the four categories, clarity, completeness, accuracy, and brevity.

To keep the judging objective, I chose to hide the source of information from the judges.

## Dataset

Some example questions for each category would be:

- "What does fruitless mean?" - Facts
- "What is the current US debt?" - Current Facts
- "Explain what supply and demand mean." - Explanations
- "Compare speed and velocity." - Comparisons
- "Find a primary source about the Boston Massacre." - Research
- "Why did George W. Carver invent the street lamp?" - Trick Questions

The full set of questions is  shared in the [references section](#references)

## Observations

Some search engines decided to auto-correct questions. For example, Google Search interpreted the question "What's the chemical formula for silicone?" and decided I was probably looking for silicon. Its response was describing what silicon was for, even though I asked for silicone.

Manual information gathering was surprisingly difficult. Print encyclopedia are obsolete quickly, especially on current topics. The encyclopedias were more helpful when it came to history, but when it came to anything tech related, there was nothing.

Wikipedia also seemed more up to date than the World Book encyclopedia, especially because the World Book I researched from was printed in 2020. However, tech was still big in 2020, but the World Book still seemed to lack such information.

Discussion forums like Reddit are great for subjective opinions, but not reliable sources of information. Google kept giving websites that AI summarized as "A discussion about...", which is most likely Reddit.

The AI responses are vastly more reliable and comprehensive than expected. The AIs were able to understand the question and break it down. For example, the AIs explained the error in detail before explaining what might've influenced your error. This is true especially for the question "What happened to the fifth plane during 9/11?". They both said that there was no fifth plane before suggesting what the question could have been looking for.

The 2 judges made the same choice 66 times out of all 144 questions they were asked, about 45.8% of the time. This is a pretty high agreement rate, and it was especially high for brevity, which was 61.1%.

## Survey Data

| **Category** | **ChatGPT** | **Gemini** | **Google** | **Bing** | **Wikipedia** | **World Book** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Basic Facts | 37.5% (18) | 35.4% (17) | 8.3% (4) | 2.1% (1) | 8.3% (4) | 8.3% (4) |
| Current Facts | 16.7% (8) | 12.5% (6) | 18.8% (9) | 39.6% (19) | 12.5% (6) | 0.0% (0) |
| Explanations | 33.3% (16) | 43.8% (21) | 8.3% (4) | 8.3% (4) | 2.1% (1) | 4.2% (2) |
| Comparisons | 43.8% (21) | 29.2% (14) | 14.6% (7) | 6.3% (3) | 0.0% (0) | 6.3% (3) |
| Research and Source Finding | 37.5% (18) | 45.8% (22) | 6.3% (3) | 6.3% (3) | 0.0% (0) | 4.2% (2) |
| Trick Questions | 41.7% (20) | 50.0% (24) | 8.3% (4) | 0.0% (0) | 0.0% (0) | 0.0% (0) |
| All categories | 35.1% (101) | 36.1% (104) | 10.8% (31) | 10.4% (30) | 3.8% (11) | 3.8% (11) |

## Results

### Basic Facts

First of all, what I noticed was that my basic facts were sometimes too complicated. For example, "What is the largest planet we have discovered?" should've been in the current facts section. Also, asking an encyclopedia how many coding languages exist would be challenging to find.

Overall, ChatGPT was favored for this type of question, being chosen 18 times out of the 48 selections. Gemini came in close second, getting 17 out of 48 choices. On the other hand, Bing was only chosen once in this batch of questions.

### Current Facts

Bing turned out to be the most preferred when it came to current facts earning 19 out of 48. It was great at completeness and accuracy.

Also, this is a category that is tricky for encyclopedias because paper cannot constantly update. World Book's responses were all N/A because most of the information was too specific.

### Explanations

Gemini excelled at this category, especially for accuracy. It earned 21 out of 48 of the votes. Explanations should be easy for AI because it can choose what to say and try to make it easy for a human to understand. However, encyclopedias are intended to be informative, which are not aimed at answering a specific question.

### Comparisons

Comparisons should be challenging for something like an encyclopedia because it has different sections for each topic, not sections comparing two topics. To work around this, I searched each topic individually in the World Book and merged what I found.

The search engines were able to find websites comparing the two topics, but AI clearly has the advantage here.

ChatGPT took the top slot, earning 21 out of the 48 selections. It was concise and accurate, but Google did really well in completeness for a website could include more information than an AI would.

### Research / Source finding

One would expect one of the search engines to do really well in this category, but once again, one of the AIs takes first prize.

Gemini did the best, getting 22 out of 48 options, probably because in some of its responses it names the source. It did really well for clarity.

For one of the questions, since the request was formatted like a question, Google saw the first word "I", and decided that I was looking for the 9th letter of the alphabet.

### Trick Questions

Gemini was the best for this category, getting 24 out of 48 votes, which is exactly half. AIs have the advantage because they can point out the user's mistake, whereas websites and encyclopedias can only give related information.

## Limitations

- The experiment only included 36 questions and 2 judges.
- The judgements were based on appearance only, not actual fact checking.
- Current facts can change after the results were gathered
- World book was from 2020
- Some questions were ambiguous, contained typos, and were hard for some sources to interpret.
- Once the user was able to guess if a number was a type of source, the order never changed, so this could incorporate bias
- Having AI summarize websites hid other parts of the website that sometimes answered the question.

## Conclusion

It was clear from the results that for comprehensive research, one source wasn't always the best. It is important to choose the right source of information based on the type of question.

Another notable observation is that the people I'd surveyed preferred the generative AIs over the other options, choosing them ~70% of the time. This indicates that over time, AI responses are going to be more comprehensive and will become the most preferred option for student research.

## References

1. Questions: [https://github.com/suryarajidev/best-research-tool/blob/2ce4d24330843e015bdcb32f3a192b8b4c852dee/output.csv](https://github.com/suryarajidev/best-research-tool/blob/2ce4d24330843e015bdcb32f3a192b8b4c852dee/output.csv)
2. Program to get results: [https://github.com/suryarajidev/best-research-tool/blob/2ce4d24330843e015bdcb32f3a192b8b4c852dee/src/main.py](https://github.com/suryarajidev/best-research-tool/blob/2ce4d24330843e015bdcb32f3a192b8b4c852dee/src/main.py)
3. Program to get survey results: [https://github.com/suryarajidev/best-research-tool/blob/2ce4d24330843e015bdcb32f3a192b8b4c852dee/src/ask\_questions.py](https://github.com/suryarajidev/best-research-tool/blob/2ce4d24330843e015bdcb32f3a192b8b4c852dee/src/ask_questions.py)


