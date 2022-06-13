from math import sqrt


class Sudoku(object):

    def __init__(self, board):
        self.board = board
        self.n = len(self.board)
        self.sqrt_user = int(sqrt(self.n))

    def is_valid(self):
        # Check size and contents
        for row in self.board:
            if len(row) != self.n:
                return False
            for n in row:
                # Make sure every entry is an integer and is in range
                if not type(n) is int or not self.in_range(n):
                    return False

        # Check rows and columns
        for n in range(self.n):
            if not self.valid_row(n) or not self.valid_col(n):
                return False
        # Check squares
        for i in range(self.sqrt_user):
            for j in range(self.sqrt_user):
                if not self.valid_square(i, j):
                    return False
        return True

    def in_range(self, n):
        return n >= 1 and n <= self.n

    def valid_row(self, i):
        valid = [False] * self.n
        row = self.board[i]
        for n in row:
            try:
                valid[n - 1] = True
            except IndexError:
                return False
        return all(valid)

    def valid_col(self, j):
        valid = [False] * self.n
        col = [row[j] for row in self.board]
        for n in col:
            try:
                valid[(n - 1)] = True
            except IndexError:
                return False
        return all(valid)

    def valid_square(self, ni, nj):
        ni *= self.sqrt_user
        nj *= self.sqrt_user
        valid = [False] * self.n
        for i in range(ni, ni + self.sqrt_user):
            for j in range(nj, nj + self.sqrt_user):
                n = self.board[i][j]
                try:
                    valid[n - 1] = True
                except IndexError:
                    return False
        return all(valid)
