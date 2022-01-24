max = 0
position = 0

for i in range (100):
    number = int(input())
    if max < number:
        max = number
        position = i + 1
print(f"{max}")
print(f"{position}")
