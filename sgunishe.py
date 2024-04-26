import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from xgboost import XGBClassifier
from sklearn.neural_network import MLPClassifier
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score


@st.cache
def load_data(dataset_name):
    if dataset_name == 'IRIS':
        data = datasets.load_iris()
    elif dataset_name == 'Digits':
        data = datasets.load_digits()
    return data

dataset_name = st.sidebar.selectbox("Select Dataset", ("IRIS", "Digits"))
data = load_data(dataset_name)


classifier_name = st.sidebar.selectbox("Select Classifier", ("Neural Networks", " XGBoost", "CatBoost", "LightGBM"))

if classifier_name == "Neural Networks":
    classifier = MLPClassifier()
elif classifier_name == " XGBoost":
    classifier = XGBClassifier()
elif classifier_name == "CatBoost":
    classifier = CatBoostClassifier()
elif classifier_name == "LightGBM":
    classifier = LGBMClassifier()
    
    
# Training the model:
X = data.data
y = data.target
        

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

classifier.fit(X_train_scaled, y_train)
y_pred = classifier.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
st.write(f"Model trained with accuracy: {accuracy:.2f}")
    

feature_values = []
for i in range(X_train_scaled.shape[1]):
    feature_values.append(st.sidebar.number_input(f"Enter feature {i+1} value", value=0.0))


if st.sidebar.button("Make Prediction"):
    input_data = [feature_values]
    prediction = classifier.predict(input_data)
    st.write(f"Prediction: {prediction}")


st.title("Machine Learning Models Interaction")
st.sidebar.title("Options")


