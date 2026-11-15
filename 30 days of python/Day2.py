#help("keywords")
#help("async")
print(min(20,30,40,50))#min function is used to find the minimum value from the given values.
print(max(20,30,40,50))#max function is used to find the maximum value from the given values.
#Write a python comment saying 'Day 2: 30 Days of python programming'
#Day-2 : 30days of python programming
#Declare a first name variable and assign a value to it
Firstname="Ragu"
print(Firstname)
print(type(Firstname)) 
#Declare a last name variable and assign a value to it
Lastname='nathan'
print(Lastname)
print(type(Lastname))
#Declare a full name variable and assign a value to it
fullname='Ragunathan'
print(fullname)
print(type(fullname))
#Declare a country variable and assign a value to it
country = "India"
print(country)
print(type(country))
#Declare a city variable and assign a value to it
city = "coimbatore"
print(city)
print(type(city))
#Declare an age variable and assign a value to it
age = 25
print (age)
print(type(age))
#Declare a year variable and assign a value to it
year = 2001
print(year)
print(type(year))
#Declare a variable is_married and assign a value to it
is_married = 'false'
print(is_married)
print(type(is_married))
#Declare a variable is_true and assign a value to it
is_true = 'true'
print(is_true)
print(type(is_true))
#Declare a variable is_light_on and assign a value to it
is_light_on = 'true'
print(is_light_on)
print(type(is_light_on))
#Declare multiple variables on one line
first_name, last_name, country = "Ragu", "nathan", "India"
print(first_name, last_name, country)

#Check the data type of all your variables using type() built-in function -which is done above.

# Using the len() built-in function, find the length of your first name

#Compare the length of your first name and your last name
a=len(first_name)
b=len(last_name)
if a> b:
    print("a is greater than b" )
#Declare 5 as num_one and 4 as num_two
num_one= 5
num_two= 4
#Add num_one and num_two and assign the value to a variable total
total =num_one + num_two
print(total)
#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)
#Multiply num_two and num_one and assign the value to a variable product
prod=num_one * num_two
print(prod)
#Divide num_one by num_two and assign the value to a variable division
div=num_one/num_two
print(div)
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
mod=num_one % num_two
print(mod)
#Calculate num_one to the power of num_two and assign the value to a variable exp
pow=num_one**num_two
print(pow)
#Find floor division of num_one by num_two and assign the value to a variable floor_division
f_div=num_one//num_two
print(f_div)
#The radius of a circle is 30 meters.
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
r=30
area_of_circle = 3.14*r**2
print(area_of_circle) 
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
import math
circum_of_circle = 2*math.pi*r
print(circum_of_circle)
#Take radius as user input and calculate the area.
#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
