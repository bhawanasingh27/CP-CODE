#sum of every single sub arraydef subarray_sum(A, S, E):
def subarray_sum(A, S, E):
    total = 0
    for i in range(S, E + 1):
        total += A[i]
    print(total)

def allsubarray_sum(A):
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            subarray_sum(A, i, j)

A = [1, 2, 3]
allsubarray_sum(A)

