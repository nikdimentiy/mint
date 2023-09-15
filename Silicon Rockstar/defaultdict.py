from collections import defaultdict

def create_default_dict():
    """
    This function demonstrates the usage of a defaultdict from the collections module.
    It initializes a defaultdict with a lambda function as the default value generator.
    """

    # Initialize a defaultdict with a lambda function to provide a default value "E-commerce".
    d = defaultdict(lambda: "E-commerce")

    # Add some key-value pairs to the defaultdict.
    d[1] = "Hello"
    d[2] = "Cool"
    d[3] = "Morning"
    d[4] = "Ice"
    d[5] = "Metropoliten"

    # Access and print values from the defaultdict.
    print("Dictionary:", d)
    print("Value at key 3:", d[3])  # Accessing an existing key.
    print("Value at key 0 (default):", d[0])  # Accessing a non-existing key returns the default value.
    
    # Get the length of the defaultdict.
    print("Length of the dictionary:", len(d))

    # Check the type of the defaultdict.
    print("Type of the dictionary:", type(d))

# Driver code to call the function.
if __name__ == "__main__":
    create_default_dict()
