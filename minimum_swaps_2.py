#!/bin/python

import math
import os
import random
import re
import sys

def minimumSwaps(arr):

    alen = len(arr)

    no_of_swaps = 0
    incorrect = dict()
    content = dict()

    count = 0
    while count < alen:
        if arr[count] != (count+1):
            incorrect[count+1] = arr[count]
            content[arr[count]] = count+1
        count += 1

    keys = sorted(incorrect.keys())
    for k in keys:
        if incorrect[k] != k:
            #e2_index = get_ind_for(k,content)
            e2_index = content[k]
            tmp = incorrect[k]
            incorrect[k] = k
            incorrect[e2_index] = tmp
            content[tmp] = e2_index
            content[k] = k
            no_of_swaps += 1

    return no_of_swaps

yy=[1, 3, 5, 2, 4, 6, 7]
minimumSwaps(yy)



if __name__ == 'A__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()



