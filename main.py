import random

# each node the left side is at points[0] 
# and the right side is at points[1] 
# and the root is at points[2]

dimention = 2

def BuildTree(points, i=0):
    if len(points) > 1:
        points.sort(key=lambda point: point[i])
        i = (i + 1) % dimention
        half = len(points) >> 1
        return [
            BuildTree(points[: half], dimention, i),
            BuildTree(points[half + 1:], dimention, i),
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
# calc distance
def dist_func(a, b, dim=dimention):
    return sum((a[i] - b[i]) ** 2 for i in range(dim))

# For the closest neighbor
def nearest_right_point(kd_node, point, dim=dimention, dist_func=dist_func, return_distances=True, i=0, best=None):
    if kd_node is not None:
        dist = dist_func(point, kd_node[2])
        dx = kd_node[2][i] - point[i]
        if not best:
            best = [dist, kd_node[2]]
        elif dist < best[0]:
            best[0], best[1] = dist, kd_node[2]
        i = (i + 1) % dimention
        # Goes into the left branch, and then the right branch if needed
        for b in [dx < 0] + [dx >= 0] * (dx * dx < best[0]):
            nearest_right_point(kd_node[b], point, dimention, dist_func, return_distances, i, best)
    return best if return_distances else best[1]

    

def main():
    print("start main")
    points = [(random.randint(0,100),random.randint(0,100)) for x in range(1000)]
    tree = BuildTree(points)
    print(nearest_right_point(tree, [0] * dimention))

if __name__ == '__main__':
    main()