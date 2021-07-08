'''
Polynomial Regression: Office Prices
https://www.hackerrank.com/challenges/predicting-office-space-price/problem
'''

import sys
import pandas as pd
import numpy as np
from sklearn import linear_model as lm
from sklearn import preprocessing as pp
input = sys.stdin.readline

F,N = map(int,input().split())
train = np.array([list(map(float,input().split())) for _ in range(N)])
T = int(input())
test = np.array([list(map(float,input().split())) for _ in range(T)])

lin_reg = lm.LinearRegression()
poly_reg = pp.PolynomialFeatures(3,include_bias=False)

lin_reg.fit(poly_reg.fit_transform(train[:,:-1]),train[:,-1])

result = lin_reg.predict(poly_reg.fit_transform(test))

for r in result:
    print(r)