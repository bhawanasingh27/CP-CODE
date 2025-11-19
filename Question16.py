A="aeiOUz"
A=A+A
A=''.join([i for i in A if not i.isupper()])
for i in 'aeiou':
    A=A.replace(i,'#')
print(A)