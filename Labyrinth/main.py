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

    parent = [[-1] * m for _ in range(n)]

    res = bfs(graph, start, parent)

    if not res:
        print("NO")
    else:
        print("YES")
        path = []
        x, y = res
        cur = parent[x][y]
        while cur != -1:
            path.append(cur[1])
            x, y = cur[0]
            cur = parent[x][y]
        path.reverse()
        print(len(path))
        print("".join(c for c in path))



def bfs(g, n, p):
    q = clc.deque()
    push = q.append
    pop = q.popleft


    push(n)

    while q:
        cur = pop()
        x, y = cur

        inBounds = lambda x, y, g: 0 <= x < len(g) and 0 <= y < len(g[0])

        if not inBounds(x, y, g) or g[x][y] == '#':
            continue

        if g[x][y] == 'B':
            return cur

        g[x][y] = "#"

        if inBounds(x + 1, y, g) and g[x + 1][y] != '#':
            push((x + 1, y))
            p[x + 1][y] = (cur, "D")
        if inBounds(x - 1, y, g)  and g[x - 1][y] != '#':
            push((x - 1, y))
            p[x - 1][y] = (cur, "U")
        if inBounds(x, y + 1, g) and g[x][y + 1] != '#':
            push((x, y + 1))
            p[x][y + 1] = (cur, "R")
        if inBounds(x, y - 1, g) and g[x][y - 1] != '#':
            push((x, y - 1))
            p[x][y - 1] = (cur, "L")

    return None

main()
