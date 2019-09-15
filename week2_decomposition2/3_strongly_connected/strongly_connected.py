# Uses python3

import sys

sys.setrecursionlimit(200000)

visited = list()
pre_visit = list()
post_visit = list()
sscs = list()
clock = 1


def dfs(adj):
    # write your code here
    # Init value for graph
    global visited, pre_visit, post_visit, sscs
    visited = [False] * len(adj)
    pre_visit = [0] * len(adj)
    post_visit = [0] * len(adj)
    sscs = [0] * len(adj)
    cc = 0

    for i, v in enumerate(adj):
        if len(adj[i]) == 0:
            continue
        else:
            if not visited[i]:
                explore(i, adj, cc)


def explore(v, adj, cc):
    global visited, pre_visit, post_visit, clock, sscs

    if visited[v]:
        return
    visited[v] = True
    sscs[v] = cc
    pre_visit[v] = clock
    clock += 1
    for nb in adj[v]:
        if not visited[nb]:
            explore(nb, adj, cc)
    post_visit[v] = clock
    clock += 1


def toposort():
    global post_visit
    order = []

    dict_index = dict()
    no_post = list()
    for i, u in enumerate(post_visit):
        if u == 0:
            no_post.append(i)
        dict_index[u] = i

    sort_post_visit = post_visit[:]
    sort_post_visit.sort(reverse=True)
    for u in sort_post_visit:
        if u == 0:
            continue
        order.append(dict_index[u])

    order = order + no_post

    return order


def number_of_strongly_connected_components(adj):
    global visited, pre_visit, post_visit, sscs
    result = 0
    # write your code here
    reversed_adj = reversed_graph(adj)
    dfs(reversed_adj)
    reversed_order = toposort()
    # print(pre_visit)
    # print(post_visit)
    # print(reversed_order)

    visited = [False] * len(adj)
    pre_visit = [0] * len(adj)
    post_visit = [0] * len(adj)
    sscs = [0] * len(adj)
    cc = 1

    for v in reversed_order:
        # print('v', v, adj[v])
        if len(adj[v]) == 0:
            visited[v] = True
            cc += 1
        else:
            if not visited[v]:
                explore(v, adj, cc)
                cc += 1
            # print(visited)

    components = dict()
    for i in sscs:
        if i == 0:
            result += 1
            continue

        find_comp = components.get(i, -1)
        if find_comp == -1:
            components[i] = 0
            result += 1
        else:
            components[i] += 1
    # print(sscs)
    return result


def reversed_graph(adj):
    reversed_adj = [[] for _ in range(len(adj))]
    for i, egdes in enumerate(adj):
        for e in egdes:
            reversed_adj[e].append(i)

    return reversed_adj


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
