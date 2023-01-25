n = int(input("Enter the total amount of minutes (lessons): "))
res_hours = (n // 60) % 24
res_minutes = n % 60
print(res_hours, "hours")
print(res_minutes, "minutes")
