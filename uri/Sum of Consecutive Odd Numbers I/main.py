x = int(input())
y = int(input())
start = 0
end = 0
sum = 0
if x > y:
    start = y
    end = x
elif x < y:
    start = x
    end = y
else:
    start = x 
    end = y

for i in range(start+1,end):
   
    if i % 2 != 0:
        sum = sum + i

print(sum)
