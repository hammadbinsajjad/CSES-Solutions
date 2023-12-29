import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

dist = None

def bfs(g, s):
    global dist
    q = deque()

    for i in range(len(dist)):
        dist[i] = -1

    push = q.append
    pop = q.popleft

    push((s, 0))
    dist[s] = 0

    last_node = s

    while q:
        c, d = pop()

        for ch in g[c]:
            if dist[ch] == -1:
                push((ch, d + 1))
                dist[ch] = d + 1

                last_node = ch

    return last_node

def main():
    global dist
    n = int(input())

    graph = [[] for _ in range(n)]

    dist = [-1] * n

    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    last_node = bfs(graph, 0)
    last_node = bfs(graph, last_node)
    print(dist[last_node])

main()
