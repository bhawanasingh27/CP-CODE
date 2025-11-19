#Given n and i check if ith bit is set or not.
n=int(input())
i=int(input())
if ((n>>i)&1==1):
    print("set")
else:
 print("unset")

#Given aninteger N count how many set bit are there in an array
arr=[2,6,8]
set_bits=0
for num in arr:
    while num > 0:
        set_bits+= num & 1
        num>>=1
print(set_bits)