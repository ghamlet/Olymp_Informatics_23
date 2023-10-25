d = int(input()) #длина 
v1 = int(input())# скорость флэша мятного
v2 = int(input())# скорость зумера
t = int(input())# время пробежки

distance1 = v1 * t
distance2 = v2 * t

f_pos = distance1 %d  
z_pos = distance2 % d 

dif = abs(f_pos - z_pos)
print(dif)

