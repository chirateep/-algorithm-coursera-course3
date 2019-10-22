# Uses python3
import sys
import math
import heapq


def distance_two_point(x1, y1, x2, y2):
    dist = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
    return dist


def make_heap(dist):
    heap = list()
    # print(dist)
    for k, v in dist.items():
        heap_key = (v, k)
        heapq.heappush(heap, heap_key)
    return heap


def minimum_distance(x, y):
    result = 0
    # write your code here
    # init value for graph
    adj = [[] for _ in range(len(x))]
    distances = [[] for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j:
                continue
            dist_cost = distance_two_point(x[i], y[i], x[j], y[j])
            adj[i].append(j)
            distances[i].append(dist_cost)

    # print(adj, distances)

    # init value for prim
    costs = dict()
    parent = dict()
    for i, v in enumerate(x):
        costs[i] = float('inf')
        parent[i] = None

    costs[0] = 0
    prio_q = make_heap(costs)
    # print(distances)
    while len(prio_q) > 0:
        v = heapq.heappop(prio_q)
        node_index = v[1]
        for edge, cost in zip(adj[node_index], distances[node_index]):
            if (costs[edge], edge) in prio_q:
                if costs[edge] > cost:
                    # print(edge)
                    heap_index = prio_q.index((costs[edge], edge))
                    costs[edge] = cost
                    parent[edge] = node_index
                    prio_q[heap_index] = (costs[edge], edge)
                    heapq.heapify(prio_q)
        # print(prio_q)
        # print(costs)

    # print(costs)
    # print(parent)
    # edge in prio_q and

    for _, v in costs.items():
        result += v

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
