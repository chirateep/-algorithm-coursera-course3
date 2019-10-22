# Uses python3

import sys
import heapq

visited = list()


def distance(adj, costs, s, t):
    # write your code here
    global visited
    visited = [False] * len(adj)
    dist = dict()
    prev = dict()
    for i, v in enumerate(adj):
        dist[i] = float('inf')
        prev[i] = None

    dist[s] = 0
    heap = make_heap(dist)
    while len(heap) > 0:
        u = heapq.heappop(heap)
        node_index = u[1]
        for edge, cost in zip(adj[node_index], costs[node_index]):
            if dist[edge] > dist[node_index] + cost:
                heap_index = heap.index((dist[edge], edge))
                # print(heap_index, heap)
                dist[edge] = dist[node_index] + cost
                prev[edge] = node_index
                heap[heap_index] = (dist[edge], edge)
                heapq.heapify(heap)

    if dist[t] == float('inf'):
        return -1
    else:
        return dist[t]


def make_heap(dist):
    heap = list()
    for k, v in dist.items():
        heap_key = (v, k)
        heapq.heappush(heap, heap_key)
    return heap


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]),
                     data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
