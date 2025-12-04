#set:
'''a set is a muttable ,unordered collection of unique and immutable
elements enclosed in curly brackets'''
'''s={1,5.9,(1,2),'python'}
print(s)
st={1,2,3,4,2,34,1,2,3,}
print(st)
set_1={34,6,1,95}
print(set_1)'''
#{1,2,3,4}
'''print(type(set_1))
s='python'
s_set=set(s)
print(s_set)'''
#set operation
#operators
#in ,not in can be used
#is,is not can be used
#some operation are used for special set opeartions like union
#union opeartion -|
#it is used to get element from both the sets together 
'''a={1,2,3,4,4,5}
b={3,4,5,6,7,8}
print(a|b)'''
#intersestion-&
#it is used to get common element from both the sets
'print(a&b)'
#difference - -
#it is used to get element present only in fiest set
'print(a-b)'
#symmentric difference -^
#it is used to get element that are not common to both the set
'print(a^b)'
#>=,<=,!=
'''sup_set = {1,2,3,4,5,6,7}
sub_set = {2,4,6,11}
print(sup_set >= sub_set)
print(sup_set != sub_set)'''
#set methods - methods defined inside set class
#we have to use these methods as set_obj.fun_name()
'example={1,2,3,4}'
#add(ele)
'''example.add(5)
print(example)'''
#update()-adds group of elements
'''example.update({10,20,30})
print(example)'''
#for removeing elements
#remove(ele)
'''example.remove(5)
print(example)'''
#discard(ele)
'''example.discard(3)
print(example)'''
#pop()
'''example.pop()
print(example)'''
#clear()
'''s={ }
print(type(s))
example.clear()
print(example)'''
#union()
"""set_1={1,2,3,4}
set_2={7,8,9,6}
print(id(set_1))
print(id(set_1.union(set_2)))"""
#intersection()
'print(id(set_1.intersection(set_2)))'
#difference()
#symmentric_difference()
#issuperset(),issubset(),isdisjoint()
'set_1.issubset(set_2)'
#typeconversion
"""int-int()
float-float()
string-str()
list-list()
tuple-tuple()
dict-dict()-directly not possible incase
iterables are having nested elements of length 2 then it can
be possible
set-set()
boolean-bool()"""



#out put formatting :
"""
formatting done in print statement to acheive output in descired
way
different ways:
1.comma based formatting
2.modulo operatior based
3.formatted string literals
4.format method of string class
"""
#1.comma based:we give multiple object withh commas in print function
#they will be converted to a single string with spaces with them
"""name=input()
age=int(input())
print(name,'is',age,'years old')

b=int(input())
h=int(input())
area=0.5*b*h
print('he area of given triangle is:', area )"""
#2.modulo operator based formattingwe use formating specifiers
"""in string and pass values that have to
be replaced with those
syntax:
string with format specifier '%(values following proper order)
%d-int format specifier
%s-string %f-float
%.nf-float with n digits after decimal point it
can be used for rounding off
name=input()
age=int(input())
print('%s is %d years old'%(name,age))
num=31.5278
print('the rounded off number is :%.2f'%(num,))"""
#3.formatted string literals
'''
we use f at the beginning of the string and place holders in string
{} brackets are used as place holders
syntax:
f'string with place holder and values to be emdedded'

name =input()
age=int(input())
print(f'{name}is {age} years old')'''

#4.format method in string class
'''we use place holders in the string and pass those values to
format function
syntax:
'string with place holders' .format (v1,v2,v3....)
name=input()
age=int(input())
op='{} is {} years old'#we can also use values
print(op.farmat(name, age))































































































       










































