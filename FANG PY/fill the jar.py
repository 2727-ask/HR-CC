#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n, operations):
    total_candies=0
    for i in operations:
        initial_index=i[0]
        limit_index=i[1]
        jars=(limit_index-initial_index)+1
        total_candies+=jars*i[2]
    return((total_candies//n))
if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    operations = []

    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))

    result = solve(n, operations)
    print(result)

