# Uses python3

import sys

visited = list()
Ccum = list()


def reach(adj, x, y):
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
        # print(visited)
    # print('ans', visited[y])
    # print(Ccum)
    # print(Ccum[x], Ccum[y])
    if Ccum[x] == Ccum[y]:
        return 1
    else:
        return 0


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
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
