#!/bin/python3
#Level: MEDIUM - https://www.hackerrank.com/challenges/encryption/problem

import math
import os
import random
import re
import sys
import math
from collections import defaultdict


# Complete the encryption function below.
def encryption(s):
    arrLen = len(s)
    n = math.sqrt(arrLen)
    columns = math.ceil(n)
    rows = math.floor(n)
  
    if (rows * columns) < arrLen:
        rows += 1

    string = ''
    ms = defaultdict(lambda : string)

    for i in range(0, arrLen, columns):  
        part = s[ i : i+columns]
        
        for letter in range(len(part)):
            ms[letter] += part[letter]
    
    encoded = ms.values()
    return (" ".join(map(str,encoded)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
