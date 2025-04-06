# Assignment: Text Classification in NLP

## Q1. Load and Preprocess the Dataset
- Choose a dataset: SMS Spam Collection, IMDb Movie Reviews, or AG News / News Category Dataset
- Perform exploratory data analysis (EDA)
- Clean the text (lowercasing, punctuation removal, etc.)
- Split the dataset into training and test sets

## Q2. Train Traditional Machine Learning Models
- Use TF-IDF vectorization
- Train the following models:
  * Naïve Bayes
  * Logistic Regression
  * Random Forest
- Evaluate using: Accuracy, Precision, Recall, F1-Score, Confusion Matrix
- Perform hyperparameter tuning using GridSearchCV

## Q3. Build and Train an LSTM Model
- Tokenize and pad text sequences
- Build an LSTM model using Keras or PyTorch
- Train the model and evaluate it on the test set
- Report the same metrics: Accuracy, Precision, Recall, F1-Score, Confusion Matrix

## Q4. Fine-tune a BERT Model for Text Classification
- Load a pre-trained BERT model (e.g., bert-base-uncased) using Hugging Face
- Fine-tune the model on your dataset
- Evaluate it using:
  * Accuracy
  * Precision, Recall, F1-Score
  * Confusion Matrix

## Q5. Compare All Models
- Create a comparison table for the above different methods of text classification
- Discuss:
  * Which model performed best and why?
  * Trade-offs in performance, time, and resources
  * Which model is ideal for deployment?

## Q6. Additional Improvements
- Visualize confusion matrices or ROC curves
- Try other transformer models like DistilBERT or RoBERTa
- Implement ensemble methods or model stacking

## Submission Instructions
- Ensure:
  * All outputs are visible
  * Each step is well-documented using Markdown
  * Final results and discussion are clearly presented