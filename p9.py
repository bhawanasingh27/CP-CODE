#given a string calculate the length of longest palindromic substring
s = input("Enter a string: ")
count=0
for i in range(len(s)):
    for j in range(i+1,len+1):
        b=s[i:j]
        c=b[::-1]
        if b==c:
            if len(b)>count:
                count=len(b)
print(count)