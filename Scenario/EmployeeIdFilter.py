n=int(input())
arr=list(map(int,input().split()))
even=[]
for i in range (len(arr)):
    if(arr[i] %2==0):
       even.append(arr[i])
       
if even:
    print(*even)
        
else:
    print(-1)  