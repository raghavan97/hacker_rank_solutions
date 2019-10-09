import math
import os
import random
import re
import sys
from pprint import pprint

# https://www.hackerrank.com/challenges/crush/problem

# The information given in each row is captured in a dictionary col_summary
# The key for the dict col_summary is the index specified as start and end
# The following shows the dict col_summary progressively as each row entry
# is processed
# Entry - (1, 2, 100)
# col_summary = {1: [100], 3: [-100]}
# Entry - (2, 5, 100)
# col_summary = {1: [100], 2: [100], 3: [-100], 6: [-100]}
# Entry - (3, 4, 100)
# col_summary = {1: [100], 2: [100], 3: [-100, 100], 5: [-100], 6: [-100]}

# finally, when the max value needs to be computed , we iterate from
# the left i.e the least column and get the value for
# that column



# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    col_summary = {}

    for row in queries:
        st,end,k = row
        # print(st,end,k)

        if st in col_summary:
            col_summary[st].append(k)
        else:
            col_summary[st] = [k]

        end = end +1
        if end in col_summary:
            col_summary[end].append(-k)
        else:
            col_summary[end] = [-k]

        # print(col_summary)

    keys = sorted(col_summary.keys())

    max_val = 0
    left  = 0

    for k in keys:
        v = sum(col_summary[k])
        curr = v +left 
        # print("key={} val={}".format(k,curr))
        if curr > max_val:
            max_val = curr
        left  = curr

    # print(max_val)
    return max_val



# print uncomment these for tracing the algorithm
# n=5
# queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
# arrayManipulation(n,queries)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

