def solution(canvas, rectangle):
    """
    Draw a rectangle on a canvas represented as a 2D list.

    Args:
    canvas (list): A 2D list representing the canvas.
    rectangle (tuple): A tuple containing the coordinates of the rectangle's top-left (x1, y1)
        and bottom-right (x2, y2) corners.

    Returns:
    list: The canvas with the rectangle drawn on it.

    The function iterates through the canvas and modifies it to draw a rectangle using ASCII characters.
    The top and bottom edges of the rectangle are represented by '-' characters, the left and right edges
    are represented by '|' characters, and the corners are represented by '*' characters.
    """

    x1, y1, x2, y2 = rectangle

    # Iterate through the rows of the canvas
    for i in range(y1, y2 + 1):
        # Iterate through the columns of the canvas
        for j in range(x1, x2 + 1):
            if i == y1 or i == y2:
                # Draw top and bottom edges of the rectangle
                canvas[i][j] = '*' if j == x1 or j == x2 else '-'
            elif j == x1 or j == x2:
                # Draw left and right edges of the rectangle
                canvas[i][j] = '|'

    return canvas

# Driver code to test the function
if __name__ == "__main__":
    # Create an empty canvas as a 2D list
    canvas_width = 10
    canvas_height = 5
    canvas = [[' ' for _ in range(canvas_width)] for _ in range(canvas_height)]

    # Define the rectangle coordinates (x1, y1, x2, y2)
    rectangle_coords = (2, 1, 7, 4)

    # Call the solution function to draw the rectangle on the canvas
    result_canvas = solution(canvas, rectangle_coords)

    # Print the resulting canvas
    for row in result_canvas:
        print(''.join(row))
