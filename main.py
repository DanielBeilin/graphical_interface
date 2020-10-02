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

# null object if nearest point not found
NULL = [0, (0,0)]

# finds nearest point to given line from the right
def NearestRightPoint(node, line, best=None):
    if node is not None:
        curr_root = node[2]
        dist = curr_root[0] - line
        if dist > 0:
            if not best:
                best = [dist, curr_root]
            elif dist < best[0]:
                best = [dist, curr_root]
        direction = 0 if curr_root[0] > line else 1
        if node[direction]:
            return NearestRightPoint(node[direction], line, best)
    return best if best else NULL

def main():
    # build tree
    points = [(random.randint(0,100),random.randint(0,100)) for x in range(1000)]
    tree = BuildTree(points)

    # finds nearest
    line = input('enter the line coordinates: ')
    result = NearestRightPoint(tree, int(line))
    print(f'distance: {result[0]} point: {result[1]}')

if __name__ == '__main__':
    main()