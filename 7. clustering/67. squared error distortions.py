import sys
import math

# Given integers k and m, followed by m centers and a list of points, compute the
# squared error distortion, assuming each point is assigned to the cluster center
# closest to it.
# run `python main.py filepath` where the first line has parameters k and m, the next
# lines have the coordinates of the centers, the following line is a separator,
# and the subsequent lines are coordinates of points.

def main():
    file = open(sys.argv[1], "r")
    params = file.readline().strip().split()
    k, m = (int(params[0]), int(params[1]))
    centers = [[float(x) for x in file.readline().strip().split()] for i in range(k)]
    file.readline()
    points = [[float(x) for x in line.strip().split()] for line in file.readlines()]
    print(str(compute_distortion(centers, points)))

def compute_distortion(centers, points):
    sum_dist = 0.0

    def min_ctr_sqr_dist(pt):
        distances = map(lambda x : squared_dist(pt, x), centers)
        return(min(distances))
    
    for point in points:
        sum_dist += min_ctr_sqr_dist(point)
    return(sum_dist / len(points))


def squared_dist(v, w):
    dist = 0
    for i in range(len(v)):
        dist += (v[i] - w[i]) ** 2
    return(dist)

def argmax(col, key = lambda x : x):
    max = -math.inf
    ind = None
    for i in range(len(col)):
        val = key(col[i])
        if val > max:
            max = val
            ind = i
    return(ind)

if __name__  == "__main__":
    main()