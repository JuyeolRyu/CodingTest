'''
Correlation and Regression Lines - A Quick Recap #2
https://www.hackerrank.com/challenges/correlation-and-regression-lines-7/problem?isFullScreen=true
'''
'''
reg_slope = covariance(x,y)/variance(x)
회귀라인 기울기 = 공분산(x,y)/분산(x) ==>x가 독립 변수일 경우
분산(X) = [(x[i]-x평균)**2 for i in range(len(x))] 의 평균
공분산(X,Y) = [(x[i]-x평균)*(y[i]-y평균) for i in range(len(x))] 의 평균
'''
import math
x = [15,12,8,8,7,7,7,6,5,3]
y = [10,25,17,11,13,17,20,13,9,15]

x_mean = float(sum(x))/len(x)
y_mean = float(sum(y))/len(y)

x2 = [num-x_mean for num in x]
y2 = [num-y_mean for num in y]

covXY = sum([n1*n2 for n1,n2 in zip(x2,y2)])/len(x)
varX = sum([num*num for num in x2])/len(x)
reg_slope = round(covXY/varX,3)

print(reg_slope)