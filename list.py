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





































































































