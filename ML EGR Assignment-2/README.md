# EE-658-758-Machine-Learning-in-Engineering-Assignment-2-Logistic-Regression


**Logistic Regression with Non-linear Decision Boundary**

Logistic regression is typically used for classification tasks where the decision boundary between classes can be approximated by a straight line. However, in cases where the decision boundary is non-linear, we can enhance the model's performance by adding non-linear transformations to the original features.

**The Dataset**

Assume we have a dataset named data.csv with three columns: Feature1, Feature2, and Label. The Label column contains binary values (0 or 1), representing two different classes. The dataset is not linearly separable, meaning a straight line cannot perfectly separate the two classes.

**Logistic Regression with Scikit-learn**

- Loaded the dataset and split it into training and testing subsets.
- Developed a logistic regression model using the scikit-learn library based on the training data, using only Feature1 and Feature2.
- Plotted the data points and the decision boundary of the model.
- Evaluated the model on the testing data and reported its accuracy.

**Logistic Regression Without Scikit-learn**

- Implemented logistic regression from scratch.
- Used the same training and testing data splits as in Part A.
- Developed a logistic regression model based on the training data, using only Feature1 and Feature2.
- Displayed the cost (loss) as a function of iterations during the training process.
- Plotted the data points and the decision boundary of the model.
- Evaluated the model on the testing data and reported its accuracy.

**Logistic Regression with Feature Engineering (Scikit-learn)**

- Enhanced the dataset by adding new features that are at a higher degree of one of the original features (e.g., Feature1^2, Feature1 * Feature2).
- Used the scikit-learn library to develop a logistic regression model based on the enhanced training data.
- Plotted the data points and the decision boundary of the model.
- Evaluated the model on the testing data and reported its accuracy.

**Logistic Regression with Feature Engineering (Without Scikit-learn)**

- Used the enhanced dataset from Part C.
- Implemented logistic regression from scratch to develop a model based on the enhanced training data.
- Displayed the cost (loss) as a function of iterations during the training process.
- Plotted the data points and the decision boundary of the model.
- Evaluated the model on the testing data and reported its accuracy.

Each part of this assignment explores different aspects of logistic regression, including using libraries like scikit-learn and implementing the algorithm from scratch. Results and insights from each part are summarized in the respective sections of this README file.
