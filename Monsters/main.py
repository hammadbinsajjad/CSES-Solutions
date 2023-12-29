import sys
from collections import deque
from math import inf

def input():
    return sys.stdin.readline().strip()

def inp_map(f):
    return map(f, input().split())

def debug(*x, sep=" ", end="\n"):
    for e in x:
        sys.stderr.write(str(e))
        sys.stderr.write(sep)
    sys.stderr.write(end)

def print(x, end="\n"):
    w = sys.stdout.write
    w(str(x))
    w(end)


dist = None
p = None
def main():
    global dist, p
    n, m = inp_map(int)

    graph = [list(input()) for _ in range(n)]
    dist = [[inf] * m for _ in range(n)]
    p = [[(0, 0)] * m for _ in range(n)]
    monsters = []

    for i, row in enumerate(graph):
        for j, e in enumerate(row):
            if e == 'M':
                #bfsm(graph, (i, j))
                monsters.append(((i, j), 0))
            if e == 'A':
                p[i][j] = None
                hx, hy = i, j

    bfsm(graph, monsters)

    res = bfs(graph, (hx, hy))
    if res == None:
        print("NO")
        return
    x, y = res
    path = []
    parent = p[x][y]


    while parent != None:
        path.append(parent[2])
        parent = p[parent[0]][parent[1]]

    print("YES")
    print(len(path))
    for e in reversed(path):
        print(e, end="")



def bfs(g, s):
    global dist, p
    q = deque()
    push = q.append
    pop = q.popleft

    push((s, 0))
    dist[s[0]][s[1]] = 0

    def inb(x, y):
        if 0 <= x < len(g) and 0 <= y < len(g[0]):
            return True
        else:
            return False

    while q:
        (x, y), d = pop()

        if x == 0 or x == len(g) - 1 or y == 0 or y == len(g[0]) - 1:
            return (x, y)

        for i in (1, -1):
            if inb(x, y + i) and dist[x][y + i] > d + 1 and g[x][y + i] != '#' and p[x][y + i] == (0, 0):
                p[x][y + i] = (x, y, 'R' if i == 1 else 'L')
                push(((x, y + i), d + 1))
            if inb(x + i, y) and dist[x + i][y] > d + 1 and g[x + i][y] != '#' and p[x + i][y] == (0, 0):
                p[x + i][y] = (x, y, 'D' if i == 1 else 'U')
                push(((x + i, y), d + 1))

def bfsm(g, mons):
    global dist, p
    q = deque(mons)

    push = q.append
    pop = q.popleft

    for (x, y), d in mons:
        dist[x][y] = 0



    def inb(x, y):
        if 0 <= x < len(g) and 0 <= y < len(g[0]):
            return True
        else:
            return False

    while q:
        (x, y), d = pop()

        for i in (1, -1):
            if inb(x, y + i) and dist[x][y + i] > dist[x][y] + 1 and g[x][y + i] != '#':
                dist[x][y + i] = dist[x][y] + 1
                push(((x, y + i), d + 1))
            if inb(x + i, y) and dist[x + i][y] > dist[x][y] + 1 and g[x + i][y] != '#':
                dist[x + i][y] = dist[x][y] + 1
                push(((x + i, y), d + 1))


main()
