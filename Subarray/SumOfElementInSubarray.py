# Input
N = int(input())
arr = list(map(int, input().split()))
L, R = map(int, input().split())

# Convert 1-based index to 0-based index and find sum
result = sum(arr[L-1 : R])

print(result)

