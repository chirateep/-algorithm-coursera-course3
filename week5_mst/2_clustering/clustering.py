# Uses python3

import sys
import math

from collections import namedtuple
from operator import attrgetter


Edge = namedtuple('Point', ['x', 'y', 'dist'])


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        if self.ranks[src_parent] > self.ranks[dst_parent]:
            self.row_counts[src_parent] += self.row_counts[dst_parent]
            self.row_counts[dst_parent] = 0
            if self.row_counts[src_parent] > self.max_row_count:
                self.max_row_count = self.row_counts[src_parent]
            self.parents[dst_parent] = src_parent
        else:
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            self.row_counts[src_parent] = 0
            if self.row_counts[dst_parent] > self.max_row_count:
                self.max_row_count = self.row_counts[dst_parent]
            self.parents[src_parent] = dst_parent
            if self.ranks[src_parent] == self.ranks[dst_parent]:
                self.ranks[dst_parent] += 1
        return True

    def get_parent(self, table):
        # find parent and compress path
        if table != self.parents[table]:
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]


def distance_two_point(x1, y1, x2, y2):
    dist = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
    return dist


def clustering(x, y, k):
    # write your code here

    # init value of disjoint set
    counts = [1] * len(x)
    disjoint_set = Database(counts)
    list_edge = list()

    # init value for graph
    edges = list()
    for i in range(len(x)):
        for j in range(i, len(x)):
            if i == j:
                continue
            dist_cost = distance_two_point(x[i], y[i], x[j], y[j])
            edge = Edge(i, j, dist_cost)
            edges.append(edge)

    edges = sorted(edges, key=attrgetter('dist'))

    for edge in edges:
        if disjoint_set.get_parent(edge.x) != disjoint_set.get_parent(edge.y):
            list_edge.append(edge)
            disjoint_set.merge(edge.x, edge.y)

    # print(list_edge)
    return list_edge[len(list_edge) - k + 1].dist


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
