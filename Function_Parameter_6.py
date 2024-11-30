'''Containerisation===(at the time of function it happens)it is a collection of code , when call the logic
automatically it will happend .it is a unit where we store the logic and call the  package/unit/container, it will
 automatically run the code.



---------Function(only use parameter , don't use user input)
-----Function is a  rap of code ,inside the function as a programmer we write logic here .
-------in a pr
------package/unit/container who contain the logic .
-----advantage
             .code reusability
             .code efficiency
             .less-time consuming


------------types of function----
1.inbuilt func--------those functions are provided by python ,it;s known as inbuilt func
                       ex-print(),id(),dir(), help(), eva(),input(),type()
2.user define function---------for the code efficiency and usability programmer rapup the logic in a function,
                         those func known as UDF.

-----How to define a function ?(with using 'def' (define/ defination ) keyword.
-----'def' means you start a function.
-----function has a name. def function_name():

..syntax===def function_name():
    statement/expression/logic entity
    return data
function_name()

example---def wish()
    print ('hi good morning')

...what is Parameter(variable) and arguments ?---------
 def function (Parameter):
    logic
----def func1()----parameter--------formal arguments
----fun()1------arguments---------actual arguments
    '''

# def f1():
#     print('hi good morning all')
# f1()

'''inbuilt function--give at the time of installation--use dot(.)
user define function--programmer made for own need'''

'''wap to write a addition function
def add(a,b):-------parameter(come from html)-----formal argument(at the time of function call/define)
    res=a+b
print (res)

add()-------(at the time of call)-------argument(value)----actual argument
no. of parameter given , have to give same amount of argument
'''
# def add(a,b):
#     res = a + b
#     print(res)
# add(10,20)
# add(67,9)

# def add():
#     a=int(input ('enter a num:-'))
#     b = int(input('enter a num2:-'))
#     result=a+b
#     return result----return----only see
# print(add())-------print---get a data

'''write a function check even or odd'''
# def even_odd(num):
#     if num%2==0:
#         print('Even')
#     else:
#         print('Odd')
# even_odd(7)


'''print====only show
   return===(keyword) return value'''

# def add(a,b):
#     res = a + b
#     return(res)
# add(10,20)

# def add(a,b):
#     res = a + b
#     print(res)
# add(10,20)

# def add(a,b):---------both show and return vale
#     res = a + b
#     return(res)
# print(add(10,20))


# def f3_div(n1,n2):
#     li=[]
#     for i in range(n1,n2+1):
#         if i%3==0:
#             li.append(i)
#     return li
#
# print(f3_div(1,9))


# def f():
#     li=[]
#     for i in range(1,15):
#         if i%3==0:
#             li.append(i)
#     return li
# print(f())


# def f1():
#     li=[]
#     for i in range (1,15):
#         if i %3==0:
#             li.append(i)
#     return li
# print(f1())



'''check a number pallindrom or not'''
# def pallindrom(a):
#     if a==a[::-1]:
#         print('pallindrom')
#     else:
#         print('not pallindrom')
# a = pallindrom(input('Enter a string:-'))
# print(pallindrom('mam'))




# def pallindrom(a):
#     return a==a[::-1]
# print(pallindrom('madam'))


'''
--Arguments having no. of parameter= Given same no of Argument
Types of Arguments-------thetre are 4 types of arguments in python function
 1..Positional Arguments
 2..Keyword Arguments
 3..Default Arguments
 4..Variable length of Arguments
 if you want to put both p.a and k.a, 1st put p.a then put k.a
 '''

'''1..Positional Arguments-it is the default argument in python , it will take based on parameter postion through 
 argument'''
# def sub(n1,n2):
#     res=n1-n2
#     return res
# print(sub(3,6))


# def sub(n1,n2):
#     res=n1-n2
#     return res
# print(sub(6))

# def cal(a,b,c,d):
#     sub=(a-b)+(c-d)
#     return(sub)
# print(cal(10,45,67,67))



'''2..Keyword Arguments---in calling of the function in that time we pass the parameter name and value ,
it is called keyword argument'''
# def sub(n1,n2,n3,n4):
#     res=(n1-n2)+(n3-n4)
#     return res
# print (sub(10,20,30,40))


# def sub(n1,n2,n3,n4):
#     res=(n1-n2)+(n3-n4)
#     return res
# print (sub(n3=35,n2=50,n1=40,n4=30))

# def add(b,f,h,s,k):
#     print(b,f,h,s,h,k)
# print(add(11,27,35,47,7))



'''3..Default Arguments---if you have no value then take default value------in the execution of the function 
we pass the value in parameter if in argument we  have no values bydefault functioin take the default parameter value
its called DA.'''
# def wish (name='unknown'):
#     return(f'Hi{name} uncle welcome')
# print(wish('pandey sir'))
# print (wish())

# def add(a=0,b=0):
#     res=a+b
#     return res
# print(add(10,20))
# print(add())

'''4..Variable length of Arguments--nth argument-(called star_argument)-----
    return data type =tuple
1..  *args(nth variable arguments use , it is more  imp.) return type tuple
2..   **kwargs(nth key-value variable arguments (use for dictionary)
    *=or'''


'''*args'''
# def add(*args):
#     print(args)
#     print(type(args))
# add(10,20,67,78,9,0,9,'i')

# def add_cal(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# print (add_cal(10,7,8,9))

'''**kwargs'''
# def nth_dict(**kwargs):
#     print(kwargs)
# print(nth_dict(name='g',age='45',salary='6700'))


'''add the element of list'''
# li=[1,2,3,4,5]
# sum=0
# for i in li:
#     sum = sum + i
# print(sum)

'''add the element '''
# def add(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# print(add(10,20,67,78,9,0,9))

'''multiply the element'''
# li=[1,2,3,4,5]
# def mul(*args):
#     mul=1
#     for i in args :
#         mul=mul*i
#     return mul
# print(mul(1,2,3,4,5))


'''nth number multiply'''
# num=1---------------------------------edit
# def mul(*args):
#     mul=1
#     for i in args :
#         mul=mul*i
#     return mul
# print(mul(input('enter a number:-')))


# def add(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# print(add(10,60,78,45))

'''for pass the key-value pair use **-----keyword Argument(**kwargs)'''
# def dic(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
# dic(name='Sahil',age=26,Salary=500000)


'''
Types of Variables------

1..Global Variable---access both in the function and outer of the function 
 2..Local Variable---------only call in the function, not any where else'''

'''Global Variable'''
# a=10
# def f1():
#     return f'hi{a}'
# print(f1())
# print(a)


'''Local Variable '''
# def f1():
#     a=10
#     return a
# print(f1())
# print(a)

'''convert as a global, then call '''
# def f1():
#     global a
#     a=10
#     return a
# print(f1())
# print(a)


# def  even_odd(num):
#     if num%2==0:
#         return 'it is even'
#     else:
#         return 'it is odd'
# print(even_odd(16))


'''Anonymous Function---a function have no name==Lambda function , it's a single line code
or we can say -Lambda(key-word)
..Lambda is a single line code and it have no name so it's called a annonymious function.
..Lambda used in the programme for the code optimisation 
..Syntax:-----
var=lambda parameter:statement/logic
print(var(parameter))'''


# add=lambda a,b:a+b
# print(add(10,8))

'''wap a lambda function check no is even or odd'''
# even=lambda a:a%2==0
# print(even(6))

# or
# even=lambda a:'even' if a%2==0 else 'odd'
#
# print(even(6))


# var= lambda st: 'pallindrom' if st==st[::-1] else' not a pallindrom'
# print(var('madkm'))


'''
Addition operation-----single line code
1..terenarry op.
2.list comprehension


1..terenarry op.---when we will write if & else in a single statement,this statement known as terenarry op.
It's a single statement of 'if' condition no elif is present
syntax:--
var=if_return if  condition  else else_return '''
# n=10
# var ='even' if n%2==0 else 'odd'
# print(var)


# st='madam'
# var='pallindrom' if st==st[::-1] else 'not pallindrom'
# print(var)


# li=[2,4,6,8]
# # output=[4,16,36,64]
# def square(li):
#     new_li=[]
#     for i in li:
#         new_li.append(i*i)
#     return new_li
# print (square(li))

# var= lambda st: 'pallindrom' if st==st[::-1] else' not a pallindrom'
# print(var('madkm'))


# li=[2,4,6,8]
# var= list(lambda li:i*i for i in li)-------not happening
# print(var(li))
'''2.list comprehension--------list com it is a single line code , in square  braces we are iterate 
and store the result'''

# var=[i for i in range(1,11)]
# print(var)


'''wap divisible by 5'''
# var=for i in range(1,51):-----------edit
#     if i%5==0
# print(var)

# or

# var=[i for i in range(1,50) if i%5==0]
# print(var)

'''# op=['aw','yu','ui']'''
# li=['aw',90,'yu',67,65,'ui']
# var=[i for i in li if type(i)==str]
# print(var)

# [0,1,1,2,3,5,8,13]
# li=[0,1,1,2,3,5]
# for i in range(10):
#     var=li[-1]+li[-2]
#     li.append(var)
# print(li)

# or

# fib_series=[0,1]
# [fib_series.append(fib_series[-1] + fib_series[-2]) for i in range(10)]
# print(fib_series)



# HW===OP=['A','B','C','D',..............'Z']


# Inbuilt function-----filter ,map, reduce
'''map:--
..map is a inbuilt function in Python who modify the each element in a collection help of 
functional logic.,do same change in whole function
syntax:- map(function_name, collection)
collection reach each element then modify the programme'''

# li=[2,4,6,8]
# var=list(map (lambda i:i*i,li))
# print(var)

'''op=[15,25,35,45,55,65]'''
# new_li=[]
# li=[10,20,30,40,50,60]
# for i in li:
#     new_li.append(i+5)
# print(new_li)

#or

# li=[10,20,30,40,50,60]
# n=len(li)
# for i in range(n):
#     li[i]=li[i]+5
# print(li)
#or

# li=[10,20,30,40,50,60]
# var=list(map (lambda i:i+5,li))
# print(var)

'''['Qwerty', 'Jbji', 'Bjh', 'Yugy']'''
# li=['qwerty','jbji','bjh','yugy']
# var=list(map (lambda i:i.capitalize(),li))
# print(var)

'''add5,check pallindrom'''
# li=[116,899,676,455,321,459,318]
# var=list(filter(lambda j:str(j)==str(j)[::-1],list(map (lambda i:i+5,li))))
# print(var)



'''op=['10r','20r','30r,'40r']'''
# tup=(10,20,30,40)
# var=list(map(lambda i:str(i)+'r',tup))
# print(var)


'''filter():-
..the element from a collection based on the functional logic
not modify based on the logic , only filterize
syntax=filter(function_condition,collection)'''

'''find even '''
# li=[1,2,3,4,5,6,7,8,9,10]
# var=list(filter(lambda a:a%2==0,li))
# print(var)

'''find string'''
# tu=('yu',90,8+9j,'qw',98)
# var=list(filter(lambda a:type(a)==str,tu))
# print(var)

'''check pallindrom'''
# li=[131,567,890,231,565,787,289]
# var=list(filter(lambda st:str(st)==str(st)[::-1],li))
# print(var)

'''check string'''
# li=[10,89.90,'56',901,'qwerty',True]
# var=list(filter(lambda a:type(a)==str,li))
# print(var)


'''Reduce:-------use in mathematical function,return one element/single data so ,'list' not use
from functools import reduce
Reduce---reduce(function_name,collection)'''

# from functools import reduce
# li=[10,20,30,40,50]
# var=reduce(lambda a,b:a+b,li)
# print (var)


'''add only integer value'''
# li=[10,290,67,8.89,6+8j,9+9j,'rt']
# from functools import reduce
# var=reduce(lambda a,b:a+b if type(a)==int and type(b)==int else a,li)
# print (var)

'''
what is function
parameter
how to use user define function
types of arguments
types of variables
what is lambda, and how to write
map,filter,reduce
'''

# hw----wap for mathematical operation in function(add,sub,mul,div)
# wap----check it's even or odd
'''wap find the biggest number in a list with using swaping'''

# li=[31,23,21,45,32,89,45,27]
# n=len(li)
# for i in range(n):
#     for j in range(0,n-i-1):
#         print(i,j)
#         if li[j]>li[j+1]:
#             li[j],li[j+1]=li[j+1],li[j]
# print(li)

# def largest_num(li):-------------edit
#     max=0
#     for i in li:
#         if i>max:
#             max=i
#
#
# li = [31, 23, 21, 45, 32, 89, 45, 27]
# print(max)



'''decorator'''




# 12-----------11-----------24
'''Nested Function--A function under a function is known as Nested Function and 
1st function is known as outer function and 2nd function known as inner function.
Everytime inner function is depends on the outer function'''

# def outer_function():
#     print('outer function execution')
#     def inner_function():
#         print('inner function execution')
#     inner_function()
#     print('outer function end')
#     print('inner function end')
# outer_function()


# WAP a nested function check the number is pallindrom or not , if the number is pallindrom, then check
# the number is even or odd.

'''def is_pallindrom(num):
    if str(num)==str(num)[::-1]:
        def is_even(num):
            if num%2==0:
                return 'Even and Pallindrom'
            else:
                return 'Pallindrom but not even'
        return is_even(num)
    else:
        return 'not a pallindrom'

print(is_pallindrom(121))
'''

'''WAP a Nested function take a list of integer,float and string, if string is available then reverse it 
in a inner function'''

# def fetch_string(li):-------------edit
#     string=[]
#     for i in li:
#         if type(i)==str:
#             def reverse_str(i):
#                 string.append(i[::-1])
#             reverse_str(i)
#     return string
# li=[12,'rahul',98.9,9+9j,'ketan','rajib']

# decorator--------it is a function, take the argument a exiting function modify the functionality of the
# exiting function and return the extensible functionality.


# if you have a calculator addition then you put substraction
'''def xyz(cal):
    def sub(a,b):
        res=a-b
        return res,cal(a,b)
    return sub

@xyz
def cal(a,b):
    add = a+b
    return add

print(cal(10,20))'''



# function---------take a phibonacy series and check even or odd.

# def fibo(num):
#     li=[0,1]
#     for i in range(num-2):
#         var=li[-1]+li[-2]
#         li.append(var)
#     return li
#
# @fibo
# def fibo(num):
#     num%2==0
#     return even


# print(fibo(10))



# 14------------11--------------24
# when a function called itself it's known as a recurssive function


# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))


# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(10))


# li=[9,6,3,5,2,1]
# def sum(num):
#     if len(num)<=1:
#         return 1
#     else:
#         return num[0]+sum(num[1:])
#
# print(sum(li))



# li=[9,6,'676',3,5,'75',2,'878',1]
# def sum(num):
#     if len(num)<=1:
#         return 1
#     else:
#         var=num[0] if isinstance(num[0],int) else 1
#         return var*sum(num[1:])
#
# print(sum(li))

'''Generator---------it's a function ,it will return with the help of 'yield'  the obj generate sequence wise with 
help of   'next()' , return type 'tuple' 
'''

function
parameter
argument type
variable type



terenarry op
list copm











