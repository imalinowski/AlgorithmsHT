import os.path, subprocess
from subprocess import STDOUT, PIPE
import random
from time import time

def compile_java (java_file):
    subprocess.check_call(['javac', java_file])

def execute_java (java_file):
    cmd=['java', java_file]
    proc=subprocess.Popen(cmd, stdout = PIPE, stderr = STDOUT)
    input = subprocess.Popen(cmd, stdin = PIPE)
    print(proc.stdout.read())


compile_java("AlgoHT.java")
f = open("input.txt",'w')
limit = 1000000
f.write(str(limit)+"\n")
array = []
checklist = []
print("генерирую тестовую информацию...")
for i in range(limit):
    a = random.randint(0,2)
    if(a==0 or len(array)==0):
        a = random.randint(0,1000000000)
        array.append(a)
        f.write("+ "+str(a)+"\n")
    elif(a==1):
        array.pop(0)
        f.write("-\n")
    elif(a==2):
        checklist.append(min(array))
        f.write("?\n")
f.close()
print("запускаю код")
start = int(time() * 1000)
execute_java("AlgoHT")
print("work done in>"+str(int(time() * 1000)-start))
print("проверяю")
f = open("output.txt","r")
c = 0
for i in f:
    if(int(i) != checklist[c]):
        print("error should >"+str(checklist[c])+" but >"+str(i))
    c+=1
print("check done")
