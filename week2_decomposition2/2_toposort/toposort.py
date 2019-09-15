# Uses python3

import sys

visited = list()
pre_visit = list()
post_visit = list()
clock = 1


def dfs(adj):
    # write your code here
    # Init value for graph
    global visited, pre_visit, post_visit
    visited = [False] * len(adj)
    pre_visit = [0] * len(adj)
    post_visit = [0] * len(adj)

    for i, v in enumerate(adj):
        if len(adj[i]) == 0:
            continue
        else:
            if not visited[i]:
                explore(i, adj)

    # print('pre_visit', pre_visit)
    # print('post_visit', post_visit)


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


def toposort(adj):
    global post_visit
    order = []
    # write your code here
    dfs(adj)

    dict_index = dict()
    no_post = list()
    for i, u in enumerate(post_visit):
        if u == 0:
            no_post.append(i)
        dict_index[u] = i

    # print(post_visit)
    sort_post_visit = post_visit[:]
    sort_post_visit.sort(reverse=True)
    # print(sort_post_visit)
    for u in sort_post_visit:
        if u == 0:
            continue
        order.append(dict_index[u])

    order = order + no_post
    # print(order)

    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
