import math


def print_matrix( matrix ):
    for r in matrix:
        s = ""
        for c in  r:
            s += str(c) + " "
        print s

def ident( matrix ):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if (c == r):
                matrix[r][c] = 1
            else:
                matrix[r][c] = 0

    #print_matrix( matrix )

def scalar_mult( matrix, s ):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrix[r][c] *= s

    #print_matrix( matrix )

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    temp = []
    for c in range(len(m1)):
        temp.append([])
        for r in range(len(m2[c])):




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
