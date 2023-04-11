import numpy


def solution(pieces):
    # Initializes variables
    res = 0
    f = numpy.zeros((20, 10))
    s = [0]*20

    # Loops over each piece in the input list
    for k, p in enumerate(pieces):
        w = -1
        rd = -1
        rs = -1

        # Rotates and places each piece in the grid
        for r in range(4):
            i = 0
            while i < 11-len(p[0]):
                c = j = 0
                while (not c) and j < 20-len(p):
                    j += 1
                    for n, line in enumerate(p):
                        for m, x in enumerate(line):
                            if x == '#' and f[j+n][i+m]:
                                c = 1
                    j -= c
                o = sum(s[j:j+len(p)])
                if o > w:
                    w, rd, rs = o, (i, j), r
                i += 1
            p = rot(p)

        # Rotates the chosen piece and places it in the grid
        for _ in range(rs):
            p = rot(p)
        bi, bj = rd
        for n, line in enumerate(p):
            for m, x in enumerate(line):
                if x == '#':
                    f[bj+n][bi+m] = k+1

        # Updates the state of the grid and counts completed rows
        s, nf = [*map(sum, f)], []
        for n, s in enumerate(f):
            if all(s):
                res += 1
            else:
                nf.append(f[n])
        f = [[0]*10 for _ in range(20-len(nf))]+nf
        s = [*map(sum, f)]

    # Returns the number of completed rows
    return res


# Rotates a matrix 90 degrees clockwise
def rot(m): return list(zip(*m[::-1]))
