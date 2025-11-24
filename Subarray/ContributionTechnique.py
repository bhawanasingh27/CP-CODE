N = int(input())
arr = list(map(int, input().split()))

total = 0

for i in range(N):
    contribution = arr[i] * (i + 1) * (N - i)
    total += contribution

print(total)
