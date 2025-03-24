# Clustering

Welcome to the **Clustering** section! This folder provides an introduction to clustering techniques, which are essential for unsupervised learning tasks. Clustering helps you group similar data points together, making it easier to identify patterns or categories within your data.

**Note**: The notebooks here are designed for beginners. They introduce foundational concepts but do not cover all available clustering methods or advanced techniques. For a more comprehensive understanding, please refer to the recommended resources provided below.

---

## 📂 Structure

This folder currently includes:
- **Agglomerative Clustering**: A hierarchical clustering technique based on merging clusters.
- **DBSCAN**: A density-based clustering method, useful for identifying clusters of arbitrary shape.
- **K-Means**: A popular clustering method that partitions data into a specified number of clusters.
- **K-Medoids**: A robust clustering algorithm that partitions data into clusters by selecting actual data points (medoids) as cluster centers. It minimizes the sum of dissimilarities between points and their assigned medoid, making it more resilient to outliers than K-Means.
- **Spectral Clustering**: A technique for clustering data that is not linearly separable, using eigenvalues of a similarity matrix.
- **Clustering Quality Evaluation**: Evaluate the performance of various clustering algorithms
- **Comparison of Various Clustering Algorithms**: Compare various clustering algorithms to find which one suits your data the best.

Each section includes **assignments** to help reinforce your understanding, along with **solutions** for self-assessment.

---

## 🔗 Learning Flow

Follow these steps to build a strong foundation in clustering techniques:

### 1. **Agglomerative Clustering**
   - **Purpose**: This hierarchical clustering method begins by treating each data point as an individual cluster, then successively merges the closest clusters.
   - **Topics to Cover**:
     - Basics of hierarchical clustering
     - Linkage criteria (single, complete, average)
     - Dendrograms for visualizing hierarchical clusters
   - **Resources**:
     - [Agglomerative Clustering (Sklearn Documentation)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html)
     - [Hierarchical Clustering Tutorial](https://www.datacamp.com/tutorial/hierarchical-clustering-python) (DataCamp)
     - [StatQuest's Hierarchical Clustering](https://www.youtube.com/watch?v=7xHsRkOdVwo) (video)

### 2. **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**
   - **Purpose**: DBSCAN identifies clusters based on data density, making it useful for detecting clusters with arbitrary shapes.
   - **Topics to Cover**:
     - Core points, border points, and noise points
     - Selecting parameters like epsilon and minimum samples
     - DBSCAN’s advantages for handling noise and non-linear shapes
   - **Resources**:
     - [DBSCAN (Sklearn Documentation)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)
     - [DBSCAN Tutorial](https://towardsdatascience.com/dbscan-clustering-algorithm-5e3c78e021eb) (Towards Data Science)
     - [StatQuest's DBSCAN](https://www.youtube.com/watch?v=RDZUdRsdvOU) (video)

### 3. **K-Means**
   - **Purpose**: K-Means is a partitioning clustering algorithm that aims to split data into a predefined number of clusters.
   - **Topics to Cover**:
     - Centroid calculation and cluster assignment
     - Elbow method for choosing the optimal number of clusters
     - Limitations of K-Means (e.g., sensitivity to initial centroids)
   - **Resources**:
     - [K-Means (Sklearn Documentation)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
     - [K-Means Clustering Guide](https://www.kaggle.com/code/kandij/k-means-clustering-tutorial/notebook) (Kaggle tutorial)
     - [K means Clustering Algorithm](https://www.youtube.com/watch?v=EItlUEPCIzM) (video)

### 4. **Spectral Clustering**
   - **Purpose**: Spectral Clustering is a technique for clustering data that is not linearly separable. It uses the eigenvalues of a similarity matrix to perform dimensionality reduction before clustering in the lower-dimensional space.
   - **Topics to Cover**:
     - Affinity matrix and graph Laplacian
     - Eigenvalue decomposition and its role in clustering
     - Parameter selection (e.g., `n_clusters`, `affinity`, `gamma`)
   - **Resources**:
     - [Spectral Clustering (Sklearn Documentation)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html)
     - [Spectral Clustering Explained](https://towardsdatascience.com/spectral-clustering-aba2640c0d5b) (Towards Data Science)
     - [Wikipedia: Spectral Clustering](https://en.wikipedia.org/wiki/Spectral_clustering)

### 5. **Clustering Quality Evaluation**
   - **Purpose**: Clustering evaluation metrics help assess the performance of the Clustering Algorithms.
   - **Topics to Cover**:
     - Silhouette Score
     - Davies Bouldin Index
     - Adjusted Rand Score (ARI)
   - **Resources**:
     - [Clustering Performance Evaluation (sklearn documentation)](https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation)
     - [Clustering Metrics in Machine Learning (GeeksForGeeks)](https://www.geeksforgeeks.org/clustering-metrics/)

## 6. **Comparing Various Clustering Algorithms**
  - **Purpose**: Comparing different clustering algorithms.
  - **Topics to Cover**:
    - Compare K - Means, Hierarchical and DBSCAN (Density Based Spatial Clustering of Applications with Noise).
    - Compare strengths and weaknesses of each.
    - Compare the runtime complexity of each. 
 - **Resources**:
   - [Compare different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)
   - [Clustering Algorithms: A comparative Approach](https://pmc.ncbi.nlm.nih.gov/articles/PMC6333366/)
   - [Comparing different clustering algorithms (video)](https://www.youtube.com/watch?v=K_KibNSH1_0)

---

## 📝 Assignments and Solutions

Each clustering method comes with assignments designed to help you apply the concepts you've learned. Solutions are provided for self-evaluation. Try to complete the assignments independently before checking the solutions for the best learning experience.

---

## 🏁 Getting Started

1. **Begin with Agglomerative Clustering**: Start by understanding how hierarchical clustering builds clusters step-by-step.
2. **Explore DBSCAN**: Learn how DBSCAN groups data based on density, making it robust for non-linear data.
3. **Try K-Means**: Experiment with partitioning data into clusters, focusing on selecting the optimal number of clusters.
4. **Dive into Spectral Clustering**: Understand how Spectral Clustering handles non-linearly separable data using eigenvalues and similarity matrices.
5. **Evaluate Performance**: Assess the performance of the above-mentioned algorithms and find the most suitable one for your data.
6. **Explore various clustering algorithms**: Experiment with various other clustering algorithms to compare and see which one is the best for your data.

---

Happy clustering! Developing these skills will enable you to analyze data and identify patterns effectively. For further learning, refer to the documentation and tutorials linked above.
