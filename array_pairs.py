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

    while count < n:
        i = count
        ai = arr[count]
        j =  count + 1
        max_dict = {}
        max_dict[(i,i)] = arr[i]
        while j < n:
            aj = arr[j]
            prod = ai * aj
            max_ij = max(max_dict[(i,j-1)], arr[j])
            max_dict[(i,j)] = max_ij
            if prod <= max_ij:
                match += 1
            j += 1
        count += 1

    N = n-1
    return match


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

