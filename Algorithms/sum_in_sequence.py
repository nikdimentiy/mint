# 🍀Preparation to algorithmic interview 😁

def find_sum(lst, x):
    """
    This function takes a list of integers and an integer x as input and returns two numbers from the list that add up to x.
    """
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == x:
                return lst[i], lst[j]
    return 0, 0

lst = [1, 2, 0, 3, 7, 4, 5, 11, 9]
x = 12 
result = find_sum(lst, x)
if result[0] != 0 and result[1] != 0:
    print(f"Two numbers adding up to {x} are {result[0]} and {result[1]}")
else:
    print("No two numbers add up to", x)


# The time complexity of this code is O(n^2), where n is the length of the input list.
# This is because the function iterates through the list twice to check if any two numbers add up to x.
# The space complexity of this code is O(1), because it uses a constant amount of memory regardless of the size of the input list.
