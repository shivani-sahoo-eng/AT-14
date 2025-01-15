'''///////////////////////////'string'
1..string is a collection of substring--------------imp.(get raw data)
2..it enclosed with ''
string----------;important
dictionary      ;
range           ;
list----------- ;

string addition and string multiplication
1-string add with a string only---------(st+st)
print('fg'+'hj')
2-string don't multiply with string but multiply with integer--------(st*int)
'''



# a=10
# print(type(a))
# a=10
# print(dir(a))........check method
# a=10.9
# print(type(a))

# a=true
# print(type(a))
# a=True
# print(type(a))


'''//////////////////////////////////////////string........'''
# s='a'
# print(type(s))
# s='abkljh'
# print(type(s))
# s=''
# print(type(s))
# s=str()......empty
# s1='empty'
# print(type(s1))
# s2='asdfghjkgh'
# print(type(s2))
# s3="asdfghjkgh"
# print(type(s3)
# s4='''asdfghjkgh'''
# print(type(s4))

'''st+st,st*int'''
# st='ty'
# st1=7
# st2='gh'
# print(st*st1)
# print(st+st2)

'''data  structure---collection of data type.
collection-----------store the data type in a collection
example..------------list,tuple,set,frozenset,bytes,bytes-array,range,dictionary'''


# st='sdfgh'
# print(type(var))

# ''' '''=doc string (documentation of string)--------multiline comment------describe about the function
# or class


# st='qwerty'
# print(type(st))
# print(dir(st))

'''[ 'capitalize', 'count','endswith', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit',
 'isascii', 'isdecimal', 'lower', 'lstrip','replace', 'rsplit', 'rstrip', 'split', 'splitlines', 'title', 
 'islower', 'isnumeric', 'isupper', 'join', 'startswith', 'strip',  'swapcase','translate', 'upper']'''


'''capitalize'''
# var='qwerty'
# print(var.capitalize())

'''count...count each specific element accurance'''
# st=('i love india, india is best')
# print(st.count('i'))

'''startswith and endswith'''
# st='yes i have'
# print(st.startswith ('y'))
# print(st.endswith ('e'))


'''find(if not present then send the -1 value) and index send  value error:substring not found'''
# st='india is a best country'
# print(st.find('is'))
# print(st.index('is'))
# print(st.find('z'))
# print(st.index('z'))


'''format(f string = if you miss something),place holder{} use variable only'''
# a=10
# b=20
# result=a+b
# print(f'addition {a} and {b} the result is : {result}')


'''upper and lower'''
# var='FGHJtyu'
# print(var.upper())
# print(var.lower())


'''swapcase.....upper to lower/ lower to upper'''
# st='FGHJtyu'
# print(st.swapcase())


'''replace'''
# st='ji jacky'
# print(st.replace('j' ,'h'))
# # print(st.replace('ji','hi'))

''' 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper'
......is= return  boolean value(T/F) use for validation ,qs true/false   answer is yes/no'''

'''isalnum'''
# st='34567'
# print(st.isalnum())


'''isalpha' &  'isdigit'''
# st='Vgvh6768567*/&^&*'
# char=0
# digit=0
# spl_char=0
# for i in st:
#     if i.isalpha():
#         char=char+1
#     elif i.isdigit():
#         digit=digit+1
#     else:
#         spl_char=spl_char+1
# print(f'char:{char}')
# print(f'digit:{digit}')
# print(f'spl_char:{spl_char}')




'''strip=rstrip,lstrip...remove white space from left and right'''
# st='india is a best country     '
# print(st.lstrip(''))
# print(st.rstrip(''))


# st='        fgh       '
# print(st.lstrip())
# print(st.rstrip())
# print(st.strip())


'''split.....is a separator of the string,it takes by default space,otherwise point-out which separator you
want ,/*& (like this)
collection=====store,it will encapulate the data by default separator ','
'''

st='Ramesh@ Suresh@  Mahesh@'
# print(st.split())
# print(st.split('@'))

'''join...list of sub-string  convert complete string,'',' ', whatever you give it separate list'''
# li=['Ramesh','Suresh','Mahesh']
# print('*'.join(li))





'''///////////////////////////////list[]
# li=[21,67.90,7+9j,'qwerty',[78,90],{78,9},None,10,10]
# print(type(li))

1-List is a collection and behave like hetrogenus (allow all type of data inside) obj. type
2-allowed duplicate char.(allow  duplicasy)
3-List is enclosed with [] and every element separate with another element help of ','
4-List is growable in nature(mutability-change the elements of data collection)(can delete,add,manupulate)
5-it follow index(position is important)
6-it is slower'''


# li=(12,56,78)
# print(li)

# li=[1,2,7,8]
# print(type(li))
# print(li[0])
# print(li)
# var=[1,2,7,8,'dfgh,hj',[5,8,0],True,22.2]


# print(dir(li))
''' ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']'''

'''append------------add a single element last position of list'''

# li=[1,2,7,8]
# li.append(676)
# print(li)
# li.append([78,909,9])
# print(li)

'''clear------------- all the elements from the list and return a empty list'''
# li=[67,89,556,4,67]
# li.clear()
# print(li)

'''copy=one data/file copy to another file'''
# li=[1,2,3]
# qw=li.copy()
# print(qw)

'''count-----------count each  element accurance'''
# li=[32,43,5,32,43,5,987,0]
# print(li.count(5))

'''extend-2nd list data(replica) come to 1st list vise-versa'''
# li1=[67,89,556,4,67]
# li2=[34,67,12,34]
# li1.extend(li2)
# print(li1)
# li2.extend(li1)
# print(li2)


'''index---------position----------if element is not present then send the value-error: substring not found'''
# li=[32,43,5,32,43,5,987,0]
# print(li.index(3))

'''insert---add a single element in a specific position'''

# li=[32,43,5,32,43,5,987,0]
# li.insert(0,'jj')
# print(li)


'''pop-remove last element'''
# li.pop()
# print(li)

'''remove-----delete specific element from list'''
# li=[23,7,9,00,7,8]
# li.remove(7)
# print(li)


'''reverse= reverse entire list of all elements'''
# li=[2,556,7,9,0,6]
# li.reverse()
# print(li)

'''sort=ascending to descending order'''
# li=[4,8,9,7,8,3,0]
# li.sort()
# print(li)

'''sort=descending to ascending'''
# li=[4,8,9,7,8,3,0]
# li.sort()
# li.reverse()
# print(li)

# or

'''sort=descending to ascending'''
# li=[4,8,9,7,8,3,0]
# li.sort(reverse=True)
# print(li)






'''//////////////////////////////tuple....allow  duplicacy'''
# tuple1=(21,67.90,7+9j,'qwerty',[78,90],{78,9},None,10,10)
# tuple2=21,67.90,7+9j,'qwerty',[78,90],{78,9},None,10,10
# print(type(tuple2))

'''
1-tuple is a hetrogenus obj. type
2-tuple allowed duplicate char.
3-tuple is enclosed with (),separate with ','
4-tuple is not growable in nature(immutability-can't change the elements of data collection)(can not delete,
  add,manupulate)
5-it follow index
6-it is faster
7-only having two methods(count,index)'''

# var=[1,2,7,8,'dfgh,hj',[5,8,0],True,22.2]
# print(type(var))

# var=(1,2,7,8,'dfgh,hj',[5,8,0],True,True,22.2,22.2)
# print(type(var))

'''tuple has only 2 methods 'count' and 'index' ,they cant modify the data'''
# tu=(12,23,45)
# print(dir(tu))


'''index---------position----------if element is not present then send the value-error: substring not found'''
# tu=[32,43,5,32,43,5,987,0]
# print(tu.index(3))


'''count...count each specific element accurance'''
# st=('i love india, india is best')
# print(st.count('l'))



'''/////-------------------------set{}---------------
1-enclosed with{}
6-not hetrogeneous 
8-it is homogeneous
2-not allow duplicate char
3-not following indexing
4-only allow unique value
5-mutable data type
7-use mathematics'''

# var={1,2,7,8,'dfgh,hj',[5,8,0],True,True,22.2,22.2}
# print(type(var))....set don't allow

# set={11,7+9j,9.99,True}
# print(type(set))
# print(set)

# set={11,7+9j,9.99,True,True,11}.....set dont allow duplicates
# print(type(set))
# print(set)

# set={11,7+9j,9.99,True,True,(55,88,99,9),11}....it contain tuple
# print(type(set))

# set={11,7+9j,9.99,True,True,[22,4,9.9],11}.....it do not contain list
# print(type(set))

# print(dir(se))
''' ['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
'symmetric_difference_update', 'union', 'update']'''

'''clear-----------return value 'None' '''
# se={12,56,78,90}
# print(se.clear())

'''copy'''
# se={12,56,78,90}
# se1=se.copy()
# print(se1)

'''difference'''
# se={12,56,78,90}
# se1={12,11,56,98}
# se3=se.difference(se1)
# se4=se1.difference(se)
# print(se3)
# print(se4)

'''intersection----------common in both set'''
# se={12,56,78,1,90}
# se1={1,2,3}
# se2=se.intersection(se1)
# se3=se1.intersection(se)
# print(se2)
# print(se3)

'''union----------merge both set and keep in a single set'''
# se={12,56,78,90,1}
# se1={1,2,3}
# se2=se.union(se1)
# se3=se1.union(se)
# print(se2)
# print(se3)

'''discard
update
isdisjoint
issubset
'''






'''frozenset
type casting==================modification
frozenset not made but modify'''
# a=[11,667,89]
# b=frozenset(a)
# print(b)
# print(type(b))


'''bytes-------output are on ASCII value'''
# li=[]
# by=bytes(li)
# print(by)

# li=[0,233,212,255,256]
# print(bytes(li))


'''bytearray-------------output are on ASCII value'''
# a=[29,90,255,89]
# b=bytearray(a)
# print(b)
# print(type(a))

# a=[29,90,257,89]..ASCII value contain (0-256) so it not accept 257
# a=bytearray(a)
# print(a)
# print(type(a))


'''None'''
# def f1():
#     a=10
# print(f1)
# print(f1())


'''range......................generate indexing  number sequence---------imp.'''
# var=range(1,10)
# print(var).......no result

# range(1,10)
# for i in range(1,10):
#     print(i)

# range(1,16)
# for i in range(1,16):
#     print(i)

# range(6)
# for i in range(6):
#     print(i)








'''///////////position in python=index(+ve(0,1,2,...)(L-R),-ve(-1,-2,....),(R-L)) json=0 base index

..slicing(create a unique number )---------------variable[start:end+1:steps]'''

# st='Banglore'
# print(st[0:4:1])
# print(st[0:4:])
# print(st[3:8:])
# print(st[3:])

# st='i love india'
# 1-india
# 2-lv n
# print(st[-5:12:])/print(st[7:12:])
# print(st[-10:-3:2])/print(st[2:9:2])

# name='Bhubanesh'
# dob='01/01/1996'
# password=name[0:4]+dob[-4:]
# print(password)

# st='qwerty'
# # op='ytrewq'
# print(st[::-1]).....imp

'''st = 'India is best, good to go'

1. best(both postitive and negetive)
2. good to go (both postitive and negetive)
3.India((both postitive and negetive))
4.best, go((both postitive and negetive))-------------edit
5.Idai(both postitive and negetive)'''




# st = 'India is best, good to go'
# print(st[9:13:])
# print(st[-16:-12:])

# 2- print(st[15:25:])
# print(st[-10:])

# 3-print(st[:5:])
# print(st[-25:-20:])

# 5-print(st[0:7:2])
# print(st[-25:-18:2])







'''/////////dictionary{}---key(column) and value(row) pair------------------imp.
1-enclosed with {} bracket
2-it is key and value pair
3-key and value separate with':'
4-one key value pair separate with another key value pair with help of ','
5-key is always unique ,value may be same
6-always key is immutable data type and value is both mutable and immutable data type'''

# di={['Name']:'A','Age':'27','Salary':'85k'}
# print(type(di))

# di={'Name':'A','Age':'27','Salary':'85k','lang':['java,python']}
# print(type(di))
# print(di)

'''json(java script)=python dictionary
in 'api' data put in backend, data store in 'dictionary'
empty {}=only show in dictionary not set
set.empty=empty set function'''

# di={'Name':'A','Age':'27','Salary':'85k','lang':['java,python']}
# print(dir(di))
'''['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']'''

'''clear'''
# di={'Name':'A','Age':'27','Salary':'85k','lang':['java,python']}
# di.clear()
# print(di)



'''copy'''
# di={'Name':'A','Age':'27','Salary':'85k','lang':['java,python']}
# di1=di.copy()
# print(di1)

'''get'''
# di={'Name':'A','Age':'27','Salary':'85k','lang':['java,python']}
# print(di.keys())
# print(di['Age'])

# di['Age']=29
# print(di)
# print(di.get('Age'))

'''items'''
# di={'Name':'A','Age':'27','Salary':'85k','lang':['java,python']}
# print(di.items())


'''keys'''
# di={'Name':'A','Age':'27','Salary':'85k','lang':['java,python']}
# print(di.keys())


'''pop===remove particular key'''
# di={'Name':'A','Age':'27','Salary':'85k','lang':['java,python']}
# di.pop('lang')
# print(di)

'''popitem===remove last popitem'''
# di={'Name':'A','Age':'27','Salary':'85k','lang':['java,python']}
# di.popitem()
# print(di)

'''setdefault===add a new data'''
# di={'Name':'A','Age':'27','Salary':'85k','lang':['java,python']}
# di.setdefault('Manager','BCD')
# print(di)

'''update'''
# a={'Name':'A','Age':'27'}
# b={'Salary':'85k','lang':['java']}
# a.update(b)
# print(a)


'''values'''
# di={'Name':'A','Age':'27','Salary':'85k','lang':['java,python']}
# print(di.values())



# def f1():
#     a=10
#     print(f1())

'''memory(heap,stack)
heap-  only one variable store, store variable, no size,no iteration
array---list , array different
list[]=homogeneous, use data store, check programme,slower
array[]=homogeneous, use at data analysis,faster'''

'''def is_even_odd(num):
    if num%2==0:
        return 'even'
    else:
        return 'odd'
print (is_even_odd(11))'''

'''def is_pallindrom(str):
    if str==str[::-1]:
        return 'pallindrom'
    else:
        return 'not pallindrom'
print (is_pallindrom('madam'))'''

st='qwerty'
new_st=''

for i in st:
    new_st=i+new_st









