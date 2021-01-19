import sys
import math

# Perform a farthest first traversal to establish cluster centers for the first
# iteration of a k-means algorithm.
# run `python main.py filepath` where the file's first line has the number of points and 
# the dimension of the space they are embedded in, and subsequent lines are coordinates
# for each point.	

def main():
    file = open(sys.argv[1], "r")
    params = file.readline().strip().split()
    k = int(params[0])
    points = [[float(x) for x in line.strip().split()] for line in file.readlines()]
    centers = farthest_first_clustering(points, k)
    print("\n".join([" ".join([str(x) for x in pt]) for pt in centers]))

def farthest_first_clustering(data, k):
    centers = [data[0]]
    while len(centers) < k:
        centers.append(furthest_pt(data, centers))
    return(centers)

def furthest_pt(data, centers):

    def min_ctr_distance(pt):
        distances = map(lambda x : distance(x, pt), centers)
        return(min(distances))
    
    return(data[argmax(data, min_ctr_distance)])
    

def distance(v, w):
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