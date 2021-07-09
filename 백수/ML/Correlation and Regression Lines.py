'''
Correlation and Regression Lines - A quick recap #3
https://www.hackerrank.com/challenges/correlation-and-regression-lines-8/problem
'''
'''
slope(x,y) = cov(x,y)/var(x)
intercept_y = avg(y)-slope(x,y)*avg(x)
'''
x = [15,12,8,8,7,7,7,6,5,3]
y = [10,25,17,11,13,17,20,13,9,15]

x_mean = float(sum(x))/len(x)
y_mean = float(sum(y))/len(y)

x2 = [num-x_mean for num in x]
y2 = [num-y_mean for num in y]

covXY = sum([n1*n2 for n1,n2 in zip(x2,y2)])/len(x)
varX = sum([num*num for num in x2])/len(x)
reg_slope = round(covXY/varX,3)
intercept_y = round(y_mean-reg_slope*x_mean,3)
ans = reg_slope*10+intercept_y
print(ans)