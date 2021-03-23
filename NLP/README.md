# Natural Language Processing: Amazon Review Data Classification
## Project Overview:

Imagine you are in charge of feedback analytics at Amazon, you are provided with the raw product review data and your task is to route it to appropriate parties that can handle questions related to product categories that they are concerned with. your first step would be to classify the dataset into distinct categories, such that people who perform sentiment analysis on book-related items don't have to deal with the expired food or malfunctioning adult toy complaints.

This project aims to do precisely that, it attempts to experiment with different natural language processing techiques to achieve highest classification accuracy on amazon reviews dataset stored in json format.

Some of the techniques employed are:

* **Bag of Words**
* **Word Embedding** (word vectors)
* **Lemitising** and **Stemming** words
* **Stopwords** removal
* **Regex** Filtering
* Fine-tuning **Bert Model**

## Packages:
**Python Version:** 3.7

**Packages:** Pandas, Numpy, Sklearn, nltk, spaCy