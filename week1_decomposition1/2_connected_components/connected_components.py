# Uses python3

import sys

visited = list()
Ccum = list()


def number_of_components(adj):
    # write your code here
    global visited
    global Ccum

    visited = [False] * len(adj)
    Ccum = [0] * len(adj)
    cc = 1

    for i, v in enumerate(adj):
        if len(adj[i]) == 0:
            continue
        else:
            if not visited[i]:
                explore(i, adj, cc)
                cc += 1

    result = 0
    components = dict()
    for i in Ccum:
        if i == 0:
            result += 1
            continue

        find_comp = components.get(i, -1)
        if find_comp == -1:
            components[i] = 0
            result += 1
        else:
            components[i] += 1
    return result


def explore(v, adj, cc):
    global visited
    global Ccum
    if visited[v]:
        return
    visited[v] = True
    Ccum[v] = cc
    for nb in adj[v]:
        if not visited[nb]:
            explore(nb, adj, cc)


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
    print(number_of_components(adj))
