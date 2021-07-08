'''
Correlation and Regression Lines - A Quick Recap #1
https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem?isFullScreen=true
'''
import math
physics = [15,12,8,8,7,7,7,6,5,3]
history = [10,25,17,11,13,17,20,13,9,15]

def cal_mean(li):
    return sum(li)/len(li)

def cal_variance(li,mean):
    n_sum = 0
    for l in li:
        n_sum += (l-mean)**2
    return n_sum/len(li)

def cal_std(variance):
    return math.sqrt(variance)

def cal_pearson(a,b,cov):
    return cov/(a*b)

physics_mean = cal_mean(physics)
history_mean = cal_mean(history)
physics2 = [x-physics_mean for x in physics]
history2 = [x-history_mean for x in history]

cov = sum([x*y for x,y in zip(physics2,history2)])
physics = sum([(x-physics_mean)**2 for x in physics])
history = sum([(x-history_mean)**2 for x in history])


print(round(cov/(math.sqrt(physics)*math.sqrt(history)),3))