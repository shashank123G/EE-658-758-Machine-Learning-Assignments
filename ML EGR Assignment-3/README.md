### Customer Segmentation and Classification Project

This project involves data preprocessing, implementing neural networks from scratch and using numpy and scikit-learn, as well as logistic regression to perform customer segmentation and classification.

All the code and implementations are available in Jupyter Notebook.

#### How to Use:

1. Clone the repository to your local machine.
2. Ensure you have Jupyter Notebook installed.
3. Open Jupyter Notebook and navigate to the cloned repository directory.
4. Open each Jupyter Notebook file (.ipynb) to view and run the code.

#### Data Preprocessing:

- The dataset is loaded and explored to understand its structure and characteristics.
- Null values are handled using appropriate techniques such as imputation or removal.
- Categorical variables are converted to numerical format and encoded.
- The target variable 'Segmentation' is encoded for classification.

#### Neural Network Implementation from Scratch:

- A two-layer neural network model is implemented from scratch focusing on understanding the mathematics and operations of forward propagation and backpropagation.
- The model is applied to the preprocessed dataset.

#### Neural Network using Scikit-learn:

- MLPClassifier class of scikit-learn is used to implement neural network models with 2 and 3 layers.
- The models are trained on the preprocessed dataset.
- The accuracy of the two-layer neural network model is studied with varying numbers of neurons in each hidden layer.
- A graph is plotted to visualize the relationship between the number of neurons and accuracy.

#### Logistic Regression Implementation:

- Logistic regression model is implemented using scikit-learn as a baseline for comparison.
- The model is trained on the same preprocessed dataset.

#### Evaluation and Comparison:

- Learning curves for each model are displayed to understand the training process.
- The performance of each model is evaluated using confusion matrix and classification report.
- A comparison between the neural network models and logistic regression is provided, discussing their strengths and weaknesses.

#### Conclusion:

This project provides a comprehensive analysis of customer segmentation and classification using various machine learning techniques, including neural networks and logistic regression. It aims to understand the effectiveness of different approaches in segmenting customers and predicting their behavior.
