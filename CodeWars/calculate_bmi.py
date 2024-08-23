def bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) and categorize the result.

    Parameters:
    weight (float): The weight of the individual in kilograms.
    height (float): The height of the individual in meters.

    Returns:
    str: A string indicating the BMI category:
         - "Underweight" if BMI <= 18.5
         - "Normal" if BMI <= 25.0
         - "Overweight" if BMI <= 30.0
         - "Obese" if BMI > 30
    """
    # Calculate BMI using the formula: weight / height squared
    bmi_value = weight / height ** 2
    
    # Determine the BMI category based on the calculated value
    if bmi_value <= 18.5:
        return "Underweight"
    elif bmi_value <= 25:
        return "Normal"
    elif bmi_value <= 30:
        return "Overweight"
    else:
        return "Obese"

# Driver code to test the bmi function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        (50, 1.6),  # Underweight
        (70, 1.75), # Normal
        (85, 1.75), # Overweight
        (95, 1.75)  # Obese
    ]
    
    for weight, height in test_cases:
        result = bmi(weight, height)
        print(f"Weight: {weight} kg, Height: {height} m -> BMI Category: {result}")
