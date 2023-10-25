n = input()
k = input() 
count = 1 
room = 1
br = False

while True: 
    if br:
        break

    for i in range(1, len(n)):
        if str(room) * i == k:
            br = True
            break
        count+=1
    room += 1 

print(count)