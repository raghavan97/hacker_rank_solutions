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

# The curr_posn is the array that contains the current position


# Complete the minimumBribes function below.
def minimumBribes(q):
    qlen = len(q)
    curr_posn = range(1,qlen+1)

    no_of_bribes = 0

    count = 0
    while count < qlen:

        # is the person is in the right place?
        if q[count] == curr_posn[count]:
            count += 1
            continue

        # unless we have one person in the right, we cant attempt to fix it
        if count+1 >= qlen:
            print("Too chaotic")
            return

        # The one to the right is the correct one, do a bribe
        if curr_posn[count+1] == q[count]:
            tmp = curr_posn[count]
            tmp1 = curr_posn[count+1]
            curr_posn[count] = tmp1
            curr_posn[count+1] = tmp
            no_of_bribes += 1
            continue

        # the one in right did not match, check the next one in the right
        if count+2 >= qlen:
            print("Too chaotic")
            return

        # the one next to the right matches, we need to bribe twice to get
        # him to the correct position
        if curr_posn[count+2] == q[count]:
            tmp = curr_posn[count]
            tmp1 = curr_posn[count+1]
            tmp2 = curr_posn[count+2]
            curr_posn[count] = tmp2
            curr_posn[count+1] = tmp
            curr_posn[count+2] = tmp1
            no_of_bribes += 2
        else:
            print("Too chaotic")
            return

    print(no_of_bribes)


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)

