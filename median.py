#!/bin/python

import sys
import statistics

def median_of_list(lst):
    return statistics.median(lst)
    n = len(lst)
    s = sorted(lst)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None

def print_it(n):
    if int(n) == n:
        print(int(n))
    else:
        print('{0:g}'.format(n))


def median(a,x):
    # (['r', 'a', 'a', 'a', 'r', 'r', 'r'], [1, 1, 2, 1, 1, 2, 1])
    arr = zip(a,x)
    elem_list = []
    elem_dict = {}
    for ta, tx in arr:
        # print(ta,tx)
        if ta == 'r':
            if tx not in elem_dict:
                print("Wrong!")
                continue
            else:
                del elem_dict[tx]
                elem_list.remove(tx)
        else:
            elem_dict[tx] = 999
            elem_list.append(tx)
        m = median_of_list(elem_list)
        print_it(m)
        

N = input()
s = []
x = []
for i in range(0, N):
    tmp = raw_input().strip().split(' ')
    s.append(tmp[0])
    x.append(int(tmp[1]))
    
median(s,x)
