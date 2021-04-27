def lsd_str(x,K):
    buckets = {chr(i) : [] for i in range(ord('a'),ord('z')+1)}
    for i in range(K):
        for s in x:
            buckets[s[len(s)-1-i]].append(s)
        x = []
        for k in buckets:
            x.extend(buckets[k])
            buckets[k]=[]
    return x

fin = open('input.txt')
N,M,K = map(int, fin.readline().split())
x = [str(i+1)+'' for i in range(N)]
for i in range(M):
    l = fin.readline()
    for j in range(len(x)):
        x[j] = x[j]+l[j]
x = lsd_str(x,K)
fout = open('output.txt','w')
for i in x:
    fout.write(i[0]+' ')
fout.close()
