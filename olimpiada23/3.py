n = int(input())
a = int(input())
b = int(input())  

time = 0
for i in range(n):
    time = max(time, a*i+2*a+2*(n-1-i)*b)
print(time)