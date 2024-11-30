'''.Module is a python file who contains functions,variables and classes.,based on the requirement a
Python file called   another Python file with help of the import keyword.
.benefit------------re-use the  another file functionalities as per requirement.
.Types of module----THere are 2 types of module in python
                            1. inbuilt module,
                            2. user define module

. module
1-math
2.os
3.sys
4.random
5.datetime
6.time
7.json
8.collection
9.iter tools
10.sub-process(netmiko,paramiko)
11.urllib'''

'''MATH MODULE'''
import math

'''sqrt'''
# result=math.sqrt(16)
# print(result)

'''pow'''
# result=math.pow(2,3)
# print(result)

'''floor'''
# result=math.floor(4.7)
# print(result)

'''fabs----- use in networking '''
# result=math.fabs(-7)
# print(result)

'''factorial'''
# result=math.factorial(5)
# print(result)

'''gcd---greatest common divisible'''
# result=math.gcd(24,12)
# print(result)

'''lcd----lowest common divisible'''
# result=math.lcd(24,12)
# print(result)

'''pi'''
# result=math.pi
# print(result)

'''sin,cos,tan'''
# result=math.sin(45)
# print(sin_res)

'''sin2+cos2==1
tan=sin/cos'''

# 23------10------2024
'''packages---it is a directory contain init file and some python file    as well, inside a package we declare
 another package as well.
3 types--------
.inbuilt package--when python install based on that requirement,it will be share some folder structure and important
 files known as inbuilt packages.

.user define packages--

.library--is a outside package,with the helpo of the PIPO we will install in our local system or server or cloud.



..init----initialisation
file name===_ _init_ _.py
it's just a python special file, that is used to mark a directry as a package.
executing-----This file to execute initialisation code when the package was imported.
'''

# 25---------10-----------2024

'''
# PACKAGES

Text file handling
binary file handling

.mode -r
.method---read, readline, read-lines,close
variable-closed

.read method used-in in 'r' mode. its read all the data from a file and store a another variable
.read-line

.escape character--
\n------newline
\t------tab
\r------carriage(no space)
\b------back space
\'-------

.readlines-----it's return a list of string ,each line becoming a sub-string, eachline separate with another line
with of',', eachline ends with '\n'

.read mode used for only read the file if file is not exit in same path or given path ,then its rise a
FileNotFoundError.


.----mode--write and append
.write mode stands for 'w' ,'a'
.method----write, writelines

'''

# 06----------11-----------2024

'''with statement------with statement used to open the file and close the file automatically. In with statement
 we will handle multiple file operation 
syntax-=with open (file path, mode) as file


'''
# .Json. .CSV, .XLsx

'''
serialisation----it is the process of  converting a python object into a format that can be easily store 
and transmitted such as convert in a json file.

de serialisation--------it is the process of converting a json string to python object .
'''

'''what is CSV (comma separated value) ?



------------check  openxl 
'''

# 14------------------11-----------2024

'''PANDAS LIBRARY---its a outer library in python, it will be basically used for create the data frame 
and handle the CSV and EXCell.



/Users/macos/PycharmProjects/TREENETRABATCH/.venv/bin/python /Users/macos/PycharmProjects/TREENETRABATCH/BatchCodeData/TREENETRA_AT_13/ApiJson/ReadApiInsertCSV/tset_api.py 
{'id': 1, 'name': 'cerulean', 'year': 2000, 'color': '#98B2D1', 'pantone_value': '15-4020'}
{'id': 2, 'name': 'fuchsia rose', 'year': 2001, 'color': '#C74375', 'pantone_value': '17-2031'}
{'id': 3, 'name': 'true red', 'year': 2002, 'color': '#BF1932', 'pantone_value': '19-1664'}
{'id': 4, 'name': 'aqua sky', 'year': 2003, 'color': '#7BC4C4', 'pantone_value': '14-4811'}
{'id': 5, 'name': 'tigerlily', 'year': 2004, 'color': '#E2583E', 'pantone_value': '17-1456'}
{'id': 6, 'name': 'blue turquoise', 'year': 2005, 'color': '#53B0AE', 'pantone_value': '15-5217'}


---How to compare the two  data frame:
with the help od 'Pandas.iloc' we compared both the length of the data frame and send the result.

POST----------create anew data from APIs

















'''



















