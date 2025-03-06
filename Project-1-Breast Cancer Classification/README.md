## Project-1 Breast Cancer Classification


This repository is divided in two parts. The first part contains code for a breast cancer classification project using Support Vector Machines (SVM). And a second part about feature reduction using Principal Component Analysis (PCA).

The project demonstrates how to preprocess data, train an SVM model, evaluate its performance, and perform feature reduction using Principal Component Analysis (PCA).

## Introduction

Cancer remains one of the most significant health challenges worldwide. Early and accurate detection is crucial for effective treatment and improved patient outcomes. Machine learning, specifically Support Vector Machine (SVM), offers a powerful tool for classifying cancerous and healthy tissues based on various biomarkers. This project aims to build an SVM model to classify samples as either cancerous or healthy using Python. On the other hand, with the PCA application to the dataset to reduce the dimensionality while retaining most of the variance in the data. This step helps in simplifying the model, reducing computational cost, and potentially improving the model's generalization.

## Objectives

1. **Data Collection and Preprocessing**: Gather a dataset containing cancerous and healthy samples and preprocess it for model training.
2. **Model Building**: Construct an SVM model to classify the samples.
3. **Model Evaluation**: Assess the performance of the SVM model using appropriate metrics.
4. **Feature Reduction (PCA)**: Perform PCA to reduce the dimensionality of the dataset and evaluate the impact on model performance.
5. **Conclusion**: Summarize the findings and discuss the effectiveness of the SVM model and the PCA analysis for this classification task.


## Repository Structure

- **Breast_Cancer_Classification/**
  - **SVM_Full_Features/**
    - `Breast-Cancer-SVM.ipynb`
    -  `svm_model.h5`
    - `README.md`
    - `LICENSE.txt`
  - **PCA_Feature_Reduction/**
    - `Breast-Cancer-PCA.ipynb`
    - `important_features_dataset.csv`
    - `README.md`
    - `LICENSE.txt`
  - **SVM_Reduced_Features/**
    - `Breast-Cancer-SVM-reduced-features.ipynb`
    -  `important_features_dataset.csv`
    - `svm-reduced-features_model.h5`
    - `README.md`
    - `LICENSE.txt`
  - `README.md`


## Results 
Initial SVM Model (Full Features): Achieved 96% accuracy using an SVM model with C=1.0 on the original dataset with full features.

PCA Applied Dataset: After applying PCA to reduce dimensionality, a **96% accuracy** value is achieved using SVM with C=10. This suggests that the reduced dataset maintains predictive power comparable to the original full-feature dataset.

 PCA successfully reduced the dataset's dimensionality while preserving most of the predictive information, as evidenced by the consistent 96% accuracy. Both the original SVM model on full features and the PCA-reduced SVM model perform equally well, indicating that PCA can simplify the model without sacrificing accuracy.

The choice of C=10 for SVM in the reduced dataset suggests that adjusting hyperparameters post-PCA may be necessary for optimal performance.


## Requirements

    Python 3.8.3
    Pandas 2.0.3
    Numpy 1.21.0
    Scikit-learn 1.3.2
    Matplotlib 3.2.2
    Seaborn 0.10.1


## Dataset

The dataset used in this project is the Breast Cancer Wisconsin (Diagnostic) dataset, available in the sklearn.datasets module.



## License

This project is licensed under the terms of the MIT license (See LICENSE.txt)
