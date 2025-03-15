# Model Tuning

Welcome to the **Model Tuning** section! This notebook explores hyperparameter tuning, a crucial step in optimizing machine learning models. By systematically adjusting model parameters, we can enhance performance and achieve better accuracy. We will compare different tuning strategies, including Grid Search, Random Search, and Bayesian Optimization.

**Note**: This notebook is intended for beginners, covering fundamental concepts and implementation steps. For a deeper understanding, please refer to the additional resources provided below.

# 📂 Structure
This folder currently includes:

**Bayesian Optimization**: Bayesian Optimization is a sequential model-based optimization technique that builds a probabilistic model (typically using Gaussian Processes) to find optimal hyperparameters.



## 🔗 Learning Flow
### **Start with Model Tuning Basics**: Learn about hyperparameters and their impact on model performance.

###  **Explore Different Tuning Methods**: Understand the strengths and limitations of Grid Search, Random Search, and Bayesian Optimization.
   
### **Bayesian Optimization** : Unlike Grid Search and Random Search, Bayesian Optimization builds a probabilistic model to select the most promising hyperparameter values intelligently.
   -**Topics to Cover**:

    a. Understand Bayesian Optimization: Learn about probabilistic models and acquisition functions (e.g., Expected 
          Improvement, Probability of Improvement, Upper Confidence Bound) to decide the next sampling point.

    b. Compare with Traditional Methods: See how Bayesian Optimization improves efficiency.

    c. Implement Optimization: Apply Bayesian tuning to a machine learning model.

    d. Visualize and Analyze: Interpret results to choose the best hyperparameters effectively.
   
   -**📘 Recommended Resources**:
1. https://medium.com/@abelkuriakose/a-guide-to-hyperparameter-tuning-enhancing-machine-learning-models-69dc9e0f02ea
2. Bayesian Optimization with Scikit-Optimize (Sklearn Documentation)


## Happy Learning!
# Grid Search for SVM - Wine Quality Dataset

## Overview
This project applies Support Vector Machines (SVM) to the Wine Quality dataset. It explores model performance before and after hyperparameter tuning using Grid Search.

## Workflow
1. Load the Wine Quality dataset.
2. Train an SVM model with default parameters.
3. Use GridSearchCV to optimize `C`, `kernel`, and `gamma`.
4. Compare performance before and after tuning.
5. Evaluate results using classification reports.

## Results Summary
- Accuracy improved from 0.60 to 0.61 after tuning.
- F1-score and recall slightly improved for most classes.
- Macro and weighted averages showed minor improvements.

## How to Use
Run `grid_search_svm.ipynb` to execute the workflow and review results. Ensure required dependencies (scikit-learn, pandas, numpy, etc.) are installed.

## References
- Scikit-learn documentation: https://scikit-learn.org/
- Wine Quality dataset: https://archive.ics.uci.edu/ml/datasets/Wine+Quality





