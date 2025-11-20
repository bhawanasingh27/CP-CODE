def reverse(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse(s[:-1])

s = input()
print(reverse(s))
