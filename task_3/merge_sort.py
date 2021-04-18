f = open("output.txt",'w')

def merge_sort(s,A):
    global f
    if len(A)==1:
        f.write(str(s)+' '+str(s)+' '+str(A[0])+' '+str(A[0])+'\n')
    if len(A) == 1 or len(A) == 0:   
        return
    L, R = A[:len(A) // 2], A[len(A) // 2:]
    merge_sort(s,L)
    merge_sort(s+len(A)//2,R) 
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]; n += 1; k += 1
    while m < len(R):
        C[k] = R[m]; m += 1; k += 1
    for i in range(len(A)):
        A[i] = C[i]
    f.write(str(s)+' '+str(s+len(A)-1)+' '+str(A[0])+' '+str(A[len(A)-1])+'\n')
    

file = open('input.txt')
n = int(file.readline())
A = []
for i in range(n):
    A.append(int(file.readline()))
merge_sort(1,A)
for i in A:
    f.write(str(i)+' ')
f.close()
