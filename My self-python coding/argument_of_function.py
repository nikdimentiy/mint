# A function (sample) that takes three arguments

def info(object, color, price):
    print('Object:', object)
    print('Color :', color)
    print('Price :', price)
    print()


# passing parameters in direct order
info('pen', 'blue', 1)
# passing parameters in random order
info(price=5, object='cup', color='orange')
# mix order
info('coffee', price=10, color='black')

