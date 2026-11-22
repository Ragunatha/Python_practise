#Declare your age as integer variable
age=25
print(type(age),age)
#Declare your height as a float variable
Height_in_feet=6.0
print(type(Height_in_feet),Height_in_feet)
#Declare a variable that store a complex number
complex_no = 2j+9
print(type(complex_no),complex_no)

'''Write a script that prompts the user to 
enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).'''
base = float(input("Enter the base of the triangle to find the area : "))
height = float(input("Enter the height of the Triangle to be calculated : "))
area = 1/2*base*height
print(type(area), "The Calculated Triangle area : ", area)

'''Write a script that prompts the user to enter side a, side b, and side c of the triangle.
Calculate the perimeter of the triangle (perimeter = a + b + c).'''
a = float(input("Enter side A of the triangle perimeter : "))
b = float(input("Enter side B of the triangle perimeter : "))
c = float(input("Enter side C of the triangle perimeter : "))
perimeter_value = a+b+c
print(type(perimeter_value), "The calculate perimeter of the triangle is : ", perimeter_value)

'''Get length and width of a rectangle using prompt. 
Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))'''
length = float(input("The length of rectangle is : "))
width = float(input("The width of rectangle is : "))
Rectangle_Perimeter = 2*(length + width )
Rectangle_area = length * width
print(type(Rectangle_area),"The area of rectangle is : ",Rectangle_area)
print(type(Rectangle_Perimeter),"The Perimeter of the rectangle : ",Rectangle_Perimeter)

'''Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
'''
import math
r=float(input("Enter the radius of the circle : ",))
area_of_circle = math.pi*r**2
circumference_of_circle = math.pi*r*2

'''Calculate the slope, x-intercept and y-intercept of y = 2x -2'''
#Actually the slop equation is y=mx+b here 'm' is the slope
m_8=2#slope is already given
b=-2
#need to find y_intercept and x_intercept
#To find Y_intercept x should be zero(i.e)x=0
x=0
y_intercept = m_8 * x + b
print("Y_intercept : ",y_intercept)
#To find X_intercept y should be zero(i.e)y=0
y=0
x_intercept = (y-b)/m_8
print("X_intercept : ",x_intercept)

'''Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)'''
import math
x1,y1=2,2
x2,y2=6,10
m_9=(y2-y1)/(x2-x1)
print("The slope m : ",m_9)
p1=(2,2)
p2=(6,10)
Euclidean_distance = math.dist(p1,p2)
print("Euclidean_Distance : ",Euclidean_distance)

'''Compare the slopes in tasks 8 and 9.'''
m_8=2
m_9=2.0
The_slope= "Both are same" if m_8 == m_9 else m_9

'''Calculate the value of y (y = x^2 + 6x + 9). 
Try to use different x values and figure out at what x value y is going to be 0.'''
for x in range (-4,1):
    y=x**2+6*x+9
    print(f"x value : ,{x}    y value : ,{y}")

'''Find the length of 'python' and 'dragon' and make a falsy comparison statement.'''
a='python'
b='dragon'
print(len(a)>len(b))

'''Use and operator to check if 'on' is found in both 'python' and 'dragon'''
if 'on' in 'dragon' and 'python':
    print("True")

'''I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.'''
a='I hope this course is not full of jargon'
if 'jargon' in a:
    print("True")

'''There is no 'on' in both dragon and python'''
print('on' not in 'dragon' and 'on' not in 'python')

'''Find the length of the text python and convert the value to float and convert it to string'''
a='python'
b=len(a)
c=float(b)
d=str(c)
print(type(c),type(d))

'''Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?'''
a=int(input())
if a%2==0:
    print(a,"even number")
else:
    print("Odd number")

'''Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.'''
a=int(2.7)
if 7//3==a:
    print("True")
print(type(a))

'''Check if type of '10' is equal to type of 10'''
print(type(10)==type('10'))

'''Check if int('9.8') is equal to 10'''
print(type(int(9.8))==type(10))
print((int(9.8))==10)

'''Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?'''
H=float(input("Enter the working hour: "))
R_H=float(input("Enter the rate per hour: "))
print("The weekly earning is: ",H*R_H)

'''Write a script that prompts the user to enter number of years. 
Calculate the number of seconds a person can live. Assume a person can live hundred years'''
a=int(input("Enter number of years you have lived: "))
print("You have lived for",a*31536000,"seconds")

'''Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125'''

a=1
for a in range(1,6,1):
    result=0
    result+=a
    print(result,result**0,result**1,result**2,result**3)