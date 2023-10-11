# main_script.py

def main():
    x = int(input("What is the value of x: "))
    print("X squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()

# # test_main_script.py
# from main_script import square

# # Test cases for the square function

# def test_square_positive():
#     assert square(5) == 25

# def test_square_negative():
#     assert square(-3) == 9

# def test_square_zero():
#     assert square(0) == 0

# # If running this script directly, run the tests
# if __name__ == "__main__":
#     import pytest
#     pytest.main()
