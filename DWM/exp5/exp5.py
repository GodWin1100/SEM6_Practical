import numpy as np
import matplotlib.pyplot as plt


class KMeansClustering:
    def __init__(self):
        self.num_centers = 3
        self.center_0 = None
        self.center_1 = None
        self.center_2 = None

    def fit(self, X, num_iters=20):
        self.center_0 = np.random.normal(0, 10, (1, 2))
        self.center_1 = np.random.normal(0, 10, (1, 2))
        self.center_2 = np.random.normal(0, 10, (1, 2))
        centers = [self.center_0, self.center_1, self.center_2]
        distances = np.zeros((300, 3))
        for _ in range(num_iters):
            for i, center in enumerate(centers):
                distances[:, i] = ((center - X) ** 2).sum(axis=1)
        cluster_index = np.argmin(distances, axis=1)
        for i in range(len(centers)):
            centers[i] = X[cluster_index == i].mean(axis=0)
        self.center_0 = centers[0]
        self.center_1 = centers[1]
        self.center_2 = centers[2]


cluster_0 = np.random.normal(-50, 10, (100, 2))
cluster_1 = np.random.normal(0, 10, (100, 2))
cluster_2 = np.random.normal(50, 10, (100, 2))
X = np.vstack([cluster_0, cluster_1, cluster_2])
kmeans_cluster = KMeansClustering()
kmeans_cluster.fit(X, num_iters=50)
print(
    "The x and y coordinates for centroid 1 is({}, {})".format(kmeans_cluster.center_0[0], kmeans_cluster.center_0[1])
)
print(
    "The x and y coordinates for centroid 2 is({}, {})".format(kmeans_cluster.center_1[0], kmeans_cluster.center_1[1])
)
print(
    "The x and y coordinates for centroid 3 is({}, {})".format(kmeans_cluster.center_2[0], kmeans_cluster.center_2[1])
)
plt.scatter(cluster_0[:, 0], cluster_0[:, 1], c="yellow")
plt.scatter(cluster_1[:, 0], cluster_1[:, 1], c="green")
plt.scatter(cluster_2[:, 0], cluster_2[:, 1], c="blue")
plt.scatter(np.array(kmeans_cluster.center_0[0]), np.array(kmeans_cluster.center_0[1]), c="black", marker="*", s=200)
plt.scatter(kmeans_cluster.center_1[0], kmeans_cluster.center_1[1], color="black", marker="*", s=200)
plt.scatter(kmeans_cluster.center_2[0], kmeans_cluster.center_2[1], color="black", marker="*", s=200)
plt.title("Data for Flower CLassification")
plt.xlabel("Petal length")
plt.ylabel("Petal Width")
plt.show()
