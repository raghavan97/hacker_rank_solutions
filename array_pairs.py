#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(arr):
    #print(arr)
    count = 0
    match = 0
    n = len(arr)
    N = n-1
    total_combi = N*(N+1)/2

    max_vals={}

    while count < n:
        i = count
        ai = arr[count]
        j =  count + 1
        max_ij = arr[i]
        expected_min = max_ij/ai
        while j < n:
            # a[i] * a[j] <= max(a[i],a[i+1],.....a[j])
            if arr[j] > max_ij:
                max_ij = arr[j]
                expected_min = max_ij/ai

            if arr[j] <= expected_min:
                match += 1
            #print("comparing arr[i]={} arr[j]={} <= expected_min={} match={}".format(ai, arr[j], expected_min,match))

            j += 1
        count += 1


    #print(match)
    return match


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

