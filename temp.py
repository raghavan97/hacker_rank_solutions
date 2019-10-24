#!/bin/python

import math
import os
import random
import re
import sys

class ArrayPairs(object):
    def __init__(self, arr):
        self.arr = arr

    def compute_supp_DS(self):
        max_vals={}
        count = 0
        elem_values = {}
        max_v = arr[count]
        max_vals[count] = max_v
        while count < n:
            elem = arr[count]
            if elem > max_v:
                max_v = elem
                max_vals[count] = max_v

            if elem in elem_values:
                elem_values[elem].append(elem)
            else:
                elem_values[elem] = [count]
            count += 1
        self.max_vals = max_vals
        self.elem_values = elem_values

        self.sorted_elem_list = sorted(elem_values.keys())
        self.sorted_max_vals_list = sorted(max_vals.keys())

    def get_max_val(self, ind):
        i = bisect_right(self.sorted_max_vals_list, ind)
        return self.max_vals[i]

    def find_matches(self, cur_ind):
        curr_val = self.arr[cur_ind]
        max_val = self.get_max_val(cur_ind)
        expected_min = 

# Complete the solve function below.
def solve(arr):
    print(arr)
    count = 0
    match = 0
    n = len(arr)
    N = n-1
    total_combi = N*(N+1)/2




    count = 0
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


    print(match)
    return match

solve([1, 1, 2, 4, 2])
sys.exit(0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

