import sys
from datetime import datetime   

if sys.argv[1] == "tarixi" and sys.argv[2] == "de":
    print(datetime.now(). strftime('%S-%Y-%M-%H'))
   
elif sys.argv[1] == "ili" and sys.argv[2] == "de":
    print(datetime.now(). strftime('%Y'))

elif sys.argv[1] == "ayi" and sys.argv[2] == "de":
    print(datetime.now(). strftime('%m'))

elif sys.argv[1] == "saati" and sys.argv[2] == "de":
    print(datetime.now(). strftime('%H'))


# folder

import os 

if sys.argv[1] == "folder" and sys.argv[2] == "yarat":  
    directory = input('Folder adi yain: ')

    parent_dir = r"C:\Users\Allahverdi\Desktop\bot"

    path = os.path.join(parent_dir,directory)

    os.mkdir(path)

    print('folder yarandi')

elif sys.argv[1] == "folderi" and sys.argv[2] == "sil":
    directory = input()

    parent_dir = r"C:\Users\Allahverdi\Desktop\bot"

    path = os.path.join(parent_dir,directory)

    os.rmdir(path)

    print('Folder Silindi')

# kalkulyator
op = sys.argv[1]

if op  == "topla":
    a = int(input())
    b = int(input())
    print( a + b)

elif op == "cix":
    a = int(input())
    b = int(input())
    print( a - b) 

elif op == "vur":
    a = int(input())
    b = int(input())
    print( a * b)

elif op == "bol":
    a = int(input())
    b = int(input())
    print( a // b)      


# menim yasim
import sys


from datetime import  date
birth=int(input("ili DE"))
today = date.today().strftime("%Y")
print("sizin yasiniz",int(today)-birth)



import sys
import os


if sys.argv[1] == "text" and  sys.argv[2] == "creat":
    b = input("adi daxil et:  ")
    f = open(f'{b}.txt',"x")
    print("fayl yarandi")


elif sys.argv[1] == "text" and sys.argv[2] == "read":
    file = open(input("fayli daxil et: "), 'r')
    content = file.read()
    print(content)   


elif sys.argv[1] == "text" and sys.argv[2] == "write":
    file = open(input("adi daxil et:  "), 'w')
    file.write(input("metn daxil et: "))
    print("Text writing")
     
     
elif sys.argv[1] == "text" and sys.argv[2] == "add":
    file = open(input("fayli daxil et: "), "a")
    file.write(input("metn daxil et: "))
    print("text add")


elif sys.argv[1] == "text" and sys.argv[2] == "clear":
    os.remove(input("fayl adin daxil et: "))
    print("text clear")


elif sys.argv[1] == "text" and sys.argv[2] == "sil":
    file = open(input("fayli daxil et: "), "r+")
    file.seek(0)
    file.truncate
