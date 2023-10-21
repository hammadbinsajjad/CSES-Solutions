 
import sys
# import math
# import bisect as bs
# import string as strn
# import heapq as hq
import collections as clc
# import itertools as it
# import operator as op
# import copy as cp

to_debug = True
def solve():
    n, m = inp_map(int)

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = inp_map(int)

        graph[a].append(b)
        graph[b].append(a)


    q = clc.deque()
    p = []
    q.append((1, p))
    v = set()
    found = False

    while q:
        c, p = q.popleft()
        # debug(q, c, p)

        if c in v:
            continue

        v.add(c)

        if c == n:
            found = True
            break

        for l in graph[c]:
            if l not in v:
                q.append((l, p + [c]))

    if found:
        print(len(p) + 1)
        for e in p:
            print(e, end=" ")
        print(n)
    else:
        print("IMPOSSIBLE")

def main():
    t = 1
    for _ in range(t):
        solve()

def input():
    return sys.stdin.readline().strip('\r\n')

def inp_int():
    return int(input())

def inp_map(f=None):
    return map(f, input().split()) if f else map(int, input().split())

def inp_list(f=None):
    return list(map(f, input().split())) if f else list(input())

def print(x='', end='\n'):
    sys.stdout.write(str(x))
    sys.stdout.write(end)

def debug(*x, end='\n', sep=' '):
    if not to_debug:
        return
    for _x in x:
        sys.stderr.write(str(_x))
        sys.stderr.write(str(sep))
    sys.stderr.write(end)

main()
