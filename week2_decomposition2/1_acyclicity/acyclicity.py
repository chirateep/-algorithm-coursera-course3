# Uses python3

import sys

visited = list()
pre_visit = list()
post_visit = list()
clock = 1


def acyclic(adj):
    # Init value for graph
    global visited, pre_visit, post_visit
    cycle = 0
    visited = [False] * len(adj)
    pre_visit = [0] * len(adj)
    post_visit = [0] * len(adj)

    # print(adj)
    # Solve
    for i, v in enumerate(adj):
        if len(adj[i]) == 0:
            continue
        else:
            if not visited[i]:
                explore(i, adj)

    # print('pre_visit', pre_visit)
    # print('post_visit', post_visit)

    for i, u in enumerate(post_visit):
        if len(adj[i]) == 0:
            continue
        else:
            for e in adj[i]:
                if u < post_visit[e]:
                    cycle = 1
                    break
            if cycle == 1:
                break

    return cycle


def explore(v, adj):
    global visited, pre_visit, post_visit, clock

    if visited[v]:
        return
    visited[v] = True
    pre_visit[v] = clock
    clock += 1
    for nb in adj[v]:
        if not visited[nb]:
            explore(nb, adj)
    post_visit[v] = clock
    clock += 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
