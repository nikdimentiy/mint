# program in python
newPrice = float(input("Enter today's stock price on stock market: "))
oldPrice = float(input("Enter old stock price on stock market: "))

qDif = newPrice - oldPrice
growthPercentage = (qDif / oldPrice) * 100
result = round(growthPercentage, 3)

if result > 0:
    print("The share price increased by:", result, "percent")
else:
    print("The stock lost:", result, "percentage in value"