# פולה דיניץ - 206978983
# דניאל ביילין - 207387622

import random
import math

# each node the left side is at points[0] 
# and the right side is at points[1] 
# and the root is at points[2]

    
def add_point(tree, point):
        if point[0] < tree[2][0]:
            if tree[0] is None:
                tree[0] = [None,None,point]
            else:
                add_point(tree[0], point)
        else:
            if tree[1] is None:
                tree[1] = [None,None,point]
            else:
                add_point(tree[1], point)

# build tree from given points
def BuildTree():
    tree = [None,None,(random.uniform(0,100),random.uniform(0,100))]
    for i in range(1000):
        point=(random.uniform(0,100),random.uniform(0,100))
        add_point(tree,point)
    return tree

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
    tree = BuildTree()
    # finds nearest
    line = input('enter the line coordinates: ')
    result = NearestRightPoint(tree, float(line))
    print(f'distance: {result[0]} point: {result[1]}')

if __name__ == '__main__':
    main()