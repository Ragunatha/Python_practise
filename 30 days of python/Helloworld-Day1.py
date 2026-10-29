#Day1-Exercise level-1
print(1+6)#addition
print(1-6)#subtraction
print(1*6)#multiplication
print(19/6)#division
print(1%6)#modulus
print(2**6)#exponentiation
print(19//6)#floor division-which gives the quotient of the division and ignores the remainder and gives the largest integer less than or equal to the result of the division as a whole number

print("Ragunathan")#string-double quote
print('Pathar-vishwakarma')#string but it is a single quote
print ("I am enjoying 30 days of python")#string with double quote

print(type(10))#int
print(type(3.14))#float
print(type(1+3j))#complex
print(type('Ragunathan'))#string
print(type([12.13,15]))#list
print(type((12.13,15)))#tuple
print(type({12.13,15}))#set
print(type({'name': 'Ragunathan'}))#dictionary

#Day1-Exercise level-2-which is to create the folder and to check the with the above examples ,Completed.

#Exercise level-3.Find an Euclidean distance between (2, 3) and (10, 8)
x1,y1=16,10
x2,y2=10,8
Euclidean_distance=((x2-x1)**2+(y2-y1)**2)**0.5#with out using math import module.
print(Euclidean_distance)

import math#to use the math module to find the Euclidean distance between two points in a 2D space.
x1, y1 = 2, 3
x2, y2 = 10, 8
distance = math.hypot(x2 - x1, y2 - y1)#To hypot is the function which is used to find the Euclidean distance between two points in a 2D space.
print(distance)