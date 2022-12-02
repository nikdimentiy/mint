#  A coloured triangle is created from a row of colours, each of which is red, green or blue.
#  Successive rows, each containing one fewer colour than the last, are generated by considering
#  the two touching colours in the previous row. If these colours are identical, the same colour
#  is used in the new row. If they are different, the missing colour is used in the new row.
#  This is continued until the final row, with only a single colour, is generated.


def triangle(row):
    if len(row) == 1:
        return row
    else:
        temp = ""
        for i in range(len(row)-1):
            if i == len(row):
                return row
            elif row[i] == row[i+1]:
                temp = temp + row[i]
            elif row[i] in "BG" and row[i+1] in "BG":
                temp = temp + "R"
            elif row[i] in "RG" and row[i+1] in "RG":
                temp = temp + "B"
            elif row[i] in "BR" and row[i+1] in "BR":
                temp = temp + "G"
        return triangle(temp)
