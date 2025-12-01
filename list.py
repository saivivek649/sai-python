#it's python class
"""print("it's python class")
list:
a list is a mutable, ordered collection of heterogenous elements
enclosed in square brackets
#homogenous is same data types
#heterogenous is differenet data types
#empty list
empty-lst-[]
#nested list
n-lst - [[1,2], [2,3]]"""
#['python','sql','html','js']
"""inp=input("enter list: ")
b=inp.strip('[ ]')
lst=b.split(',')
print(lst)
print(type(lst))"""
#if input format is space seperated string elements
#python sql html
"""
lst=input().split()
print(lst)
print(type(lst))
"""
#if input format is space seperated integer elements
"""inp=input().split()
int_lst=list(map(int,inp))
print(int_lst)"""
#write aprogram to print number of words in given input sentance
#sample input :this is python
#sample output:3
"""a=input().split()
print(a)
print(len(a))"""
#find the average of the give space seperated numbers
#sample input:12 1 80 4
#sample output:
"""a=list(map(int,input().split()))
sum_num=sum(a)
n=len(a)
avg=sum_num/n
print(avg)"""
#list operations:
"""
1.
"""
#1. + can be used for joining two lists
"""lst_1=[1,2]
lst_2=[3,4]
new=lst_1+lst_2
print(new)"""
#write a program to print to the second largest element from
#two given lists
#sample input:
#12,63,3
#90, 45,32
#sample output:
#63
"""lst_1=list(map(int,input().split(',')))
lst_2=list(map(int,input().split(',')))
result=lst_1+lst_2
sorted_lst=sorted(result)
print(sorted_lst[-2])"""
#2. * can be used for list repetition
"""1=[1,2]
print(1*2)"""
#3.in, not in can be used
"""print(1 in [1,2])"""
#4.is,is not can be used


#builtin function:
"""len(),min()/max(),sorted(),sum()
"""
#indexing and slicing
"""
everything from string class holds true over here in list class also
as list is mutable ,element at a particular position can be change
using their respective index

lst=[11,22,33,45]
print(lst)
lst[3]=44
print(lst)"""
#write a program to print the number of elements present at
#odd indices for the given list of elements
#sample input:1,2,3,4,5,6
#sample output:2
"""
lst=[1,2,3,4,5,6]
odd_lst=lst[1: :2]
print(len(odd_lst))"""
#list class methods
"""these are the functions defined in list class to use them
syntax:list_object.fun_name()"""
# a sequence of natural number is given
#find out missing number from that sequence
#sammple:1 2 3 4 6 7 8
#out put:5

#list methods
"""lst=[5,10,15,20,25]"""
#for Adding element
#append (ele)-adds that given element to the end of the list
"""lst.append(30)
print(lst)"""
#insert (ele,pos)-it insert the given element at that
#position
"""lst=[5,10,20,25,30]
lst.insert(2,15)
print(lst)"""
#extend(iter)-it adds all the element from given iterable
#at the end of existing list
"""next_multiples=[35,40,45]
lst.extend(next_multiples)
print(next_multiples)"""
#removing elements
#remove(ele)-it takes the elenent to be removed
#incase of multiple occurences itremoves the first occurence
"""lst=[1,2,3,4]
lst.remove(3)
print(lst)"""
#pop(index)
"""
a=[1,2,3,3]
a.pop()
print(a)
b=[2,3,4,5]
b.pop(3)
print(b)"""

#clear()-remoives all elements
#index(ele) -returns first index of the element we have given
#count(ele)-0counts occurences
#sort()-sorts given list
#reverse()-reverses the given list
#copy()-creates acopy of the given list
"""
the weekly log of a persons excise machine is given as input
find out on which day of the week he has sept more on
exrecising
sample input:
sigke line with space seperated numbers which are minutes he exercised
12 40 50 75 45 30 20
output
4
"""
"""
week=list(map(int,input().split()))
max_ele=max(week)
day=week.index(max_ele)+1
print(day)"""
#tapule:
"""
a tapule is immutable ,ordered collection of heterogenous element enclosed
in round brackets()"""
"""t=(1,2.3,'python',[1,2],(3,4),{9,9},{'a':1})
empty_tuple=()"""
#tuple with single element
"""s_t=(1,)"""
#implicit tapule creation
'''tup=1,2,3,4,6
print(type(tup))'''
#tuple input
'''l=[1,2,3]
s="python"
print(tuple(s))
print(tuple(3))
'''
#a b c d e f
"""t=tuple(input().split())
print(t,type(t))"""
#1 2 3 4 5 
"""t_int=tuple(map(int,input().split()))
print(t_int)"""
#tuple operations
#operation :*,+,in,not in,is ,is not
#bulitin functions
#min(),max(),sorted(),len(),sum()
#indexing and slicing
#same as string and list classes
#tuple methods
#count (ele)-returns the number of occurence of a particular
#ele
#index(ele)-returns the index of a particular element
#no other methods of modification are there,as tuple immutable

#immutability behaviour
"""if a mutable object exists as a tuple element ,change can be made
to that object but entire replacement of that object withn other obeject
is not supported
t=(1,[38,11,72],'python')
lst=[[1,2],[3,4]]
print(lst[0][1])"""
#tuple unpacking
"""
assigning all the elements in a tuple to variables using single line of code
t=('ram',123456,'pfs-43')
name,id_num,batch=t
print(name,id_num,batch)"""





















































































