# Uses python3

import sys
from collections import deque

visited = list()


def bipartite(adj):
    # write your code here
    # init value
    global visited
    visited = [False] * len(adj)
    queue = deque()
    dist = dict()
    for i, v in enumerate(adj):
        dist[i] = float('inf')

    # print(adj)
    for i, v in enumerate(adj):
        if len(adj[i]) == 0:
            continue
        else:
            if not visited[i]:
                dist[i] = 0
                queue.append(i)
                while len(queue) > 0:
                    u = queue.popleft()
                    visited[u] = True
                    for e in adj[u]:
                        # print(u, e)
                        if dist[e] == float('inf'):
                            queue.append(e)
                            dist[e] = dist[u] + 1

    for i, edges in enumerate(adj):
        for e in edges:
            distance = dist[i]
            if distance == dist[e]:
                return 0

    return 1


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
    print(bipartite(adj))
