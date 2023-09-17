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
    n, m, k = inp_map(int)
    a = sorted(inp_list(int))
    b = sorted(inp_list(int))

    u = 0
    d = 0
    c = 0
    while u < n and d < m:
        if b[d] >= (a[u] - k) and b[d] <= (a[u] + k):
            c += 1
            u += 1
            d += 1
        elif b[d] < a[u]:
            d += 1
        elif b[d] > a[u]:
            u += 1
    print(c)

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