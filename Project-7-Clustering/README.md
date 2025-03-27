## Clustering

**Clustering** is a fundamental technique in **unsupervised machine learning**, essential for grouping similar data points without prior knowledge of labels. It helps in discovering hidden patterns and structures within data. In this repository, we apply two popular clustering algorithms **K-Means** and **DBSCAN** to the Iris dataset.


### Repository Structure

- **Clustering/**
  - **DBSCAN/**
    - `Clustering-DBSCAN.ipynb`
    - 
  - **K-Means/**
    - `Clustering-K-Means.ipynb`
    - `kmeans_model.joblib`
    - `iris_clusters.png`
  - **data/**
    - `iris_with_clusters.csv`
  
   

## Requirements

    Python 3.8.3
    Pandas 2.0.3
    Numpy 1.21.0
    Scikit-learn 1.3.2
    Matplotlib 3.2.2
    Seaborn 0.10.1


## Dataset

The dataset used in this project is the Iris dataset, available in the seaborn datasets module.

The Iris dataset contains 150 samples of iris flowers, each with four features: sepal length, sepal width, petal length, and petal width. The dataset is labeled with three species: setosa, versicolor, and virginica.


## License

This project is licensed under the terms of the MIT license (See LICENSE.txt)
