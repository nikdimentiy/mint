def main():
    name = input("What is your name: ?")
    hello(name)


def hello(name="world"):
    return f"Hello, {name}"


if __name__ == "__name__":
    main()
