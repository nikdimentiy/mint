# 😎 Preparation to coding interview 🍀 (algorithmic session)

def countbeating_rooks(rookcoords):
    """This function takes a list of rook coordinates on a chess board and returns the number of pairs of rooks that can beat each other.

    Parameters:
    rookcoords (list): A list of tuples representing the row and column of each rook on the board.

    Returns:
    int: The number of pairs of rooks that can beat each other.

    Example:
    >>> rookcoords = [(1, 1), (1, 3), (2, 4), (3, 1), (4, 4)]
    >>> countbeating_rooks(rookcoords)
    3
    """

    def addrook(roworcol, key):
        """This helper function adds a rook to a dictionary that counts the number of rooks in each row or column.

        Parameters:
        roworcol (dict): A dictionary that maps a row or column number to the number of rooks in that row or column.
        key (int): The row or column number of the rook to be added.

        Returns:
        None
        """
        if key not in roworcol: # If the key is not in the dictionary, initialize it with zero
            roworcol[key] = 0
        roworcol[key] += 1 # Increment the count of rooks for that key

    def countpairs(roworcol):
        """This helper function counts the number of pairs of rooks that can beat each other in a given row or column.

        Parameters:
        roworcol (dict): A dictionary that maps a row or column number to the number of rooks in that row or column.

        Returns:
        int: The number of pairs of rooks that can beat each other in that row or column.
        """
        pairs = 0 # Initialize the number of pairs to zero
        for key in roworcol: # Loop through each key in the dictionary
            pairs += roworcol[key] - 1 # Add the number of rooks minus one to the number of pairs
            # This is because each rook can beat all the other rooks in the same row or column
        return pairs # Return the number of pairs

    rooksinrow = {} # Initialize an empty dictionary to store the number of rooks in each row
    rooksincol = {} # Initialize an empty dictionary to store the number of rooks in each column
    for row, col in rookcoords: # Loop through each coordinate in the list
        addrook(rooksinrow, row) # Add a rook to the corresponding row
        addrook(rooksincol, col) # Add a rook to the corresponding column

    return countpairs(rooksinrow) + countpairs(rooksincol) # Return the sum of pairs in rows and columns
