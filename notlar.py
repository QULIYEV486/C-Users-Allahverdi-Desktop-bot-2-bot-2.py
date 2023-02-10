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

    

   



