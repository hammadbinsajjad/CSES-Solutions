import sys
import math
import heapq as hq

def input():
    return sys.stdin.readline()

def inp_list(f=None):
    return list(map(f, input().split())) if f else list(input())

def main():
    n, m = inp_list(int)
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b, w = inp_list(int)
        graph[a - 1].append((b - 1, w))

    dijkstra(graph)

def dijkstra(g):
    n = len(g)
    dist = [math.inf] * n
    dist[0] = 0

    pq = []
    push = lambda x: hq.heappush(pq, x)
    pop = lambda: hq.heappop(pq)

    push((0, 0))
    while pq:
        cd, c = pop()

        if cd != dist[c]:
            continue

        for ch, cw in g[c]:
            if dist[ch] > cw + dist[c]:
                dist[ch] = cw + dist[c]
                push((dist[ch], ch))

    for d in dist:
        print(d, end=" ")
    print()


main()
