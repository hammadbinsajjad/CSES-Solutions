import collections as clc
import sys

def inp_list(f=None):
    return list(map(f, input().strip().split())) if f else list(input().strip())

def main():
    n, m = inp_list(int)
    graph = [[] for _ in range(n)]

    for i in range(n):
        row = inp_list()
        graph[i] = row
    res = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '.':
                res += 1
                bfs(graph, (i,j))

    print(res)

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

        g[x][y] = "#"

        for i in (1, -1):
            push((x + i, y))
        for j in (1, -1):
            push((x, y + j))



main()
