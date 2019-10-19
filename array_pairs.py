#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(arr):
    count = 0
    match = 0
    n = len(arr)
    N = n-1
    total_combi = N*(N+1)/2

    while count < n:
        i = count
        ai = arr[count]
        j =  count + 1
        max_dict = {}
        max_ij = arr[i]
        combi = 0
        while j < n:
            aj = arr[j]
            prod = ai * aj
            max_ij = max(max_ij, arr[j])
            if prod <= max_ij:
                match += 1
            j += 1
        count += 1


    return match


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

