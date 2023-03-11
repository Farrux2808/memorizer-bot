import string


s = input()
a = {}
for i in string.ascii_uppercase:
    a[i] = 0
for char in s:
    a[char] += 1


n = len(s)
for i in range(n-1):
    for j in range(n-i-1):
        