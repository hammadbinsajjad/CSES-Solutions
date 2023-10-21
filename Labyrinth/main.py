import collections as clc

import sys

def input():
    return sys.stdin.readline().strip()

def inp_list(f=None):
    return list(map(f, input().split())) if f else list(input())

def main():
    n, m = inp_list(int)
    graph = [[] for _ in range(n)]


    start, end = None, None
    for i in range(n):
        row = inp_list()
        graph[i] = row

        if 'A' in row:
            start = (i, row.index('A'))
        if 'B' in row:
            end = (i, row.index('B'))

    p = [[-1] * n for _ in range(n)]

    res = bfs(graph, start)

    if not res:
        print("NO")
    else:
        print("YES")



def bfs(g, n):
    q = clc.deque()
    push = q.append
    pop = q.popleft

    push(n)

    while q:
        cur = pop()
        x, y = cur

        inBounds = lambda x, n: 0 <= x < n

        if not inBounds(x, len(g)) or not inBounds(y, len(g[0])) or g[x][y] == '#':
            continue

        if g[x][y] == 'B':
            return cur

        g[x][y] = "#"

        for i in (1, -1):
            if inBounds(x + i, len(g) and inBounds(y, len(g[0])):
                p[x + i][j] = cur
            if inBounds(x, len(g) and inBounds(y + i, len(g[0]):
                p[x][j + i] = cur
            bfs(g, (x + i, j))
            bfs(g, (x, j + i))

    return None

main()
