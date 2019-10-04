# Uses python3

import sys


def negative_cycle(adj, costs):
    # write your code here
    dist = dict()
    prev = dict()

    for i, node in enumerate(adj):
        dist[i] = 1000000000
        prev[i] = None

    dist[0] = 0
    for _ in range(len(adj) - 1):
        for i, node in enumerate(adj):
            for edge, cost in zip(node, costs[i]):
                if dist[edge] > dist[i] + cost:
                    dist[edge] = dist[i] + cost
                    prev[edge] = i

    for i, node in enumerate(adj):
        for edge, cost in zip(node, costs[i]):
            if dist[edge] > dist[i] + cost:
                return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
