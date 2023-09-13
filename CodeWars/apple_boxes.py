# You have k apple boxes full of apples. Each square box of size m contains m × m apples.
# You just noticed two interesting properties about the boxes:

# The smallest box is size 1, the next one is size 2,..., all the way up to size k.
# Boxes that have an odd size contain only yellow apples. Boxes that have an even size contain only red apples.
# Your task is to calculate the difference between the number of red apples and the number of yellow apples.


def calculate_apple_difference(k):
    """
    Calculate the difference between the number of red apples and yellow apples in apple boxes.

    Args:
        k (int): The number of apple boxes.

    Returns:
        int: The difference between the number of red apples and yellow apples.

    Explanation:
    - Yellow apples are in boxes with odd sizes (1x1, 3x3, 5x5, ...).
    - Red apples are in boxes with even sizes (2x2, 4x4, 6x6, ...).

    The function calculates the number of red and yellow apples in the boxes and returns the difference.
    """
    yellow_apples = sum(i * i for i in range(1, k + 1, 2))
    red_apples = sum(i * i for i in range(2, k + 1, 2))
    return red_apples - yellow_apples

# Driver code to test the function
if __name__ == "__main__":
    k = int(input("Enter the number of apple boxes (k): "))
    apple_difference = calculate_apple_difference(k)
    print(f"The difference between the number of red and yellow apples is: {apple_difference}")

