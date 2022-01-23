count = 0
sum = 0

for i in range(6):
    num = float(input())
    if num > 0:
        count+=1 
        sum = sum + num
avg = sum / count

print(f"{count} valores positivos")
print(f"{average:0.1f}")
