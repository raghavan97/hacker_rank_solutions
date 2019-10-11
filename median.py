#!/bin/python

import sys
import bisect

def median_of_list(s):
    n = len(s)
    #s = sorted(lst)
    if n == 1:
        return s[0]

    if n == 2:
        return float(s[0]+s[1])/2

    if n%2 != 0:
        return s[n/2]
    else:
        a = s[n/2]
        b = s[(n/2)-1]
        return float(a+b)/2

def print_it(n):
    mm = '{0:f}'.format(n)
    mm = mm.rstrip('0')
    mm = mm.rstrip('.')
    print(mm)


def median(a,x):
    # (['r', 'a', 'a', 'a', 'r', 'r', 'r'], [1, 1, 2, 1, 1, 2, 1])
    arr = zip(a,x)
    elem_list = []
    elem_dict = {}
    #for ta, tx in arr:
    count  = 0
    while count < len(a):
        ta = a[count]
        tx = x[count]
        #print(ta,tx)
        '''
        if tx == 936866298:
            print(tx)
            print("tx in elem_dict{}".format(tx not in elem_dict))
        '''

        if ta == 'r':
            if tx not in elem_dict:
                print("Wrong!")
            else:
                occ = elem_dict[tx]
                occ -= 1
                if occ == 0:
                    del elem_dict[tx]
                else:
                    elem_dict[tx] = occ

                ind = bisect.bisect_left(elem_list,tx)
                del elem_list[ind]
                if len(elem_list) == 0:
                    print("Wrong!")
                else:
                    m = median_of_list(elem_list)
                    print_it(m)
        else:
            if tx in elem_dict:
                elem_dict[tx] += 1
            else:
                elem_dict[tx] = 1

            bisect.insort(elem_list,tx)
            #print(elem_list)
            m = median_of_list(elem_list)
            print_it(m)

        count += 1
        #print("------------")
        #if count == 6:
        #   break
        

N = input()
s = []
x = []
for i in range(0, N):
    tmp = raw_input().strip().split(' ')
    s.append(tmp[0])
    x.append(int(tmp[1]))
    
median(s,x)
