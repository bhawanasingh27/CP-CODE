#given an array and increment number generate a new array which contains all value of original array increased by increment value 
#arr = list(map(int, input("Enter numbers: ").split()))
#inc = int(input("Enter increment number: "))
#new_arr = [i + inc for i in arr]
#print("New array =", new_arr)

#(Linear Search)Given a list of integer and target number find and print index of target number in the list
A=list(map(int,input().split()))
t=int(input("Enter the target number: "))
x=-1
for i in range(len(A)):
    if A[i]==t:
        x=i
        print(x)