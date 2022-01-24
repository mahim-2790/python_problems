n = int(input())
total_c = 0
total_r = 0
total_s = 0

for i in range(n):
    amount, animal = map(int, input().split())
    if animal == "C":
        total_c = total_c + amount
    elif animal == "R":
        total_r = total_r + amount
    elif animal == "S":
        total_s = total_s + amount

total_animals = total_s + total_r + total_c

c_percent = (total_c / total_animals * 1.0) * 100.00
r_percent = (total_r / total_animals * 1.0) * 100.00
s_percent = (total_s / total_animals * 1.0) * 100.00

print("Total: {} cobaias".format(total_animals))
print("Total de coelhos:",total_c)
print("Total de ratos:",total_r)
print("Total de sapos:",total_s)
print("Percentual de coelhos: %.2lf %%"%c_percent)
print("Percentual de ratos: %.2lf %%"%r_percent)
print("Percentual de sapos: %.2lf %%"%s_percent)
