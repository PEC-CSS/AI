# Linear Regression and Logistic Descent Notebooks

# Linear Regression

## Overview
This contains Jupyter notebooks implementing linear regression and gradient descent algorithms. These notebooks provide step-by-step explanations, code implementations, and visualizations to help understand these fundamental machine learning concepts.

## Contents
1. **1_linear_regression.ipynb**  
   - Implements simple linear regression using least squares.
   - Demonstrates the relationship between independent and dependent variables.
   - Uses visualization to illustrate regression lines and predictions.

2. **2_linear_regression_multivariate.ipynb**  
   - Extends linear regression to multiple variables (multivariate regression).
   - Implements the normal equation method for finding optimal parameters.
   - Includes feature normalization and data preprocessing techniques.

3. **gradient_descent.ipynb**  
   - Explains the concept of gradient descent for optimization.
   - Implements batch gradient descent for linear regression.
   - Compares learning rates and their impact on convergence.
   - Provides plots to visualize cost function behavior over iterations.

## Prerequisites
Ensure you have the following dependencies installed:

```bash
pip install numpy pandas matplotlib sklearn
```

# Spam Detection using Logistic Regression

This project uses **Logistic Regression** to classify SMS messages as **spam** or **ham** (not spam). The dataset used is the SMS Spam Collection Dataset.

## Features

- Text preprocessing using **NLTK** (stopwords removal, tokenization, etc.).
- Feature extraction using **TF-IDF Vectorization**.
- Model training using **Scikit-Learn's Logistic Regression**.
- Performance evaluation using metrics like accuracy, precision, and recall.

## Installation

### Prerequisites

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Dataset

- The dataset can be accessed using this link (<https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset>).





