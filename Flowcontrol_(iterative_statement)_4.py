'''Flowcontrol---Flowcontrol and handle the logical operator
1=conditional statement(if,elif,else)
2=iterative statement(for,while)
3=transfer statement(break,continue,pass)

2......iteration----iterative statement are two types(for_loop and while_loop)

for_loop===it's a keyword in python and it's a collectional iterative statement ,it will iterate only
the collectional data type, like -string,list,tuple,set,frozenset,range ,dictionary.

while_loop=it's a keyword in python and it's a conditional iterative statement,it iterate till
condition failed, if condition is alwz true then it's a infinite loop'
'''


'''
syntax-
for variable in collection_name
    logic/statement expression
'''

# li = [12,24,778,99,9]
# for var in li:
#     # print(var)
#     print(var+5)

# li = [12,24,778,99,9]
# for i in li:
#     print(i+5)
# print(li)


# li = [12,24,778,99,9]
# new_li=[]
# for i in li:
#     new_li.append(i+5)
# print(new_li)


# li=[11,12,13,14,15,16,17,18,19]
# new_li=[]
# for i in li:
#     if i%2==0:
#         new_li.append(i)
# print(new_li)


# li=[11,12,13,14,15,16,17,18,19]
# even = []
# odd = []
# for i in li:
#     if i%2==0:
#          even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)


# st='Radfgh RTYUgh'
# upper=''
# lower=''
# for i in st:
#      if i.isupper():
#         upper=upper+i
#      else:
#         lower=lower+i
#
# print(upper)
# print(lower)


'''
range()---it's a datatype in python and it's is a function as well. generating the sequence of number
          based on user values.
range-----(start,end+1,step),by default step 1 not need to necessary
range (10,21):(it needs iteration ,without iteration not works)
'''
# for i in range (10,21):
#     print(i)

# for i in range (2,11,2):
#     print(i)

# for i in range (1,11,2):
#     print(i)

# for i in range(10):
#     print(i)

# count=0
# for i in range(10):
#     count=count+1
# print(count)



''' * ------tree structure'''



# for i in range(5):
#     print('*')

# for i in range(6):
#     print('*',end=' ')

# for i in range(1,6):
#     print('*'*i)

# for i in range(5):
#     print(((i+1) * '*'))


# for i in range(1, 6):
#     print('*'*(6-i))

# for i in range(1,6,2):
#      print('*'*(6-i))


# for i in range(5):
#        print(' '*(i)+'*'*(5-i))

# or

# for i in range(1,6):
#      print(' '*(i-1)+'*'*(6-i))

# for i in range(5):
#       print(' '*(4-i)+'*'*(i+1))

# or

# for i in range(5):
#       print(' '*(4-i)+'*'*(i+1))

'''
op=====    *--------------edit
          * *
         * * *
        * * * *
       * * * * *
'''



'''100-201 check how many pallindrom'''
# for i in range(100,201):
#     st = str(i)
#     if st == st[::-1]:
#         print(i)

# 100-201=check the numbers howmany hava last digit 9
# for i in range(100,201):
#     st = str(i)
#     if st.endswith('9'):
#         print(i)

'''separate each datatype and store other collection or list'''
# li=[10,89,78,90.9,'gh','ghj',[8,9,67,45],(67,78),[11,78,78],(78,56,78)]
#
# integer=[]
# float1=[]
# complex1=[]
# li1=[]
# string=[]
# tupl=[]
# for i in li:
#     if type(i)==int:
#         integer.append(i)
#     elif type(i)==float:
#         float1.append(i)
#     elif type(i) ==complex:
#         complex1.append(i)
#     elif type(i) == list:
#         li1.append(i)
#     elif type(i) == str:
#         string.append(i)
#     else:
#         tupl.append(i)
# print(integer)
# print(float1)
# print(complex1)
# print(li1)
# print(string)
# print(tupl)



'''range(100,1000),check how many number are divisible by both 3 and 5, print the numbers'''
# li=[]
# for i in range(100,1001):
#     if (i%3==0 and i%5==0):
#         li.append(i)
# print(li)
# print(len(li))




'''
--------------------------------count'''
# li=[]
# count = 0
# for i in range(100,1001):
#     if i%3==0 and i%5==0:
#         li.append(i)
#         count=count+1
# print(li)
# print(len(li))
# print(count)

# li1 = [10,20,30,40,50,60]
# sum = 0
# for i in li1:
#     sum = sum+i
# print(sum)

# li=[[10,20],[30,40],[67,90,54,23],[25]]
# for i in li:
#     print(i)


# li=[[10,20],[30,40],[67,90,54,23],[25]]
# for i in li:
#     for j in i:
#         print(j)

# li=[[10,20],[30,40],[67,90,54,23],[25]]
# sum= 0
# for i in li:
#     for j in i:
#         sum=sum+j
# print(sum)

# li=['Anup','Archana','Subhashis','Shivani','Martha']
# st=''
# for i in li:
#     for j in i:
#         st=st+j
# print(st)

# li=[[10,20],89,91,[56,78]]
# sum=0
# for i in li:
#     if type(i)==list:
#         for j in i:
#             sum=sum+j
#     else:
#         sum=sum+i
# print(sum)


'''21--------10---------2024'''

'''1. reverse a string without using func or slicing.'''
# op='ytrewq'

# st='qwerty'
# new_st=''
# for i in st:
#     new_st =i+new_st
# print(new_st)


'''2.i have a string, from use input, count the length of the string without using inbuilt function
 and slicing.'''
# len=0
# user=input('enter a string:- ')
# for i in user:
#         len=len+1
# print(len)

'''3. i have a string, from use input, count how many vowels in a string without using inbuilt function and
slicing.'''

# count=0
# user=input('enter a string:- ')
# vowels='aeiouAEIOU'
# for i in user:
#     if i in vowels:
#         count= count+1
#         print(i)
# print(count)




'''5.i have a string , find  out the digit and print sum'''
# st='Ok, Hello, 123,yes,89 @,rt&^7vh$%^4354'
# digit=''
# for i in st:
#     if i.isdigit():
#         digit=digit+i
# print(digit)
# sum=0
# for i in digit:
#     var=int(i)
#     sum=sum+var
# print(sum)

'''22-------10-------2024'''

# li=['Rajesh','Mahesh','Suresh']
# for i in li:
#     print(i)


'''nested loop'''
# for i in range(1,6):
#     print(i)

# for i in range(1,6):
#     for j in range(1,6):
#         print(i,j)

# li=['Rajesh','Mahesh','Suresh']
# for i in li:
#     for j in i:
#         print(i,j)

# li=[[10,11,13],[12,15,18],[90,23,42]]
# for i in li:
#     for j in i:
#         if j%2==0:
#             print(j)

# op=collect all the string and save in a list using isinstance
# li=[['qwerty',12,89],[78.90,67,'rt','Vamshi'],['ty',90]]
# new_str=[]
# for i in li:
#     for j in i:
#         # if type(j)==str:
#         if isinstance(j,str):
#             new_str.append(j)
# print(new_str)


'''op=[10,30,11,12,34,56,67,89]-----------------edit'''
# li=[10,30,[11,12],[34,56],67,89]
# new_li=[]
# for i in li:
#     for j in i:
#
#         if isinstance(i,list):
#             new_li.append(i)
#         else:
#             new_li.append(j)
#             var=int(j)
# print(new_li)

'''
li_dict = [
    {'Name':'A','Age':21,'Salary':'67000','Subjcet':['Python','C++','SQL'],'MName':'Ragav'},
    {'Name':'B','Age':23,'Salary':'78000','Subjcet':['Python','Java','Java Script'],'MName':'Ragav'},
    {'Name':'C','Age':32,'Salary':'120000','Subjcet':['SQL','Java','C#'],'MName':'Sachin'},
    {'Name':'D','Age':28,'Salary':'98000','Subjcet':['SQL','Java','R'],'MName':'Sachin'},
    {'Name':'E','Age':34,'Salary':'140000','Subjcet':['Python','R','Golang'],'MName':'Ragav'} 
]'''

# manager=raghav--name, age ,salary

# for i in li_dict:
#     if 'Python' in i['Subjcet']:
#         print(i['MName'])


# for i in li_dict:
#     if i['MName']=='Ragav':
#         print(i['Name'])
#

# for i in li_dict:
#     if 'Python' in i['Subjcet']:
#         print(i['Name'])

# for i in li_dict:
#     if 'Python'  and 'Java' in i['Subjcet']:
#         print(i['Name'])




data_di=   {
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://reqres.in/img/faces/10-image.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
 "avatar": "https://reqres.in/img/faces/11-image.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }
    ],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}

# for i in data_di['data']:
#     if i['id']==8:
#         print(i['email'])


'''first with help of ['data_di']fetch the value and get a list
fetch the data with di(data) and store in a list,then fetch  email 
then email get string  format 
store the email in var
split the email with using .separator
with the zero index add the name
set default
'''



'''
...While Loop-------'while' is a keyword .it's used in conditional statement based on the condition  it will
continue the iteration, if the condition will fail , iteration stop.'''

# while True:
#     print('offer letter')



'''while
print 1 to 10'''

# num=1
# while num<=10:
#     print(num)
#     num=num+1

'''add next  to next digit'''
# num=1
# sum=0
# while num<=10:
#     print(num)
#     sum=sum+num
#     num=num+1
# print(sum)




