A = [2,5,6]
B = 10

count = 0
n = len(A)



for i in range(n):
    sum = 0
    subarray = []
    for j in range(i, n):
        sum = sum + A[j]
        subarray.append(A[j])
        if sum < B:
            print(subarray)
            count = count + 1

print(count)
