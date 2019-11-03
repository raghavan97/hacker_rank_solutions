#!/bin/python

import math
import os
import random
import re
import sys
import bisect

class Bucket(object):
    def __init__(self, max_val, max_val_index):
        self.max_val = max_val
        self.max_val_index = max_val_index
        self.values = []

    def add_value(self, val):
        self.values.append(val)

    def store_sorted_values(self):
        self.sorted_values = sorted(self.values)

    def __repr__(self):
        bstr = "values={} max_val_index={} max_val={}".format(
            self.values, self.max_val_index, self.max_val
        )
        return bstr



class ArrayPairs(object):
    def __init__(self, arr):
        self.orig_arr = arr
        self.orig_arr_len = len(arr)
        self.match = 0
        self.arr = []


    def populate_DS(self):

        i=0
        n = len(self.orig_arr)
        no_of_ones = 0
        while i < n:
            if self.orig_arr[i] == 1:
                no_of_ones += 1 
            else:
                self.arr.append(self.orig_arr[i])
            i += 1

        no_of_terms = no_of_ones
        highest = len(self.orig_arr) - 1
        least = highest - no_of_terms + 1
        self.match += ((no_of_terms)*(highest+least))/2
        #print(self.match)

        #self.arr = self.orig_arr
        self.arr_len = len(self.arr)

        #print(self.arr)
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
            b.store_sorted_values()
        self.buckets = buckets


    def calc_match_buckets(self, b1, b2):
        match = 0
        for i in b1.sorted_values:
            cnt = bisect.bisect_right(b2.sorted_values, b2.max_val/i)
            match += cnt
        return match

    def solve2(self):
        i = 0
        n = len(self.buckets)
        while i < n:
            j = i + 1
            bi = self.buckets[i]
            self.match += self.calc_match(bi.values, bi.sorted_values)
            while j < n:
                bj = self.buckets[j]
                ret = self.calc_match_buckets(bi,bj)
                self.match += ret
                j += 1
            i += 1

    def calc_match(self, li_values, sorted_values):
        i = 0
        n = len(li_values)
        a = li_values
        match = 0

        if sorted_values[0] == sorted_values[len(sorted_values)-1]:
            return 0

        if n > 50:
            num = bisect.bisect_right(sorted_values,1)
            mm = solve(li_values[1:n])
            mm += num
            return mm

        while i < n:
            ai = li_values[i]
            j = i + 1
            max_val = a[i]
            min_expected = max_val/ai
            while j < n:
                if a[j] > max_val:
                    max_val = a[j]
                    min_expected = max_val/ai
                if a[j] <= min_expected:
                    match += 1
                j += 1
            i += 1

        return match


    def run(self):
        self.populate_DS()
        self.solve2()
        return self.match

# Complete the solve function below.
def solve(arr):
    ap = ArrayPairs(arr)
    ret = ap.run()
    return ret

def debug_main(fname):
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    with open(fname, 'r') as fd:
        arr_count = int(fd.readline())
        line = fd.readline().split()
        arr = [int(i) for i in line]
    result = solve(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

#debug_main(sys.argv[1])

#solve([1,3000, 28, 25, 4000, 15, 10, 6000, 24, 23, 8000, 25, 20])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

