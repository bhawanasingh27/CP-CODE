#A=list(map(int,input().split()))
#print(A)
#given an array and compute the sum of all the elements in the array

#A=list(map(int,input().split()))
#sum=0
#for i in A:
#    sum=sum+i
#print(sum)
#Given an array find the maximum value in it
#A=list(map(int,input().split()))
#max=A[1]
#for i in A:
#    if i>max:
#        max=i
#print(max)

#given an array and a target number find number of occurence of target number in a given array
A=list(map(int,input().split()))
target=int(input())
count=0
for i in A:
    if target == i:
        count=count+1
print(count)