import random
rand_param = 100
f_in =  open('input.txt','w')
n = random.randint(5,rand_param)
f_in.write(str(n)+'\n')
f_in.write('+'+str(random.randint(-rand_param/2,rand_param/2))+'\n')
for i in range(n-1):
    r = random.randint(-1,1)
    if(r == 1):
        f_in.write('+'+str(random.randint(-rand_param/2,rand_param/2))+'\n')
    if(r == -1):
        f_in.write('-'+str(random.randint(-rand_param/2,rand_param/2))+'\n')
    if(r == 0):
        f_in.write('?'+str(random.randint(-rand_param/2,rand_param/2))+'\n')
