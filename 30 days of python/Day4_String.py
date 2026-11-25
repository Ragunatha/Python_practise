#Hello starts with Day 4 python
''' Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.'''
a=['Thirty', 'Days', 'Of', 'Python' ]
print(' '.join(a))
'''Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'''
b=['Coding', 'For' , 'All']
print(' '.join(b))
'''Declare a variable named company and assign it to an initial value "Coding For All".'''
company="Coding For All"
print(company)
'''Print the length of the company string using len() method and print().'''
print(len(company))
'''Change all the characters to uppercase letters using upper() method.'''
print(company.upper())
'''Change all the characters to lowercase letters using lower() method.'''
print(company.lower())
'''Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.'''
print(company.capitalize())
print(company.title())
print(company.swapcase())
'''Cut(slice) out the first word of Coding For All string.'''
print(company[6:])#removes till 6 character array positions
'''Check if Coding For All string contains a word Coding using the method index, find or other methods.'''
sub_string='Coding'
print(company.index(sub_string))
print(company.find(sub_string))
print(sub_string in company)
print(company.startswith(sub_string))#using Startswith() return true if present the word present
'''Replace the word coding in the string 'Coding For All' to Python.'''
print(company.replace('Coding','Python'))
'''Change "Python for Everyone" to "Python for All" using the replace'''
a="Python for Everyone"
print(a.replace('Everyone','All'))#using .replace ()
print(a[:11] + 'All')#In which a[:11] removes the Everyone by the character E-11 position of string
word = a.split()
print(word)
word[-1]='All'#Syntax: separator.join(iterable)
print(' '.join(word))#here the word is splited by seperate words and it's last word in statement gets  changed and joined back.
'''Split the string 'Coding For All' using space as the separator (split()) .'''
a='Coding For All'
print(a.split())
'''"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.'''
a="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(a.split(','))
'''What is the character at index 0 in the string Coding For All.'''
a="Coding for All"
print(a[0])
'''What is the last index of the string Coding For All.'''
a='Coding for All'
print(a[-1])
'''What character is at index 10 in "Coding For All" string.'''
a='Coding for All'
print(repr(a[10]))#repr-which seperately represents the space
'''Create an acronym or an abbreviation for the name 'Python For Everyone'
'''
b="Python For Everyone"
a=b.split()
Acronymn=a[0][0]+a[1][0]+a[2][0]
print(Acronymn)

'''Another-way:
b="Python For Everyone"
a=''.join(word[0].upper() for word in b.split())
print(a)
'''

#Create an acronym or an abbreviation for the name 'Coding For All'.
a='Coding For All'
b=''.join(word[0].upper() for word in a.split())
print(b)
#Use index to determine the position of the first occurrence of C in Coding For All.
a='Coding For All'
print(a.index('C'))
#Use index to determine the position of the first occurrence of F in Coding For All.
a='Coding For All'
print(a.index('F'))
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
a='Coding For All People'
print(a.rfind('l'))
#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
a='You cannot end a sentence with because because because is a conjunction'
print(a.index('because'))
print(a.find('because'))
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
a='You cannot end a sentence with because because because is a conjunction'
print(a.rindex('because'))
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
a='You cannot end a sentence with because because because is a conjunction'
print(a[31:54])#That is the last occurrence of because in index is 47 position you just add the length of that single last word (47 + 7 = 54)
#Does 'Coding For All' start with a substring Coding?
a='Coding For All'
print(a.startswith('Coding'))
#Does 'Coding For All' end with a substring coding?
a='Coding For All'
print(a.endswith('coding'))
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
a='   Coding For All      i'
print(a.strip())#If you ever only want to remove spaces from one side, Python also has .lstrip() for the left side and .rstrip() for the right side.
'''Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python'''
a='30DaysOfPython'
b='thirty_days_of_python'
print(a.isidentifier())#Python variable names cannot start with a digit like 3 shows false
print(b.isidentifier())#True as output
'''The following list contains the names of some of python libraries:
 ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
Join the list with a hash with space string.'''
a=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(a ))#syntax separator.join(list_variable)
'''Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.
'''
a='I am enjoying this challenge\nI just wonder what is next'
print(a)
'''Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland  '''
a='Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki'
print(a.expandtabs(10))
'''Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
'''
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius,area))
'''Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144'''
a=8
b=6
print(
'{} + {} = {}\n'.format(a,b,a+b),
'{} - {} = {}\n'.format(a,b,a-b),
'{} + {} = {}\n'.format(a,b,a*b),
'{} + {} = {:.2f}\n'.format(a,b,a/b),
'{} + {} = {}\n'.format(a,b,a//b),
'{} + {} = {}\n'.format(a,b,a%b),
'{} + {} = {}\n'.format(a,b,a**b)
)