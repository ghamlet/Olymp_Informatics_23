n = int(input())
k = int(input())

strengths = [] 
min_weakness = 0 

for i in range(n): 
    ai = int(input())  
    strengths.append(ai) 

strengths.sort() 
 
for i in range(1, k): 
    min_weakness += strengths[i] - strengths[i - 1]
 
print(min_weakness)