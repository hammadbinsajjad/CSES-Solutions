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
    n = inp_int()
    a = inp_list(int)

    l = 0
    cnt = {}
    res = 0

    for r in range(n):
        debug(cnt)
        while cnt.get(a[r], 0) >= 1:
            cnt[a[l]] -= 1
            l += 1
        cnt[a[r]] = cnt.get(a[r], 0) + 1
        res = max(res, r - l + 1)

    print(res)


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