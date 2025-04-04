# 🗂 Text Classification

Welcome to the **Text Classification** section! This notebook compares traditional machine learning and deep learning models for classifying text data. Whether you're building a spam detector or analyzing sentiments, text classification is a core task in **Natural Language Processing (NLP)**.


## 📚 What’s Inside?

This notebook covers:

- **Naïve Bayes**: Fast, simple, and effective for clean datasets.
- **Logistic Regression**: A good, interpretable baseline for binary text classification.
- **Random Forest**: Captures feature interactions and non-linear patterns.
- **LSTM (Long Short-Term Memory)**: Great for handling sequences and capturing context.
- **Transformers (BERT)**: State-of-the-art models for understanding language and context.

Each model is evaluated using:

- **Accuracy**
- **Precision, Recall, F1-Score**
- **Confusion Matrix**


## 🔄 Workflow Overview

1. **Preprocessing**
    - Split the dataset.
    - Convert text into numerical vectors using **TF-IDF** or **Tokenization + Padding**.

2. **Traditional Models**
    - Train and evaluate **Naïve Bayes**, **Logistic Regression**, and **Random Forest** on TF-IDF features.

3. **Deep Learning**
    - Use an **LSTM model** built with Keras to capture text sequences and dependencies.

4. **Transformers**
    - Load **BERT** using Hugging Face and fine-tune it for classification.

5. **Model Evaluation**
    - Display confusion matrices and metrics for comparison.


## 🚀 Learning Goals

- Understand how different models perform on the same classification task.
- Learn when to use simple models vs. deep learning.
- Explore trade-offs in speed, accuracy, and interpretability.


## 🔗 Helpful Resources

- [Text Classification Overview ](https://levity.ai/blog/text-classification)
- [Understanding LSTMs ](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [Transformers for LLMs ](https://medium.com/@jimwang3589/what-are-the-different-transformers-for-llms-like-bert-chatgpt-and-google-flan-t5-2a52f4dd132f)
- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers/en/tasks/sequence_classification)

