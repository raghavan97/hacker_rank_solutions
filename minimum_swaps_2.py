#!/bin/python

import math
import os
import random
import re
import sys

def dprint(msg):
    pass
    print(msg)

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    alen = len(arr)
    dprint(arr)

    i = 0
    anchor = 0
    no_of_swaps = 0
    min_found_index = anchor

    min_found = arr[anchor]

    while anchor < alen:
        if arr[i] < arr[anchor]:
            dprint("swapping {} to {}".format(arr[i], arr[anchor]))
            tmp = arr[i]
            arr[i] = arr[anchor]
            arr[anchor] = tmp
            no_of_swaps += 1
            dprint(arr)

        i += 1

        if i == alen:
            anchor += 1
            i = anchor
            dprint("----------------")

    dprint(arr)
    return no_of_swaps






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()


