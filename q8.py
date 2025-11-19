#given an array find the sum of all subarrays sums
#givsn an array A of length N your task is to found max possible sum of any non empty contiguous array in other words among all possible subarrays of A determine the one that is the highest
A = [2,5,6,-1,-2]
n = len(A)
max_sum = A[0]
current_sum = A[0]

for i in range(1, n):
    if current_sum < 0:
        current_sum = A[i]
    else:
        current_sum = current_sum + A[i]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)
