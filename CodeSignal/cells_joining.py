def solution(table: List[str], coords: List[List[int]]) -> List[str]:
    """
    Merge cells within a given rectangular part of the table into a single cell
    by removing the borders between them.

    Args:
    - table (List[str]): A table in ASCII graphics where '|' and '-' characters
      represent borders, and '+' characters represent their intersection. It is
      guaranteed that there are no joined cells in the table, and that the table
      occupies the entire rectangular array, i.e. its outer borders occupy the
      leftmost and the rightmost columns of the array as well as its topmost and
      bottommost rows.
    - coords (List[List[int]]): A list containing two elements, where the first
      element is a list containing the 0-based row and column indices (given in
      that exact order) of the extreme bottom left cell in the area to join, and
      the second element is a list containing indices of the extreme top right
      cell of that region. It's guaranteed that there are at least two cells to
      be joined, and that cells with the given indices do exist in the table.

    Returns:
    - List[str]: The table with cells in the given region joined into one.

    Example:
    table = ["+----+--+-----+----+",
             "|abcd|56|!@#$%|qwer|",
             "|1234|78|^&=()|tyui|",
             "+----+--+-----+----+",
             "|zxcv|90|77777|stop|",
             "+----+--+-----+----+",
             "|asdf|~~|ghjkl|100$|",
             "+----+--+-----+----+"]
    coords = [[2, 0], [1, 1]]
    assert solution(table, coords) == ["+----+--+-----+----+",
                                       "|abcd|56|!@#$%|qwer|",
                                       "|1234|78|^&=()|tyui|",
                                       "+----+--+-----+----+",
                                       "|zxcv 90|77777|stop|",
                                       "|       +-----+----+",
                                       "|asdf ~~|ghjkl|100$|",
                                       "+-------+-----+----+"]
    """

    table = list(map(list, table))
    rdivs = [i for i, row in enumerate(table) if row[0] == "+"]
    cdivs = [i for i, col in enumerate(table[0]) if col == "+"]
    x1, y1, x2, y2 = rdivs[coords[1][0]], cdivs[coords[0]
                                                [1]], rdivs[coords[0][0] + 1], cdivs[coords[1][1] + 1]
    for x in range(x1 + 1, x2):
        if y1 == 0:
            table[x][y1] = "|"
        if y2 == len(table[0]) - 1:
            table[x][y2] = "|"

        for y in range(y1 + 1, y2):
            if table[x][y] in "|-+":
                table[x][y] = " "

    for y in range(y1 + 1, y2):
        if x1 == 0:
            table[x1][y] = "-"
        if x2 == len(table) - 1:
            table[x2][y] = "-"
    return list(map(lambda x: "".join(x), table))
