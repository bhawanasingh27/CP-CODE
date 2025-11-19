A=[2,5,6]
B=10
count=0
N=len(A)
for i in range(N):
    sum=0
    for j in range(i,N):
        sum+=A[j]
        length=j-i+1
        if length%2==0 and sum <B:
            count+=1
        if length%2!=0 and sum >B:
            count+=1
print(count)