# Uses list comprehension


def main():
    yell("This", "is", "coding")


def yell(*words):
    uppercased = [arg.upper() for arg in words]
    print(*uppercased) # unpacking list


if __name__ == "__main__":
    main()
