#print all subarray of an array

def subarray(A, S, E):
    for i in range(S, E + 1):
        print(A[i], end=" ")
    print()

def allsubarray(A):
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            subarray(A, i, j)

A = [1, 2, 3]
allsubarray(A)
