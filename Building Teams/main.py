import sys
import collections as clc

def input():
    return sys.stdin.readline().strip()

def inp_list():
    return map(int, input().split())

def main():
    global side
    n, m = inp_list()
    side = [None for _ in range(n)]
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = inp_list()
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    for i in range(n):
        if side[i] is None:
            side[i] = 1
            if dfs(graph, i) == -1:
                print("IMPOSSIBLE")
                return

    for e in side:
        print(e, end=" ")
    print()

side = []

def dfs(g, n):
    s = clc.deque()
    push = s.append
    pop = s.popleft

    push(n)
    while s:
        cur = pop()

        for ch in g[cur]:
            if side[ch] is None:
                side[ch] = 2 if side[cur] == 1 else 1
                push(ch)
            else:
                if side[ch] == side[cur]:
                    return -1
    return 0

main()
