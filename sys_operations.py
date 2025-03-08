import os
import sys
import platform
import socket


#lab9 - q - 3.a.a 3.a.b
# machine type and processor type
print(platform.machine())
print(platform.architecture())

# lab9 - 3.a.c 3.a.d
#set amd get socket timeout
print(socket.getdefaulttimeout())
socket.setdefaulttimeout(50)
print(socket.getdefaulttimeout())

# lab9 - 3.a.e
#os name
print(os.name)
print(platform.system())

# lab9 - 3.a.f
# process is
print(os.getpid())

# lab9 - q3.b.a
#file description
#open(or create )a file name fdpractice.txt
f_name = "fdpractice.txt"
#with open("fdpractice.txt" ,"a+") as f:
 #  print(f.readline())
 #   f.write("hello world")

#f1 = open(f_name, "r")
#print(f1)
#f1.close()

f=os.open(f_name, os.O_RDWR | os.O_CREAT)
print(f)

f_obj = os.fdopen(f,"a+")
print(f_obj)
f_obj.close()

print()

# lab9 - q3.b.e
#forking
print("before fork:",os.getpid())
p= os.fork()
print("after fork",os.getpid())


if p==0:
    print("child process")
    print("parent process PID",os.getppid())
else:
    print("parent process")
    os.wait()
    print("child process",p)

print("last line")
