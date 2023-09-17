import sys
import math
import bisect as bs
import string as strn
import heapq as hq
import collections as clc
import itertools as it
import operator as op
import copy as cp

to_debug = False
def solve():
    n, x = inp_map(int)
    p = sorted(inp_list(int))
    debug(p)

    c = 0
    s = 0
    l = 0
    r = n - 1

    while l <= r:
        s = p[l] + p[r]
        debug(p[l], p[r], s, c)

        if l == r:
            c += 1
            break

        if s <= x:
            c += 1
            r -= 1
            l += 1
        else:
            c += 1
            r -= 1
        s = 0
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