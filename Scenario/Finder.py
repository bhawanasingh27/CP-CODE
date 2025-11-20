n=int(input())
a=list(map(int,input().split()))
tar=int(input())
count=0
for i in range(n): 
    for j in range(i+1,n):
        if a[i]+a[j]==tar:
            count +=1
print(count) 