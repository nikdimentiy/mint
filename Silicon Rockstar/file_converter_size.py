# Constants for file size units in bytes
KB = 1 << (10 * 1)  # 1KB = 1024 bytes
MB = 1 << (10 * 2)  # 1MB = 1024 KB
GB = 1 << (10 * 3)  # 1GB = 1024 MB
TB = 1 << (10 * 4)  # 1TB = 1024 GB

def convert_file_size(file_size, unit):
    """
    Converts the given file size to gigabytes based on the specified unit.

    Args:
        file_size (float): The file size.
        unit (str): The unit of the file size (KB, MB, GB, TB).

    Returns:
        str: A formatted string representing the file size in gigabytes.
    """
    try:
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
            raise ValueError("Invalid unit. Please enter KB, MB, GB, or TB.")

        # Return the result in gigabytes
        return f"File size: {file_size / GB:.2f}GB"
    except ValueError as e:
        return str(e)

try:
    # Get user input for file size and unit
    file_size = float(input("Enter file size: "))
    unit = input("Enter unit (KB, MB, GB, TB): ").upper()  # Convert to uppercase

    # Display the result
    result = convert_file_size(file_size, unit)
    print(result)

except ValueError as e:
    print(f"Error: {e}. Please enter a valid numeric file size.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

