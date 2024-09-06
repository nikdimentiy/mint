def bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) and categorize it.

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
    # Calculate BMI using the formula: weight / height^2
    b = weight / height ** 2
    
    # Determine the BMI category based on the calculated value
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]

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
        print(f"BMI for weight {weight} kg and height {height} m: {result}")
