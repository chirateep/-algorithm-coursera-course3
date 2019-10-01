# Uses python3

import sys
from collections import deque


def distance(adj, s, t):
    # write your code here

    # init value
    queue = deque()
    dist = dict()
    for i, v in enumerate(adj):
        dist[i] = float('inf')
    dist[s] = 0

    # print(adj)
    queue.append(s)
    while len(queue) > 0:
        u = queue.popleft()

        for e in adj[u]:
            # print(u, e)
            if dist[e] == float('inf'):
                queue.append(e)
                dist[e] = dist[u] + 1

    if dist[t] == float('inf'):
        return -1

    return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
