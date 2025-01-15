'''Flowcontrol---Flowcontrol and handle the logical operator
1=conditional statement(if,elif,else)
2=iterative statement(for,while)
3=transfer statement(break,continue,pass)'''

'''3.transfer statement-------
......break------it's a keyword in transfer statement, based on the condition it will break the iteration 
(loop), once loop will break , it will stop the iteration and its not iterate again.'''

# for i in range(1,11):
#     if i == 7:
#         break
#     print(i)

# li=['Rajesh','Mahesh','Suresh','Kalpesh','Gopi','Rohit','Bana Bihari', 'bikash','Paresh']
# for i in li:
#     if i=='Rohit':
#         break
#     print(i)

# for i in range(5):
#     for j in range(5):
#         if j==3:
#             break
#         print(i,j)

# for i in range(5):
#     for j in range(5):
#         if i==3:
#             break
#         print(i,j)



'''continue--------(skip):-continue is a keyword of transfer statement, based on that condition it will skip 
the iteration.'''

# for i in range(1,11):
#     if i%2==0:
#         continue
#     print(i)

# li=['Rajesh','Mahesh','Suresh','Kalpesh','Gopi','Rohit','Bana Bihari', 'bikash','Paresh']
# for i in li:
#     if i.endswith('esh'):
#         continue
#     print(i)

# li=[90,89.89,6+9j,True,'String',12]
# for i in li:
#     # if type(i)!=int:
#     if type(i)== int:
#         continue
#     print(i)


# for i in range(7):
#     if i==3 or i==6:
#         continue
#     for j in range(5):
#         if j==5:
#             break
#         print(i)
#         print('treenetra')



# for i in range(7):
#     if i==3 or i==6:
#         continue
#     for j in range(5):
#         if j==1:
#             break
#         print(i,j)
#         print('treenetra')

# for i in range(7):
#     if i==3 and i==6:
#         continue
#     for j in range(5):
#         if j==1:
#             break
#         # print(i,j)
#         print('treenetra')


# for i in range(7):
#     if i==3:
#         break
#     for j in range(5):
#         if j==5:
#             break
#         print(i,j)
#         print('treenetra')

# for i in range(7):
#     if i==3:
#         break
#     for j in range(5):
#         if j==-1:
#             break
#         # print(i,j)
#         print('Treenetra')





''' pass -------------- when you have  no statement to execute in this time in statement we pass the 'pass' 
keyword for avoiding indentation error to remove error and pass the function.
for i in range(1,11):-------if having no value, it's not seems error, and not provide any error

i====consider a key'''

# for i in range(5):
#     def f1():
#         pass



# di={'Name':'Martha','Age':89,'Salary':567890}
# for i in di:
#     print(i)

# di={'Name':'Martha','Age':89,'Salary':567890}
# # return value in tuple
# for key,value in di.items():
#      print(key,value)


li=[
{'Name':'ABC','Age':21,'Salary':890000,'Subject':['Python','Java']},
{'Name': 'EFG', 'Age': 26, 'Salary': 960000,'Subject': ['Python','C++']},
{'Name': 'XYZ', 'Age': 23, 'Salary': 91000,'Subject': ['Sql', 'R']},
{'Name': 'PQR', 'Age': 28, 'Salary': 99000,'Subject': ['Python', 'R']}
]

'''1-check how much salary have get name xyz
2- Check the total salary of the candidates
3-fetch the name who have mora than 25 in age
4-check how many candidates work in Python
5-Fetch the name who have both python and java'''

# 1..for i in li:
#     for k,v in i.items():
#         if k=='Name' and v=='XYZ':
#             print(i.get('Salary'))

# 2..total_salary =0
# for i in li:
#     total_salary = total_salary+ i.get('Salary')
# print(total_salary)


#3.. for i in li:
#     for k,v in i.items():
#         if k=='Age' and v>25:
#             print(i.get('Name'))


# 4..for i in li:
#     for k,v in i.items():
#         if k=='Subject' and 'Python' in v:
#             print(i.get('Name'))


# for i in li:-----------------edit
#     for k,v in i.items():
#         if k=='Subject' and 'Python' and 'java' in v:
#             print(i.get('Name'))


'''li=[
    {'Name':'A','age':26,'salary':56000},--------------edit
    {'Name':'B','age':23,'salary':78000},
    {'Name':'C','age':24,'salary':91000},
{'Name':'D','age':21,'salary':67000},
{'Name':'E','age':27,'salary':56000},
]


3-COUNT above 25 age sum the salary
'''

di={
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
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
    }
}



'''for i in di.get('data'):
    print(i)
'''

'''for i in di.get('data'):
    if i.get('id')==8:
        print(i.get('first_name'))
'''

'''id_8_li=None
id_9_li=None
for i in di.get('data'):
    if i.get('id')==8:
        print(i.get('avatar').split('/'))

for i in di.get('data'):
            if i.get('id') ==9:
                print(i.get('avatar').split('/'))

print(id_8_li)
print(id_9_li)

# id -8----------------------------------edit
for i in id_8_li:
    if i not in id_9_li:
        print(i)

# id -9
for i in id_9_li:
    if i not in id_8_li:
        print(i)

'''












