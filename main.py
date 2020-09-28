import random

# each node the left side is at points[0] 
# and the right side is at points[1] 
# and the root is at points[2]
# https://github.com/Vectorized/Python-KD-Tree/blob/master/kdtree.py Pola look at this, could help 

DIMINTIONS = 2

def BuildTree(points, dim, i=0):
    if len(points) > 1:
        points.sort(key=lambda point: point[i])
        i = (i + 1) % dim
        half = len(points) >> 1
        return [
            BuildTree(points[: half], dim, i),
            BuildTree(points[half + 1:], dim, i),
            points[half]
        ]
    elif len(points) == 1:
        return [None, None, points[0]]

# Adds a point to the kd-tree
def add_point(kd_node, point, dim, i=0):
    if kd_node is not None:
        dx = kd_node[2][i] - point[i]
        i = (i + 1) % dim
        for j, c in ((0, dx >= 0), (1, dx < 0)):
            if c and kd_node[j] is None:
                kd_node[j] = [None, None, point]
            elif c:
                add_point(kd_node[j], point, dim, i)

def main():
    print("start main")
    points = [(random.randint(0,100),random.randint(0,100)) for x in range(1000)]
    tree = BuildTree(points,DIMINTIONS)

if __name__ == '__main__':
    main()