# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 13:53:08 2022

@author: bskyl
"""
# import pandas as pd
# import matplotlib.pyplot as plt
# from decimal import Decimal
# import numpy as np
# x = np.r_[1.:20.:0.1]
# x1=[]
# y1=[]
# for i in x:
#     i=round(i,2)
#     x1.append(i)
# print(x1)
# for j in x1:
#     y=(5*j**2)+15 
#     y=round(y,2)
#     y1.append(y)
# print(y1)
# y1=np.array(y1)
# data=pd.DataFrame({"x":x,"y":y1})
# print(data)

# plt.scatter(x1, y1)
# plt.xlabel('independent values')
# plt.ylabel('dependent values')
# plt.show()

# from scipy.interpolate import interp1d
  

  
# # test value
# interpolate_x = [1.02,2.06,5.15,10.12,19.81]
  
# # Finding the interpolation
# y_interp = interp1d(x1, y1)
# print("Value of Y at x = {} is".format(interpolate_x),
#       y_interp(interpolate_x))




# from sympy import *
# import numpy as np
# x = Symbol('x')
# y = x**2 + 1
# yprime = y.diff(x)
# print(yprime)


# f = lambdify(x, yprime, 'numpy')
# f(np.ones(5))
# [ 2.  2.  2.  2.  2.]


from sympy import * 
y=Symbol('y')                   
print(integrate(3y+4))














