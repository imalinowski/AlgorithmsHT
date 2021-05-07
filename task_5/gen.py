import random
f_in =  open('input.txt','w')
n = random.randint(0,1000)
f_in.write(str(n)+'\n')
f_in.write('+'+str(random.randint(-999,999))+'\n')
for i in range(n):
    r = random.randint(-1,1)
    if(r == 1):
        f_in.write('+'+str(random.randint(-999,999))+'\n')
    if(r == -1):
        f_in.write('-'+str(random.randint(-999,999))+'\n')
    if(r == 0):
        f_in.write('?'+str(random.randint(-999,999))+'\n')
