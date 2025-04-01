## Clustering

### Clustering using DBSCAN

### Overview


**DBSCAN** (Density-Based Spatial Clustering of Applications with Noise)

**DBSCAN** is a density-based clustering algorithm that identifies clusters in data based on the density of points in a given neighborhood. Unlike k-means, DBSCAN does not require specifying the number of clusters beforehand and is effective at detecting clusters of arbitrary shape while handling noise (outliers).

**Key Concepts**

  *  Core Points: Points with at least min_samples neighbors within a radius of eps.

  *  Border Points: Points within eps of a core point but with fewer than min_samples neighbors.

  *  Noise Points: Points that do not belong to any cluster.

**How It Works**

   1- A random unvisited point is selected.

   2- If it is a core point, a new cluster is formed, and all density-reachable points are added.

   3- The process continues recursively until all points are assigned to a cluster or labeled as noise.

**Advantages**

✔️ Detects clusters of arbitrary shape.

✔️ Handles outliers effectively.

✔️ No need to predefine the number of clusters.

**Limitations**

⚠️ Choosing optimal eps and min_samples can be challenging.

⚠️ Struggles with varying density clusters.

DBSCAN is widely used in geospatial data analysis, anomaly detection, and customer segmentation, among other applications.





### Results

<img src="https://github.com/user-attachments/assets/03bbcd7b-480e-4da9-a0c2-3f21d47e2e32" width="400">

While DBSCAN could distinguish some clusters, its performance was affected by the density-based nature of the algorithm. It does not explicitly match the original species labels but instead finds natural groupings based on data density.
