import random
f = open("input.txt",'w')
n = random.randint(0,100)
f.write(str(n)+'\n')
for i in range(n):
    f.write(str(random.randint(0,100))+'\n')
f.close()
