# -*- coding: utf-8 -*-
"""polynomial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BagmWM7QA5kWs2_zhCpL2T8znMQdbRMi
"""

def index_in_list(a_list, index):
    return (index < len(a_list))

from math import exp as e
from math import cos as cos
import math
from sympy import *
from math import *
from __future__ import division
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange
from scipy.interpolate import splrep
from scipy import interpolate

'''This code is to input the function, compute x values according to the given n
 and the y values of that function against those values'''

fx = '(exp(x) + 2**-x+ 2*cos(x) - 6)'
f= lambda x: eval(fx)
interval_start= input("enter starting point: ")
interval_end= input("enter ending point: ")
n= int(input("enter n: "))
x=[]
y_values=[]
difference= (int(interval_end) - int(interval_start))/int(n)
for i in range(n+1):
  x.append(int(interval_start) + i*difference)
for i in x:
  y_values.append(f(i))


'''This peice of code is to form the lagrange polynomial of the equation'''
poly = lagrange(x, y_values)
print(poly)
lang_vals=poly(x)

'''This peice of code is to form the cubic Spline function against the equation  values'''
c_s=splrep(x,y_values,s=0)
ynew = interpolate.splev(x, c_s, der=0)

"""This peice of code is to create a divided difference table in the TxT file"""
x_increment=0
dict = {'y':y_values}
diff = []
count = 0
while True:
 length = len(y_values)
 if length == 0:
   break
 for i in range(len(y_values)-1):
   diff.append(((y_values[i+1]-y_values[i])/(x[i+1+x_increment]-x[i])))
 
 y_values = diff
 diff=[]
 dict['y'+str(count)] = y_values
 count+=1
 x_increment+=1

file2 = open("Divied_Difference_Table.txt","w")
file2.write("x                                             ")
print(x)
'''for i in range(len(x)):
  file2.write(str(x[i])+"\n")'''
for key in dict.keys():
  file2.write(str(key) + "                                             ")

file2 = open("Divied_Difference_Table.txt","a")
file2.write("\n")
counter=0
while counter<len(dict)-1:
  file2.write(str(x[counter])+"                                    ")
  for data in dict.keys():
    if (index_in_list(dict[data],counter)==True):
     file2.write(str(dict[data][counter])+ "                      ")
  file2.write("\n")
  counter+=1

'''This peice of code is to show graphs of each equations seperately and a 
graph showing their comparisions also'''

'''Shows the function Graph'''
plt.plot(x,dict['y'],'gs-',  label='F(x)')
plt.title("Polynomial Function")
plt.xlabel("X values")
plt.ylabel("F(x)")
plt.show()
plt.clf()
'''Shows the lagrange graph'''
plt.plot(x,lang_vals, 'yo-', label='Langrange')
plt.title("Langrange Plot")
plt.xlabel("X values")
plt.ylabel("F(x)")
plt.show()
plt.clf()

'''Shows the cubic Spline graph'''
plt.plot(x,ynew, 'bo-', label='Langrange')
plt.title("Cubic Spline")
plt.xlabel("X values")
plt.ylabel("F(x)")
plt.show()
plt.clf()

'''Shows the comaprision of all graphs'''
plt.plot(x,dict['y'],'gs-',  label='F(x)')
plt.plot(x,lang_vals, 'yo-', label='Langrange')
plt.plot(x,ynew, 'bo-', label='Langrange')
plt.title("Comparision")
plt.xlabel("X values")
plt.ylabel("F(x)")
plt.show()
plt.clf()

