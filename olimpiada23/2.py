n = int(input())#серия
m = int(input())#интро
k = int(input())#перемотка
t = int(input())#потеря

count = 0

while count * k < m: 
    count += 1
 
if count * k < m + t: 
    print(n - ((m+t) - count * k)) 
else: 
    print(n)
