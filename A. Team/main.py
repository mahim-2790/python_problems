n = int(input())
approve_count = 0
for i in range(0 , n):
    contestant_input = input()
    if contestant_input.count('1') >= 2:
        approve_count+=1

print(approve_count)
