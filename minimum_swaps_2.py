#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    alen = len(arr)
    print(arr)

    i = 0
    anchor = 0
    no_of_swaps = 0
    min_found_index = anchor

    min_found = arr[anchor]

    while anchor < alen:
        if i >= alen:
            if min_found_index != anchor:
                tmp = arr[min_found_index]
                arr[min_found_index] = arr[anchor]
                arr[anchor] = tmp
                no_of_swaps += 1
                print("from:{} to {}".format(min_found_index, anchor))
                print("{}".format(arr))
            anchor += 1
            i = anchor
            if anchor < alen:
                min_found = arr[anchor]
            continue

        if arr[i] < min_found:
            tmp = arr[i]
            min_found = tmp
            min_found_index = i

        i += 1

    print(arr)
    return no_of_swaps






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()


