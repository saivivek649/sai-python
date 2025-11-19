#arthametic operators
#addition
"""a=90
b=20
c=a+b
print(c)"""
#dynamic addition
"""a=int(input('enter first number'))
b=int(input('enter second number'))
c=a+b
print(c)"""
# multiplication
"""a=int(input('enter first number'))
b=int(input('enter second number'))
c=a*b
print(c)"""
#divition
"""a=int(input('enter first number'))
b=int(input('enter second number'))
c=a/b
print(c)"""
# substraction
"""a=int(input('enter first number'))
b=int(input('enter second number'))
c=a-b
print(c)"""
# exponent
"""a=int(input('enter first number'))
b=int(input('enter second number'))
c=a**b
print(c)"""
# flore division
"""a=int(input('enter first number'))
b=int(input('enter second number'))
c=a//b
print(c)"""
#all in one
"""sai=int(input('enter first number'))
vivek=int(input('enter second number'))
print(sai+vivek)
print(sai*vivek)
print(sai/vivek)
print(sai//vivek)
print(sai**vivek)
print(sai-vivek)"""
#2.comparision operator
"""
a=int(input('enter the number:'))
b=int(input('enter second number:'))
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)
print(a<b)
print(a>b) """
"""
sec=int(input('enter sec'))
hrs_sec=5*60*60
print(sec>=hrs_sec)"""
#3.logical operator
""" working of not :
it is an unary operator that works on single boolen operand
it gives the inverse of the boolean operand
not true    false
not false    true
"""
#write a program to check if the given input number exists
#in range of  0 to 100
"""
a=int(input('enter the number'))
range_con=a>0   and a<100
print(range_con)"""

#check if the given number is either smaller than 100 or greater than 0"
"""print(not true)
"""
#4.membership operator
"""t=[1,3,4,5,6]
print(3 in t)"""
#5.identity operator:
"""lst_1=[1,2,3]
lst_2=[1,2,3]
print(lst_1 is lst_2)
print(id(lst_1))
print(id(lst_2))"""# immutable
#mutable
"""a=5
b=5
print(a is b)
print(id(a))
print(id(b))"""
#6.assignment operators
"""they are used to assingn vales to variables or update values present in variables
= -is used to assign value to varaibles
+= -used to certain quantity
-=,*=,/=,//=,**=,%==
"""
"""n=2
incre_n=n+5
print(incre_n)
n=3
n/=3
print(n)"""
#7.bitwise operator
"""these are used for bit level operations
these are symbols
&-bitwise and
|-bitwise or
^-bitwise xor
~-bitwise not
>>-right shift
<<-left shift"""

#1.bitwise and:
"""it works similar to logical and
it compares bits at specific position in both the operationds and decides what should be the bit at position in
the resultant if both the bits are 1 then the resultant will be if both the bits are 1 then the resultant will be 1 else 0
"""
"""a=5#0101
b=3#0011
#0001
print(a&b)

"""
#2.bitwise or
"""
a=5#0101
b=3#0011
#0111
print(a|b)
"""
#3.bitwise xor:
"""if both are diffrent it print 1 then 0
a=5#0101
b=3#0011
#0111
print(a^b)"""
#4.bitwise not:
"""this is an unary it inverse the bit given in the number
~= -n-1
a=6
print(~6)#-6-1=-7
print(~-5)#-(-5)-1=4"""
#5.leftshift (<<)
"""this operator is used to move all the bits to left by given number of position
the result of a <<nwill be a*2^n
a=100
print(a<<3)
"""
#6.rightshift(>>)
"""this operator is used to move all the bits to right by given number of position
the result of a >> n will be a//2^n"""
"""a=100
print(a>>3)
"""































































      


