#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(arr):
    print(arr)
    count = 0
    match = 0
    n = len(arr)
    print(n)
    N = n-1
    count=N
    no_of_tests=0
    while count >= 0:
        i = count
        ai = arr[count]
        j =  count - 1
        if j >= 0:
            max_val = arr[i]
        while j >= 0:
            if arr[j] > max_val:
                max_val = arr[j]
            min_num = max_val/arr[i]

            # there should be atleast one number less than or equal to min_num
            # on the LHS of j , if there is none , we can break
            if j:
                min_lhs = min(arr[0:j])
            '''
            if sarr[0] > min_num:
                #print("{} < {} breaking out".format(min_num, sarr[0]))
                break
            '''
            # a[i] * a[j] <= max(a[i],a[i+1],.....a[j])
            no_of_tests += 1
            mflag = False
            if arr[j]*arr[i] <= max_val:
                match += 1
                mflag = True
            print("trying {},{} max={} min={} min_lhs={} match={}".format(arr[j], ai, max_val, min_num, min_lhs, mflag))
            j -= 1
        count -= 1


    print(no_of_tests)
    print(match)
    return match


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

