data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64,
    "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35,
    "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23,
    "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16,
    "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
}
age = int(input("Enter a age -> (to change discount): "))

total_tickets = len(data) # total_tickets of data set

adult_tickets = 0
child_tickets = 0
discont_tickets = 0

for value in data.values():
    if value >= 18:
        adult_tickets += 1
    else:
        child_tickets += 1

for value in data.values():
    if value < 18 and value < age:
        discont_tickets += 1

revenue_1 = (adult_tickets * 20) + (child_tickets * 5)
revenue_2 = ((len(data) - discont_tickets) * 20) + (discont_tickets * 5)

percentage = ((revenue_2 - revenue_1) / revenue_1) * 100
print(int(percentage)) # percentage to increase revenue -> if change age limit
