
#conditional statements:
'''they are programming structures which interrupt the normal flow
of the program and help in executing certain lines of code based on conditions
type:
1.if statement
2.if_else statementn
3.if _elif_elif ..else statement
'''
#1.if statement:
'''
it executes a block of code when the condition results in
boolean true
in case of fales ,the control goes to the next statement presention after if
syntax:

if boolean:
   indented block of code
   
intendation: the space present at the beginning of any line is called as indendation
the standard practice is to provide one tab space
all the lines enclosed as a block of code should be with the
same intendation
n=int(input('enter a number :'))
if n>0:
    doubled_n=2*n
    print(doubled_n)
print('completed')'''
#2.if else:
'''
it adds an alternate path to if conditional statement.
if the give condition results in boolean true if block of code will be executed
if the given codition results in boolean false ,else block of code will be executed 
syntax:
if cond :
     if block
else:
     else block

n=int(input())
if n>0:
    print('positive')
else:
    print('negative')
'''
#write a program to check if given string is a palindrome out put
#should be either palindrome or not .

"""s=input('enter a string')
rev_str=s[ : :-1]
if s==rev_str:
    print('palindrome')
else:
    print('not a palindrome')
    
lst=['sai','vivek','kumar']
if sai in lst:
   print('positive')
else:
    print('negative')
  

d={'bob':25,'sai':50}
name=input()
if name in d:
    print(d[name])
else:
    print('not present')

bill=int(input())
discounted=bool(int(input()))
if bill>2000:
    if discounted:
        print('no discounted')
    else:
        print('10% discount')

else:
     print('no discount')
     
"""
#write a porogram to take an integer input and do the following
'''
if it is even:
check for divisibility by 4
if it is divisible by 4 print even and divisible
else print even and not divisible
else print not even.
if n%2==0
if n%4==0:
print('even and divisible')
else:
  print('even and not divisible')
  esle:
  print('not even')'''












     
































