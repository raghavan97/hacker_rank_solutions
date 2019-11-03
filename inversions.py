import math
import os
import random
import re
import sys
import bisect

# https://www.hackerrank.com/challenges/ctci-merge-sort/problem

# Complete the countInversions function below.
def countInversions(arr):
    s = [arr[0]]
    c = 1
    n = len(arr)
    pairs = 0
    while c < n:
        # find the highest value in the list which is < arr[c]
        # if it is not the highest , then all the ones above it are
        # inversions
        pos = bisect.bisect_right(s,arr[c])
        pairs += (len(s) - pos)

        # add element to the sorted list
        s.insert(pos,arr[c])
        c += 1
    print(pairs)
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        arr = map(int, raw_input().rstrip().split())

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
