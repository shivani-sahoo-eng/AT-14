'''
operator(LABARS)---operator are special symbol or  keywords that help perform various operations on variables
and values.
1=Arithmetic operator
2=relational or comparison operator(used to compare values and return a boolean result)
3=logical op
4=assignment op---compound assignment op.
5=bitwise op
6=special op---(identity operator ,membership operator)'''

'''1==Arithmetic operator---(used) to perform basic mathematical operation)
+(addition)-      int+int,   int+float,   float+float,   comp+comp,  str+str
-(substraction)-  int-int,   int-float,   float-float,   comp-comp
*(multiplication)-int*int,   int*float,   float*float,   comp*comp,  str*str
/(division)-      int/int,   int/float,   float/float(everytime return datatype is  float)
//(floor division)-everytime return datatype is  integer
**(exponent-to the power)--2**3=8
%(modulo)--reminder'''
# print(10/2)
# print(10//3)
# print(10**2)---to the power
# print(10%3)---reminder

'''2==Relational or comparison operator---relationship op. compared the data between the data and return 
type always a boolean value.
1-->,>=
2--<,<=
3--!=(not equal),
4--==
print(10>=10)
print(10!=10)
print(10==10)'''

'''3==logical op(and,or,not)-its only check the conditions and return the boolean value.
# print(not False)

and---if both cond. is true then result return a True value or it's False
True   True    True
True    False   False
False   True    False
False   False   False

 # or---Atleast one condition is True , result return as True or its False
True   True    True
True    False   True
False   True    True
False   False   False

# not--just a compliment ,it will reverse True to False, False to True
# print(not False)=True
# print(not True)=False'''

'''4==assignment op---in assignment op.in  a variable data stored with
help of( = )symbol,everytime variable behave like the type of data
a=10
print(a)==variable behaviour act as a data behaviour
'''

'''compound assignment op----assignment op. working with a arithmetic op.'''
# x=10
# x=x+10
# print(x)
# a=a+1(here =,+ two types of op. are use , so it's a compound ass.op)
# a=10
# a=a+10/(a+=10)both are same
# print(a)

'''5--bitwise operator'''






'''6==special op. (identity, membership op.)
    A..identity op(both the data has same identity prof,it checks the location of the variable and compare with
another variable location, if both the location is same , the ans. should be True neither its false,
, use 'is' operator)'''
# a=10
# b=10
# print(id(a))
# print(id(b))
# print(a is b)
# print(a is not b)

'''B..membership op(in op. use)(use near collection -list,tuple,set,frozenset)
------check the data or value, its present in the specific collection or not, if the value is present the 
return type is True , if the value is not present  then it is 'False'.'''
# li=[10,20,30,40,50]
# print(10 in li)
# print(67 not in li)



'''
The style guide of python , or designing or maintain style of python is handle
 by PEP8(python enhancement proposal)
'''

'''user define variable'''
# a=10
# b=20
# res=a+b
# print(res)

'''input()---it takes the data from end user or customer in console its always takes a data as a string'''

# a=input('enter a number:-')
# print(a)
# print(type(a))

# var=input('Enter a number:-')
# var1=input('Enter a number:-')
# res=var+var1
# print(res)


'''eval=====if not known the data type it point-out'''
# var=eval(input('Enter a number:-'))
# var1=eval(input('Enter a number:-'))
# res=var+var1
# print(res)
# print(type(res))

'''typecasting---convert  one data type to a another data type with supported one only'''
# a='10'
# b=int(a)
# print(type(a))
# print(type(b))

