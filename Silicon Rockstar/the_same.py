# Level 6 Kata - Code Wars
# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities
# (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.


def comp(array1, array2):
    import math

    # Declare a boolean to determine what string to return.
    is_same = True
    
    # Check for None arrays.
    if array1 == None or array2 == None:
        return False
     
    
    if array1 == [] and array2 == []:
        return True
    
    # Check for different sizes of arrays.
    if len(array1) != len(array2):
        return False

    
    # Check for empty arrays.
    if len(array1) == 0 or len(array2) == 0:
        return False
    
    # Loop through array2 and check if each value is the square of one of the values in array1.
    for num in array2:
        if (int(math.floor(math.pow(num, .5)))) not in array1 and (int(math.floor(math.pow(num, .5))) * -1) not in array1:
            is_same = False
        if array2.count(num) != array1.count(math.pow(num, .5)) and array2.count(num) != array1.count(math.pow(num, .5) * -1):
            return False
    
    # Loop through array1 and check if each value is the square of one of the values in array1.
    for num in array1:
        if (math.pow(num, 2)) not in array2:
            is_same = False
        if array1.count(num) > 1:
            if array2.count(num * num) <=1:
                return False
    # Return boolean is_same
    return is_same
