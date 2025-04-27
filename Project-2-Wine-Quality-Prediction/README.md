# Project-2- Wine Quality Prediction
 
The main goal is to build a robust machine learning model that can accurately **predict the quality of wines** using physicochemical variables such as acidity, alcohol concentration, pH, etc. In this classification problem, the quality of wine can be represented as a discrete variable, often categorized into classes such as bad, and good quality. Various classification algorithms such as **Logistic Regression**, **Random Forest**, **XGBoost**, and a **Deep Neural Network** are considered.

In addition, a Streamlit web app was created.
https://wine-quality-ml-prediction.streamlit.app/

![image-Wine-ML]("https://github.com/user-attachments/assets/27c3932d-75ef-4ed7-8e2a-36b909339ba3" width="400")


# Results

The most relevant results obtained for the Machine Learning algorithms explored are ( order based on the Validation Accuracy):
* **Deep Neural Network (94.92%)**
* **XGBoost (92.89%)**
* **Random Forest (89.59%)**
* **Logistic Regression (84.77%)**
  
The accuracy of the wine quality prediction results can be improved by increasing the amount of data obtaining a superior balance between the different classes of wine quality studied here.


# Requirements

* Python 3.8.3
* TensorFlow  2.10.0
* Pandas 1.0.5
* Numpy  1.23.4
* Scikit-learn 1.3.2
* Keras  2.10.0
* Streamlit 1.22.0

# Dataset

In this project I am using the wine quality dataset available on Kaggle for free.
https://www.kaggle.com/datasets/yasserh/wine-quality-dataset?resource=download&select=WineQT.csv

# License

This project is licensed under the terms of the MIT license (See LICENSE.txt)
