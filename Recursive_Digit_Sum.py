#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    string = str(n)
    lst = list(string)
    lst = list(map(int, string))
    temp = sum(lst) * k
    def helper(string):
        # print(string)
        if len(string) == 1:
            return int(string[0])
        lst = list(map(int, string))
        temp = sum(lst)
        temp = str(temp)
        return helper(list(temp))
    return helper(list(str(temp)))
    
            
    # if len()
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
