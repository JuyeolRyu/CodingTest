'''
Basic Statistics Warmup
https://www.hackerrank.com/challenges/stat-warmup/problem
'''

import sys
import numpy as np
from scipy.stats import mode
import math
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

print(np.mean(nums)) #평균
print(np.median(nums)) #중간값(짝수일 경우 중간값 2개 평균)
print(int(mode(nums)[0]))#가장 빈도가 높은 수
print(round(np.std(nums),1))#표준편차
a = round(np.mean(nums) - (1.96 * (np.std(nums) / math.sqrt(len(nums)))),1)
b = round(np.mean(nums) + (1.96 * (np.std(nums) / math.sqrt(len(nums)))),1)
print a,b #신뢰구간