# פולה דיניץ - 206978983
# דניאל ביילין - 207387622

import random
import math

# each node the left side is at points[0] 
# and the right side is at points[1] 
# and the root is at points[2]

dimention = 2

# build tree from given points
def BuildTree(points, i=0):
    if len(points) > 1:
        points.sort(key=lambda point: point[i])
        i = (i + 1) % dimention
        half = len(points) >> 1
        return [
            BuildTree(points[: half], i),
            BuildTree(points[half + 1:], i),
            points[half]
        ]
    elif len(points) == 1:
        return [None, None, points[0]]

# Adds a point to the kd-tree
def add_point(kd_node, point, i=0):
    if kd_node is not None:
        dx = kd_node[2][i] - point[i]
        i = (i + 1) % dimention
        for j, c in ((0, dx >= 0), (1, dx < 0)):
            if c and kd_node[j] is None:
                kd_node[j] = [None, None, point]
            elif c:
                add_point(kd_node[j], point, dimention, i)

# null object if nearest point not found
NULL = [0, (0,0)]

# finds nearest point to given line from the right
def nearest_right_point(kd_node, line, best=None):
    if not kd_node:
        return NULL
    curr_root = kd_node[2]
    dist = curr_root[0] - line

    if dist > 0:
        if not best:
            best = [dist, curr_root]
        elif dist < best[0]:
            best = [dist, curr_root]

    direction = 0 if curr_root[0] > line else 1
    if kd_node[direction]:
        nearest_right_point(kd_node[direction], line, best)
    return best if best else NULL

def main():
    print("start main")

    # build tree
    points = [(random.randint(0,100),random.randint(0,100)) for x in range(1000)]
    tree = BuildTree(points)

    # finds nearest
    line = random.randint(0, 100)
    print('line is: ' + str(line))
    result = nearest_right_point(tree, line)
    print('not found' if result == NULL
    else 'distance: ' + str(result[0]) + ' point: ' + str(result[1]))

if __name__ == '__main__':
    main()