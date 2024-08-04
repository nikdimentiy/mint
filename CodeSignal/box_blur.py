def solution(image):
    """
    Applies a 3x3 average blur filter to a given 2D image represented as a list of lists.

    Parameters:
    image (List[List[int]]): A 2D list representing the image, where each element is an integer 
                              representing the pixel value (0-255).

    Returns:
    List[List[int]]: A new 2D list representing the blurred image, with the same dimensions 
                     as the input image minus the borders.
    """
    # Get the number of rows and columns in the input image
    rows = len(image)
    cols = len(image[0])
    
    # Initialize a new 2D list for the blurred image, reducing the size by 2 in both dimensions
    blurred = [[0] * (cols - 2) for _ in range(rows - 2)]
    
    # Iterate over each pixel in the image, excluding the border pixels
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Calculate the average of the 3x3 grid centered at (i, j)
            avg = (image[i-1][j-1] + image[i-1][j] + image[i-1][j+1] +
                   image[i][j-1] + image[i][j] + image[i][j+1] +
                   image[i+1][j-1] + image[i+1][j] + image[i+1][j+1]) // 9
            
            # Assign the calculated average to the corresponding position in the blurred image
            blurred[i-1][j-1] = avg
            
    return blurred

# Driver code to test the solution function
if __name__ == "__main__":
    # Example input image (5x5)
    image = [
        [100, 200, 100, 200, 100],
        [200, 100, 200, 100, 200],
        [100, 200, 100, 200, 100],
        [200, 100, 200, 100, 200],
        [100, 200, 100, 200, 100]
    ]
    
    # Call the solution function
    blurred_image = solution(image)
    
    # Print the blurred image
    print("Blurred Image:")
    for row in blurred_image:
        print(row)
