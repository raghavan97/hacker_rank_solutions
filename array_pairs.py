#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(arr):
    #print(arr)
    #print("-----------")

    count = 0
    combi = 0
    match = 0
    n = len(arr)

    while count < n:
        i = count
        ai = arr[count]
        j =  count + 1
        while j < n:
            aj = arr[j]
            prod = ai * aj
            max_ij = max(arr[i:j+1])
            # print("{},{} prod={} max={}".format(i+1,j+1,prod,max_ij))
            if prod <= max_ij:
                # print(i+1,j+1)
                match += 1
            j += 1
            combi += 1
        count += 1

    N = n-1
    # assert combi == (N*(N+1))/2
    # print(match)
    return match


solve([1, 1, 2, 4, 2])

if __name__ == 'b__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

