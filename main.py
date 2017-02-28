from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print "===Testing Identity Matrix Creation==="
ident( matrix )

print "=====Displaying Matrix====="
print_matrix( matrix )

print "===Testing Scalar Matrix Multiplication==="
scalar_mult( matrix, 7 )
print_matrix( matrix )

print "===Creating New Identity Matrix==="
matrix2 = new_matrix()
ident( matrix2 )
print_matrix( matrix2 )

print "===Testing add_edge With New Matrix==="
matrix3 = new_matrix(0, 4)
add_edge(matrix3, 0, 7, 0, 4, 2, 0)
print_matrix( matrix3 )

print "===Testing Matrix Multiplication==="
print "Result With Identity Matrix:"
matrix_mult( matrix2, matrix3 )
print_matrix( matrix3 )

print "Multiplying This Matrix:"
matrix4 = new_matrix(0, 4)
add_edge(matrix4, 1, 3, 0, 5, 9, 0)
add_edge(matrix4, 4, 2, 0, 6, 3, 0)
print_matrix( matrix4 )

print "4x4 X 4x2 Result:"
matrix_mult( matrix4, matrix3 )
print_matrix( matrix3 )


print "===Creating Image==="
matrix = new_matrix(0, 4)

for i in range(0, XRES/5, 6):
    x = (XRES/6 + i)
    y = (YRES/6 + i)
    add_edge(matrix, x - 60, y - 50, 0, x - 60, y - 40, 0 )
    add_edge(matrix, x - 60, y - 50, 0, x - 56, y - 50, 0 )
    add_edge(matrix, x - 60, y - 40, 0, x - 56, y - 40, 0 )
    add_edge(matrix, x - 56, y - 50, 0, x - 56, y - 40, 0 )

display(screen)
save_extension(screen, 'img.png')
