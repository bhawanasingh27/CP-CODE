# Input
N = int(input())
arr = list(map(int, input().split()))

# Printing all subarrays
for i in range(N):
    for j in range(i, N):
        # Print elements from index i to j
        print(*arr[i:j+1])
