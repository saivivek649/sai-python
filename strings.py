#strings
"""
strings is an immutable ordered sequence of characters enclosed in quotation marks
*for single line strings we use single  quatation mark
*for multi line strings we use three  quatation marks."""
"""
string='abc123 [.&'
print(string)"""
#empty string
"""print('')"""
"""sai=input('enter the value')
print(type(sai))
print(sai)"""
#to convert any other compatible data type into string data type we use str() function
"""a=14
print(type(a))
int_str=str(a)
print(type(int_str))
"""
#string operations;
"""
1.operation that work on string
*a.+(string concatenation)-can be used for jionig two or more strings together
"""
"""first="sai"
second="vivek"
full_name=first+second
print(full_name)
*b. string reputation -*- repeats characters present in given string
s='sai
print(s*3)"""
"""
*c.relational operators -compares based on ascii values
a=30
b=20
print('a'>'b')
d.we can use identity and membership operators
print('p'in python)
"""
"""
2.indexing and slicing
index tells about position of charater
we have types of indexing.
1.zero based indexing
it goes from left to right
it runs from 0 to n-1 where n represents total no of charater
2.negitive indexing
it goes from right to lift
it runs from -1 to -n
"""
"""
s='sai'
print(s[2])
print(s[-1])"""

#write a program to cheack if the last but one charater from
#the given iput string is a vowel
#true or false is the expected output
"""inp=input()
ch=inp[-2]
print(ch in 'aeiou')"""
#2.slicing;
"""obtaining a substracting from given string is called as slicing"""
"""s='python'
print(s[1:4:2])
"""
"""s='python'
print(s[-5:-1])"""

#write a program to check if given string is palindrome
"""s=input("give a string ")
r=s[ : :-1]
print(s==r)"""
#3.builtin functions
"""
1. len()-it is use to check no of element in any iterable
s='saivivek'
print(len(s))
2. max() /min()
they are used to return maximum and minimum element in given iterable
s='saivivek'
print(min(s))
print(max(s))

3.sorted()
it gives a sorted list of all the elements in given iterable
s='asdd'
print(sorted(s))

4. char()/ord()
they are used for fetching characters and ascii values
print(ord('a'))
print(chr(65))"""

#operation on string using function(methods)present in str class

"""
syntax:
string_object.function_name()
"""
#case convertion methods
"""s='python'
s1=s.upper()
print(s1)
"""
"""
s='PyThoN'
print(s.lower())
print(s.swapcase())"""
#validation methods
"""s='adc'
print(s.isalpha())
print(s.isdigit())"""
#searching methods
"""s='abcdaa'
print(s.index('a'))
print(s.find('e'))
print(s.rindex('a'))
print(s.rfind('e'))"""
#counting method
"print(s.count('a'))"
#splitting and joining methods
"""s='1 2 3 4 5'
print(s.split())
s='1, 2, 3, 4, 5'
print(s.split(','))
1st=['this','is','python']
print(" ".join(1st))"""
#stripping methods
"""s='   python   '
print(s.strip(" "))"""
#formatting methods
"""s='my name is {}'
inp=input()
print(s.format('saivivek'))"""
#write a program to check if given string can be a valid password
#conditions:
#password should have at least 4 characters and a max of 7 char
#should always start with alphabet only
#give o/p as true or false
















































































