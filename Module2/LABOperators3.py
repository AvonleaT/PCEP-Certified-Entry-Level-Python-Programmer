hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total = hour * 60 + mins
total = total + dura
hour = total // 60
mins = total % 60

print(hour, mins)
