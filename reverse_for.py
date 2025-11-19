list=[20,21,22]
N=len(list)
for i in range(0,N//2):
    list[i],list[N-1-i]=list[N-1-i],  list[i]
print(list)
    