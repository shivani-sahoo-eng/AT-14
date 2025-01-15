'''Flowcontrol---Flowcontrol and handle the logical operator
1=conditional statement(if,elif,else)
2=iterative statement(for,while)
3=transfer statement(break,continue,pass)
'''

'''conditional statement(if,elif,else)
if--if the condition is 'True' then the statement will execute,if the condition is 'False' then nothing
 will execute.
'''
# num=int(input('Enter a number:-'))
# if num%2==0:
#     print('Even')

# li=[89,72,23,45,12]
# if 23 in li:
#     print('23 is in list')

# age=int(input('Enter a number:-'))
# if age>=18 and age<=60:
#     print ('Allowed')

# time=int(input('Enter a time:-'))
# if time==6 or time==9:
#     print('booked')


# st=input('Enter a  string:-')
# if st==st[::-1]:
#     print('pallindrom')


'''debug--it's a process to check each and every point in your programme we can analyse step-to-step execution
from start point to endpoint , its looks like step-to-reproduce.
'''
# a='madam'
# if a==a[::-1]:
#     print('pallindrom')

'''String can convert in any data type'''

# var = input('Enter a num:-')
# print(type(var))

# var = int(input('Enter a num:-'))
# print(type(var))

# var = float(input('Enter a num:-'))
# print(type(var))

# user_num=int(input('Enter a num:-'))
# st_num=str(user_num)

'''else----------it's a keyword in python and it's have no conditions, it's fully depend upon the 'if' 
                 condition, incase 'if' condition was failed , then 'else' will execute.
--------------when 'else' use in multi conditions, 'else' is execute when all the condition was failed.
'''
# a=int(input('enter a number:-'))
# if a%2==0:
#     print('even')
# else:
#     print('odd')


# a=int(input('enter a number:-'))
# if a%2==0 and a%3==0:
#     print('divisible by 2 & 3')
# else:
#     print('not divisible')



'''if-elif(else-if)-else ----multiple condition'''

# a=int(input('enter a number:-'))
# if a%2==0 and a%3==0:
#     print('div by 2 and 3')
# elif a%2==0:
#     print('div by 2')
# elif a%3==0:
#     print('div by 3')
# else:
#     print('not div by both')



'''location=input('Enter your location where to go:- ')'''

# if location=='Hyd':
#     print('attain your marriage')
# elif location=='Pune':
#     print('Darshan Siridi Sai')
# elif location=='Indore':
#     print('Darshan Mahakaleswar')
# else:
#     print('enjoy in Blr')


# num= int(input('Enter a num:- '))
# if num%2==0:
#     print(f'{num} divisible by 2')
# elif num%3==0:
#     print(f'{num} divisible by 3')
# elif num%2==0 and num%3==0:
#     print(f'{num} both divisible by 2 and 3')
# else:
#     print(f'{num} not divisible by anyone')


# percentage= int(input('Enter a percentage:- '))
# if percentage >=60:
#     print('1st division')
# elif percentage <60 and percentage>=45:
#     print('2nd division')
# elif percentage>=30 and percentage>45:
#     print ('3rd division')
# else:
#     print('failed')

'''1.Even or Odd:---- Write a program that checks if a given number is even or odd using if-elif-else 
statements.'''
# num =int(input('Enter a num:-'))
# if num%2==0:
#     print(f'{num}even')
# else:
#     print(f'{num}odd')

'''2.Grading System:------ Write a program that takes a student's score and outputs their grade using the
 following conditions.
Score >= 90: Grade A
80 <= Score < 90: Grade B
70 <= Score < 80: Grade C
60 <= Score < 70: Grade D
Score < 60: Grade E'''

# score=int(input('enter your score:-'))
# if score>=90:
#     print('Grade A')
# elif score>=80 or score>90:
#     print('Grade B')
# elif 70 <= Score or Score < 80:
#     print('Grade C')
# elif 60 <= Score or Score < 70:
#     print('Grade D')
# else:
#     print('Grade E')



# a=int(input('enter a number:-'))
# if a%2==0 or a%3==0:
#     print('not div by either 2 or 3')


'''Nested-if function '''

# Train=60
# Monday  :- 15 seats booked the rest are 45 seat available
#             you can book 5 seats, and return result how many available
# Tuesday :- 30 seat booked, the rest are 30 seat available
#             you can book 10 seats,return result how many available
# Wednesday :-60 seat booked the rest is 0
#            1 seat booked, return no seat available

'''total_train_seat=60
days=input('enter your days name:-')
if days=='Monday':
    avl_seats = total_train_seat-15
    print(f'Avl seats are:-{avl_seats}')

    booking_no_of_seats=int(input('enter how many seats you wants'))
    if booking_no_of_seats<=avl_seats:
        avl_seat = avl_seats-booking_no_of_seats
        print(f'After book the avl seats are in Monday:-{avl_seats}, and booking is :-{booking_no_of_seats}')
    else:
        print(f'seat is not avl')
elif days == 'Tuesday':

    avl_seats == total_train_seats-30
    print(f'Avl seats are:-{avl_seats}')
    booking_no_of_seats = int(input('enter how many seats you can  wants'))
    if booking_no_of_seats <= avl_seats:
        avl_seat = avl_seats - booking_no_of_seats
        print(f'After book the avl seats are in Tuesday:-{avl_seats},and booking is :-{booking_no_of_seats}')
    else:
        print(f'seat is not avl')

elif days== 'Wednesday':
    avl_seat=total_train_seat-60
    if avl_seat==0:
        print('Wednesday seats are not avl')
    else:
        booking_no_of_seats = int(input('Enter how many seats you can wants'))
        avl_seats= avl_seat-booking_no_of_seats
        print(avl_seats)'''



# if your age is 15-25:
#     then marks of 12th
#     if more than 85% then science
#     70%--com
#     45%--arts
#
# if your age is 25-45
#     the salary:-
#     if more 1 lakh--buy Xuv700
#     if more than 2 lakh--buys Innova
#     if more than 3 lakh--Wranghler

# if your age is more 45
#     take care of your family



'''age=int(input('enter your age:-'))

if age>=15 and age<25:
    marks=int(input('put your 12th marks'))
    if marks>=85:
        print('science')
    elif marks>=70:
        print('com')
    elif marks>=45:
        print('Arts')
    else:
        print('rest are try again')


elif age>=25 and age<45:
    salary=int(input('enter your monthly salary'))
    if salary>=3:
        print('Wrangler')
    elif salary>=2:
        print('Innova')
    else:
        print('Xuv700')

else:
    print('take care of your family')'''




'''separate each datatype and store other collection or list'''
# st='shivani108@gmail.com'
# char=''
# digit=''
# sp_ch=''
#
# for i in st:
#     if i.isdigit():
#         digit+=i
#     elif i.isalpha():
#        char+=i
#     else:
#         sp_ch+=i
#
# print(char)
# print(digit)
# print(sp_ch)

'''i have a string, some upper, lower, digit and special char want to separate them.'''
# st=('Ok, Hello, 123,yes,89 @,rt&^7vh$%^4354')
# upper=''
# lower=''
# digit=''
# special_char=''
# for i in st:
#     if i.isupper():
#         upper=upper+i
#     elif i.islower():
#         lower=lower+i
#     elif i.isdigit():
#         digit=digit+i
#     else:
#         special_char=special_char+i
# print(upper)
# print(lower)
# print(digit)
# print(special_char)






