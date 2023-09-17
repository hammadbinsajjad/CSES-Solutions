import sys
import math
import bisect as bs
import string as strn
import heapq as hq
import collections as clc
import itertools as it
import operator as op
import copy as cp

to_debug = True
def solve():
    n, x = inp_map(int)
    a = inp_list(int)

    m = [[]] * n
    for i, e in enumerate(a):
        m[i] = (e, i)
    m.sort(key=op.itemgetter(0))
    
    l  = 0
    r = n - 1

    while l < r:
        s = m[l][0] + m[r][0]
        if s < x:
            l += 1
        elif s > x:
            r -= 1
        else:
            print(m[l][1] + 1, end=" ")
            print(m[r][1] + 1)
            return

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