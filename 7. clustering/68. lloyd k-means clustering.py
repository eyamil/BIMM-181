import sys
import math

# Given a list of points and an integer k, run k-means clustering using the lloyd algorithm.
# run `python main.py filepath` where the file's first line has integers k, m, and the
# subsequent lines are the points.
# run `python main.py filepath` where the file's first line has the parameter k and 
# the dimension of the space they are embedded in, and subsequent lines are coordinates
# for each point.

def main():
    file = open(sys.argv[1], "r")
    params = file.readline().strip().split()
    k, m = (int(params[0]), int(params[1]))
    points = [[float(x) for x in line.strip().split()] for line in file.readlines()]
    centroids = lloyd_kmeans(points, points[0:k], squared_dist, cluster_to_mean)
    print("\n".join([" ".join([str(coord) for coord in point]) for point in centroids]))

def lloyd_kmeans(points, init_centroids, dist_fn, centroid_fn):
    centroids = init_centroids
    prev_clustering = []
    curr_clustering = assign_points(points, centroids, dist_fn)
    while curr_clustering != prev_clustering:
        prev_clustering = curr_clustering
        centroids = compute_centroids(points, curr_clustering, centroid_fn)
        curr_clustering = assign_points(points, centroids, dist_fn)
    return(centroids)

def assign_points(points, centroids, distance_fn):
    cluster_assignment = [set() for i in range(len(centroids))]

    def closest_ctr(pt):
        distances = list(map(lambda x : distance_fn(x, pt), centroids))
        return(argmin(distances))

    for i in range(len(points)):
        point = points[i]
        cluster_assignment[closest_ctr(point)].add(i)
    return(cluster_assignment)

def compute_centroids(points, cluster_assignment, centroid_function):
    centroids = []
    for cluster in cluster_assignment:
        centroids.append(centroid_function(points, cluster))
    return(centroids)

def cluster_to_mean(points, cluster):
    mean = [0.0 for i in points[next(iter(cluster))]]
    n = 0
    for i in cluster:
        point = points[i]
        n += 1
        for i in range(len(mean)):
            mean[i] += point[i]
    for i in range(len(mean)):
        mean[i] = mean[i] / n
    return(mean)

def squared_dist(v, w):
    dist = 0
    for i in range(len(v)):
        dist += (v[i] - w[i]) ** 2
    return(dist)

def argmin(col, key = lambda x : x):
    min = math.inf
    ind = None
    for i in range(len(col)):
        val = key(col[i])
        if val < min:
            min = val
            ind = i
    return(ind)

if __name__  == "__main__":
    main()