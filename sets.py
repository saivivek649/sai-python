#set:
'''a set is a muttable ,unordered collection of unique and immutable
elements enclosed in curly brackets'''
s={1,5.9,(1,2),'python'}
print(s)
st={1,2,3,4,2,34,1,2,3,}
print(st)
set_1={34,6,1,95}
print(set_1)
#{1,2,3,4}
print(type(set_1))
s='python'
s_set=set(s)
print(s_set)
#set operation
#operators
#in ,not in can be used
#is,is not can be used
#some operation are used for special set opeartions like union
#union opeartion -|
#it is used to get element from both the sets together 
a={1,2,3,4,4,5}
b={3,4,5,6,7,8}
print(a|b)
#intersestion-&
#it is used to get common element from both the sets
print(a&b)
#difference - -
#it is used to get element present only in fiest set
print(a-b)
#symmentric difference -^
#it is used to get element that are not common to both the set
print(a^b)
