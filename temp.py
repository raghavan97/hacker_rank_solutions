#!/bin/python

import math
import os
import random
import re
import sys
import bisect

def check_matches_lt(min_num, j, all_elem, keys, prev_ind, rt):
    i = bisect.bisect_right(keys, min_num)
    if not i:
        return 0
    count = i
    match = 0
    while count >= 0:
        (val, ind) = all_elem[count]
        print("trying {},{} ind={} min={}".format(val,rt, ind,min_num))
        if val <= min_num and ind <= j:
            match += 1
        count -= 1
    return match

# Complete the solve function below.
def solve(arr):
    print(arr)
    count = 0
    match = 0
    n = len(arr)
    print(n)
    N = n-1
    count=N
    all_elem = []
    count = 0
    while count < n:
        all_elem.append((arr[count],count))
        count += 1
    all_elem.sort(key=lambda r: r[0])
    keys = [r[0] for r in all_elem]
    print(all_elem)
    print(keys)

    no_of_tests=0
    count=N
    while count >= 0:
        i = count
        ai = arr[count]
        j =  count - 1
        if j >= 0:
            max_val = -1
            prev_ind = -1
            max_ind = -1
        while j >= 0:
            if arr[j] > max_val:
                max_val = arr[j]
                prev_ind = max_ind
                max_ind = j
            min_num = max_val/arr[i]

            mats = check_matches_lt(min_num, j, all_elem, keys, prev_ind, arr[j])

            # there should be atleast one number less than or equal to min_num
            # on the LHS of j , if there is none , we can break
            match += mats

            j -= 1
        count -= 1


    print(no_of_tests)
    print(match)
    return match

solve([1, 1, 2, 4, 2])
sys.exit(0)

if __name__ == 's__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

