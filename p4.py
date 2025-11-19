#given N array elements,every element repeats twice except 1 find the unique number using bitwise operator
arr = [4, 1, 2, 1, 2]
unique_num= 0
for i in range(len(arr)):
    unique_num = unique_num ^ arr[i]
print(unique_num)
