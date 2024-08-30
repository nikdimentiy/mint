def solution(n, firstNumber):
    """
    Find the number that is radially opposite to the given firstNumber in a circular arrangement of numbers.

    The numbers are arranged in a circle from 0 to n-1. The function calculates the number that is 
    located directly opposite to firstNumber by adding half of n to firstNumber and taking the result 
    modulo n.

    Parameters:
    n (int): The total number of integers in the circle (must be greater than 0).
    firstNumber (int): The starting number in the circle (must be in the range 0 to n-1).

    Returns:
    int: The number that is radially opposite to firstNumber.
    """
    # Calculate the opposite number by adding half of n to firstNumber
    # and taking the result modulo n to ensure it wraps around the circle.
    return (firstNumber + n // 2) % n

# Driver code to test the solution function
if __name__ == "__main__":
    # Example test cases
    n = 10
    firstNumber = 2
    print(f"The number opposite to {firstNumber} in a circle of {n} numbers is: {solution(n, firstNumber)}")

    n = 5
    firstNumber = 1
    print(f"The number opposite to {firstNumber} in a circle of {n} numbers is: {solution(n, firstNumber)}")

    n = 8
    firstNumber = 3
    print(f"The number opposite to {firstNumber} in a circle of {n} numbers is: {solution(n, firstNumber)}")

    n = 12
    firstNumber = 7
    print(f"The number opposite to {firstNumber} in a circle of {n} numbers is: {solution(n, firstNumber)}")
