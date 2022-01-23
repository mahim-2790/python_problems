n = int(input())

for i in range(n):
    number = int(input())
    if number == 0:
        print("NULL")
    elif number % 2 == 0:
        if number > 0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    else:
        if number > 0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")
        