# the function calculates the change in the share price on a percentage

def stock_percentage_change(new_price: float, old_price: float) -> float:
    quantitative_difference = new_price - old_price
    growth_percentage = (quantitative_difference / old_price) * 100
    result = round(growth_percentage, 3)

    if result > 0:
        print("The share price increased by:", result, "percent")
    else:
        print("The stock lost:", result, "percentage in value")


# FB (Facebook stock - NASDAQ: 07/29/21 - 30 week : Thursday -> 358.32$)
# FB (Facebook stock - NASDAQ: 07/22/21 - 29 week : Thursday -> 351.19$)

stock_percentage_change(358.32, 351.19)