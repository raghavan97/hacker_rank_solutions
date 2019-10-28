#!/bin/python

import math
import os
import random
import re
import sys

class ArrayPairs(object):
    def __init__(self, arr):
        self.arr = arr
        self.arr_len = len(arr)

    def populate_DS(self):
        print(self.arr)
        i = 0
        max_val = -1
        max_val_arr = dict()
        while i < self.arr_len:
            if self.arr[i] > max_val:
                max_val = self.arr[i]
                max_val_arr[i] = {'max_val': max_val, 'values': []}
                max_val_index = i

            max_val_arr[max_val_index]['values'].append(self.arr[i])
            i += 1


        self.max_val_arr = max_val_arr
        self.max_val_arr_keys = self.max_val_arr.keys()
        self.max_val_arr_keys.sort()
        for i in self.max_val_arr_keys:
            self.max_val_arr[i]['values'].sort()
            print(i,max_val_arr[i])

    def solve2(self):
        pass


    def solve(self):
        pass

    def run(self):
        self.populate_DS()




# Complete the solve function below.
def solve(arr):
    ap = ArrayPairs(arr)
    ap.run()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

