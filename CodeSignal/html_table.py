def solution(table: str, row: int, column: int) -> str:
    """
    Extracts the content of the cell with coordinates (row, column) from a rectangular HTML table.

    Args:
        table (str): A syntactically correct representation of a rectangular HTML table with at least one cell.
                     Each of its cells contains only letters and/or digits.
        row (int): A non-negative integer representing 0-based index of the desired row (rows are numbered from top to bottom).
        column (int): A non-negative integer representing 0-based index of the desired column (columns are numbered from left to right).

    Returns:
        str: The content of the cell with coordinates (row, column) or the string "No such cell"
             if there is no cell with those coordinates in the table.
    """
    # Remove unnecessary HTML tags
    table = table.replace("</td>", "").replace("</tr>",
                                               "").replace("<table>", "").replace("</table>", "")

    # Check if the given coordinates are valid
    if row >= table.count("<tr>") or column >= table.split("<tr>")[row + 1].count("<td>"):
        return "No such cell"

    # Extract the content of the desired cell
    cell_content = table.split("<tr>")[row + 1].split("<td>")[column + 1]

    return cell_content
