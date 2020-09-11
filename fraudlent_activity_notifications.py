#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import median

# Complete the activityNotifications function below.

def activityNotifications(expenditure, d):
    notifications = 0
    expLen = len(expenditure) - d
    index = 1
        
    for i in range(expLen):
        remaining = expenditure[i:d+i]
        current = expenditure[expLen+index]
        med = median(remaining)
        p = 2 * med
        if current >= p:
            notifications += 1
        index += 1
        
    return notifications
            
       
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
