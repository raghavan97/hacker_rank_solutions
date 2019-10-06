#!/bin/python

import math
import os
import random
import re
import sys
import heapq
import copy
from pprint import pprint

# https://www.hackerrank.com/challenges/new-year-chaos/problem




# Complete the minimumBribes function below.
def minimumBribes(q):
    qlen = len(q)
    start_posn = range(1,qlen+1)

    no_of_swaps = 0

    count = 0
    while count < qlen:
        if q[count] == start_posn[count]:
            count += 1
            continue

        if count+1 >= qlen:
            print("Too chaotic")
            return

        if start_posn[count+1] == q[count]:
            tmp = start_posn[count]
            tmp1 = start_posn[count+1]
            start_posn[count] = tmp1
            start_posn[count+1] = tmp
            no_of_swaps += 1
            continue

        if count+2 >= qlen:
            print("Too chaotic")
            return

        if start_posn[count+2] == q[count]:
            tmp = start_posn[count]
            tmp1 = start_posn[count+1]
            tmp2 = start_posn[count+2]
            start_posn[count] = tmp2
            start_posn[count+1] = tmp
            start_posn[count+2] = tmp1
            no_of_swaps += 2

        else:
            print("Too chaotic")
            return

    print(no_of_swaps)


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)

