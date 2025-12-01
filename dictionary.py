
#dictionary:
'''
dictionary is a muttable ,ordered collaction of key value pair
where key are unique, immutable and value can be of any data type
and enclosed in curly brackets'''
#obj:obj,obj_1:0
'''d={'a':1,100:'abcd',(1,2):['a','b']}
print(d)
emp_d={}
print(type(d))'''
#dictionary input
'''lst=[(1,'a'),(2,'b')]
print(dict(lst))'''
#eval()
'''print(eval('3+5'))
print(type(eval('[1,2,3,4]')))'''
'''d=eval(input('enter dictionary:  '))
print(d)
print(type(d))'''
#dictionaery operations:
'''dict_1={'a':1}
dict_2={'b':2}
print(dict_1|dict_2)'''
#in,noy in always check in keys only
'''marks ={'bob':80,'john':100,100:1}
print(100 in marks)'''
#is ,is not can be used
#builtin functions
'''n={'sai':1,'vivek':2}
print(f"{max(n)}{min(n)}")'''

#accessing values in dictionary
#values are accessed using key
'''marks={'bob':80,'john':100}
print(marks['john'])'''
#we can use key based indexing for reassigning  values also
'''marks['john']=90
print(marks)'''
#we can use this to insert new key value pairs in dictionary
'''marks['alex']=100
print(marks)'''

#dictionary class function
#method for adding new elements
#update()-adds new key value pairs at theb end of an existing dictionary
'''marks={'bob':80,'john':100}
marks.update({'lilly':75,'rose':55})
print(marks)'''
#methods for removing elements
#pop(key)
'''marks.pop('john')
print(marks)'''
#popitem()
'''marks.popitem()
print(marks)'''
#clear()
'''marks.clear()
print(marks)'''
#methods for accessing values
#marks={'bob':80,'john':100}
#get()-safer way to access using keys
'''print(marks.get('bob'))
print(marks['bob'])'''
#keys()
''''marks={'bob':80,'john':100}
print(marks.keys())'''
#values()
#print(marks.values())
#items()
'''print(marks.items())
keys = marks.keys()
values = marks.values()
print(keys)
print(values)
marks['charles']=70
print(keys)
print(values)'''
#avgreges
'''student_marks ={'physics':50,'maths':80,'english':90}
marks_lst=list(student_marks.values())
avg=sum(marks_lst)/len(marks_lst)
print(avg)
'''








































































