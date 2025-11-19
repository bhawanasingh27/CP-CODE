A=5
B=12
C=[2,1,3,4,5]
N=len(C)
maxV=0
for i in range(N):
    sum1=0
    for j in range(i,N):
        sum1+=C[j]
        if sum1>maxV