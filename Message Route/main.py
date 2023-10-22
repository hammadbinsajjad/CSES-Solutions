import sys
import collections as clc

to_debug = False
def solve():
    n, m = inp_map(int)

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = inp_map(int)
        graph[a].append(b)
        graph[b].append(a)


    q = clc.deque()
    p = [-1 for _ in range(n + 1)]
    q.append(1)
    v = set([1])
    found = False

    while q:
        c = q.popleft()

        if c == n:
            found = True
            break

        for l in graph[c]:
            if l not in v:
                p[l] = c
                q.append(l)
                v.add(l)

    if found:
        debug(p)
        path = []
        cur = p[-1]
        while cur != -1:
            path.append(cur)
            cur = p[cur]
        path.reverse()
        print(len(path) + 1)
        print(" ".join(str(i) for i in path) + " " + str(n))

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
