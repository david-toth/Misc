import numpy as np

def make_clusters(n_obs, n_clusters, means, std_devs):
    """
    Creates a set of n clusters drawn from
    a normal distribution.

    args:
        n_obs (int): number of observations in each cluster
        n_clusters (int): number of clusters to generate
        means (array): means of each cluster
        std_devs (array): standard deviation of clusters

    returns:
        array containing cluster coordinates and corresponding labels

    """
    assert n_obs > 0, "Number of observations should be greater than 0"
    assert n_clusters > 0, "Number of clusters should be at least 1"
    assert len(means) == len(std_devs) == n_clusters, "Size mismatch"
    assert all([i > 0 for i in std_devs]), "Std. dev should be positive"

    labels = []
    clusters = []

    for i in range(n_clusters):
        cluster = np.random.normal(means[i], std_devs[i], (n_obs, 2))
        label = [i]*n_obs

        clusters.append(cluster)
        labels.extend(label)

    labels = np.array(labels).reshape(-1,1)
    
    return np.hstack((np.vstack(clusters), labels))
