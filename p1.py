def perfect_square(A):
    root = int(A**0.5)     
    if root * root == A:    
        return root
    else:
        return -1

# example
A = int(input("Enter number: "))
ans = perfect_square(A)
print(ans)
