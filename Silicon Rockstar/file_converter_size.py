# Constants for file size units in bytes
KB = 1 << (10 * 1)  # 1KB = 1024 bytes
MB = 1 << (10 * 2)  # 1MB = 1024 KB
GB = 1 << (10 * 3)  # 1GB = 1024 MB
TB = 1 << (10 * 4)  # 1TB = 1024 GB
PB = 1 << (10 * 5)  # 1PB = 1024 TB
EB = 1 << (10 * 6)  # 1EB = 1024 PB
ZB = 1 << (10 * 7)  # 1ZB = 1024 EB
YB = 1 << (10 * 8)  # 1YB = 1024 ZB


def convert_file_size(file_size, unit):
    """
    Converts the given file size to gigabytes based on the specified unit.

    Args:
        file_size (float): The file size.
        unit (str): The unit of the file size (KB, MB, GB, TB).

    Returns:
        str: A formatted string representing the file size in gigabytes.
    """
    # Convert file size to bytes based on unit
    if unit == "KB":
        file_size *= KB
    elif unit == "MB":
        file_size *= MB
    elif unit == "GB":
        file_size *= GB
    elif unit == "TB":
        file_size *= TB
    else:
        return "Invalid unit. Please enter KB, MB, GB, or TB."

    # Return the result in gigabytes
    return f"File size: {file_size / GB:.2f}GB"


# Get user input for file size and unit
file_size = float(input("Enter file size: "))
unit = input("Enter unit (KB, MB, GB, TB): ").upper()  # Convert to uppercase

# Display the result
result = convert_file_size(file_size, unit)
print(result)
