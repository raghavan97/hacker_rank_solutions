#!/bin/python

import math
import os
import random
import re
import sys

class Bucket(object):
    def __init__(self, max_val, max_val_index):
        self.max_val = max_val
        self.max_val_index = max_val_index
        self.values = []

    def add_value(self, val):
        self.values.append(val)

    def __repr__(self):
        bstr = "values={} max_val_index={} max_val={}".format(
            self.values, self.max_val_index, self.max_val
        )
        return bstr



class ArrayPairs(object):
    def __init__(self, arr):
        self.arr = arr
        self.arr_len = len(arr)
        self.match = 0

    def populate_DS(self):
        print(self.arr)
        i = 0
        buckets = []
        max_val = -1
        while i < self.arr_len:
            if self.arr[i] > max_val:
                max_val = self.arr[i]
                b = Bucket(max_val, i)
                buckets.append(b)

            b.add_value(self.arr[i])
            i += 1

        for b in buckets:
            print(b)
        self.buckets = buckets


    def solve(self):
        self.calc_match(self.arr)

    def calc_match_buckets(self, b1, b2):
        match = 0
        b1_values = sorted(b1.values)
        for i in b1_values:
            b2_values = sorted(b2.values)
            for j in b2_values:
                print("Trying {},{}".format(i,j))
                if i*j <= b2.max_val:
                    match += 1
                else:
                    break
        return match



    def solve2(self):
        i = 0
        n = len(self.buckets)
        while i < n:
            j = i + 1
            bi = self.buckets[i]
            self.calc_match(bi.values)
            while j < n:
                bj = self.buckets[j]
                mat = self.calc_match_buckets(bi,bj)
                self.match += mat
                j += 1
            i += 1




    def calc_match(self, li_values):
        i = 0
        n = len(li_values)
        a = li_values
        while i < n:
            ai = li_values[i]
            j = i + 1
            max_val = a[i]
            while j < n:
                if a[j] > max_val:
                    max_val = a[j]
                aj = a[j]
                print("trying {},{} max_val={}".format(ai,aj,max_val))
                if a[i]*a[j] < max_val:
                    self.match += 1
                j += 1
            i += 1



    def run(self):
        self.populate_DS()
        self.solve2()
        print(self.match)
        return self.match




# Complete the solve function below.
def solve(arr):
    ap = ArrayPairs(arr)
    ap.run()

#solve([1,3000, 28, 25, 4000, 15, 10, 6000, 24, 23, 8000, 25, 20])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

