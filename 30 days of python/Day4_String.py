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


