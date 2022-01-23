dia, date1 = input().split()
date1 = int(date1)
h1,m1,s1 = map(int,input().split(":"))

dia, date2 = input().split()
date2 = int(date2)
h2,m2,s2 = map(int,input().split(":"))

passesSeconds = h1*3600 + m1*60 + s1
remainingSeconds = 86400 - passesSeconds
remainingSeconds2 = h2*3600 + m2*60 + s2

date =(date2-1)-date1
remainDateSeconds = date*86400

totalSeconds = remainingSeconds+remainingSeconds2+remainDateSeconds

finalDate = totalSeconds/86400
totalSeconds = totalSeconds%86400
finalHour = totalSeconds/3600
totalSeconds = totalSeconds%3600
finalMinutes = totalSeconds/60
totalSeconds = totalSeconds%60

print(f"{int(finalDate)} dia(s)")
print(f"{int(finalHour)} hora(s)")
print(f"{int(finalMinutes)} munito(s)")
print(f"{int(totalSeconds)} segundo(s)")

