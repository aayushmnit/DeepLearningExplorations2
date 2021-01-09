My solution to solve a simple practice NLP classification challenge on Analytics Vidhya's website - [Identify the Sentiments](https://datahack.analyticsvidhya.com/contest/linguipedia-codefest-natural-language-processing-1/). Here is where I stand with few hours of hacking - 
![alt text](./img/website_capture.PNG "Snapshot from leaderboard")

## Problem statement - 
Sentiment analysis remains one of the key problems that has seen extensive application of natural language processing. This time around, given the tweets from customers about various tech firms who manufacture and sell mobiles, computers, laptops, etc, the task is to identify if the tweets have a negative sentiment towards such companies or products.

## Dataset
The train set contains 7,920 tweets
The test set contains 1,953 tweets

## Data Pre-processing 
(It's pretty standard so I took it from here - [Link](https://github.com/iamarkaj/Identify-the-Sentiments))
- Lower-case all characters
- Remove twitter handles
- Remove urls
- Replace unidecode characters
- Only keep characters
- Keep words with length>1 only
- Replace words like 'whatisthis' to ' what is this'
- Remove repeated spaces

## Approach
1)  [FastAI ULM FIT Approach](https://docs.fast.ai/tutorial.text.html)  
    - Fine tune a language model on training/testing data
    - Train a classifier using [AWD-LSTM](https://docs.fast.ai/text.models.awdlstm.html)
    - Got a public LB of 0.89xx using this approach
    - Refer to 1_Training_ULMFIT.ipynb

2) [Blurr: Using Hugging face transformers(bert-uncased) and FastAI](https://ohmeow.github.io/blurr//)
    - Take a [bert-base-uncased](https://huggingface.co/bert-base-uncased) pre-trained transformer model to create embeddings and put a classifier on top to finetune it for the classification class
    - Got a public LB of 0.91xx using this approach
    - Refer to 2_Training_Blurr_bert_uncased.ipynb

3) [Blurr: Using Hugging face transformers(roberta-base) and FastAI](https://ohmeow.github.io/blurr//)
    - Take a [roberta-base](https://huggingface.co/roberta-base) pre-trained transformer model to create embeddings and put a classifier on top to finetune it for the classification class
    - Got a public LB of 0.91xx using this approach
    - Refer to 3_Training_Blurr_roberta_base.ipynb

4) Take model ouput predictions probability from 2 & 3 and average it to create an ensemble. Achieved ~.91xx-.92xx depending on training conditions
    - Refer to 4_Ensemble.ipynb

