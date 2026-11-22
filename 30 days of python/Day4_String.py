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
print(company[6:])
'''Check if Coding For All string contains a word Coding using the method index, find or other methods.'''
sub_string='Coding'
print(company.index(sub_string))
'''company = "Coding For All"
sub_string = "Coding"

# 1. Using index() (your solution — returns 0 if found, raises ValueError if not)
print(company.index(sub_string))      # 0

# 2. Using find() (returns 0 if found, -1 if not)
print(company.find(sub_string))       # 0

# 3. Using the 'in' operator (returns a clean True/False boolean)
print(sub_string in company)          # True

# 4. Using startswith() (since 'Coding' is at the start)
print(company.startswith(sub_string)) # True'''