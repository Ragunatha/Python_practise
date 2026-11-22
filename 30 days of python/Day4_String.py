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
