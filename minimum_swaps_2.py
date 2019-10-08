#!/bin/python

import math
import os
import random
import re
import sys

# The brunt of the work is done by the 2 DS
# reverse and incorrect

# incorrect is a dictionary that stores all the incorrectly placed
# entries. It would not store the correctly placed entries 
# for an input of [1, 3, 5, 2, 4, 6, 7]
# incorrect would be { 2:3, 3:5, 4:2, 5:4 }
# incorrect would not have entries with keys for 1,6 and 7 since they
# are in the respective places and DONT need a swap

# reverse is a dictionary that stores the index where a particular
# element is stored. For example reverse[3] would tell us at what index
# 3 is stored
# for an input of [1, 3, 5, 2, 4, 6, 7]
# reverse would be { 3:2, 5:3, 2:4, 4:5 }
# Again reverse would only contain the entries that are incorrectly placed
# there would be no "values" 1,6,7

# The swaps would take place while we are traversing the array
# The array keeps getting "corrected" as the traversal progresses
# Hence, It is gauranteed to be minimum number of swaps

def minimumSwaps(arr):

    alen = len(arr)

    no_of_swaps = 0
    incorrect = dict()
    reverse = dict()

    count = 0
    while count < alen:
        if arr[count] != (count+1):
            incorrect[count+1] = arr[count]
            reverse[arr[count]] = count+1
        count += 1

    keys = sorted(incorrect.keys())
    for k in keys:
        if incorrect[k] != k:

            # where is k ?
            k_index = reverse[k]

            # swap them
            tmp = incorrect[k]
            incorrect[k] = k
            incorrect[k_index] = tmp

            # update reverse
            reverse[tmp] = k_index
            reverse[k] = k

            no_of_swaps += 1

    return no_of_swaps

# Try tracing it by uncommenting the following lines
#yy=[1, 3, 5, 2, 4, 6, 7]
#minimumSwaps(yy)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()



