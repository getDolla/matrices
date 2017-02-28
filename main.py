from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print "Testing Identity Matrix Creation..."
ident( matrix )

print "Displaying Matrix:"
print_matrix( matrix )

print "\nScalar Matrix Multiplication (7 * matrix):"
scalar_mult( matrix, 7 )
print_matrix( matrix )

matrix2 = new_matrix()
ident( matrix2 )

print "\nTesting add_edge With New Matrix (m2):"
matrix3 = new_matrix(0, 4)
add_edge(matrix3, 0, 7, 0, 4, 2, 0)
print_matrix( matrix3 )

print "\nTesting Matrix Multiplication:"
print "Result With 4x4 Identity Matrix:"
matrix_mult( matrix2, matrix3 )
print_matrix( matrix3 )

print "\nMultiplying With This Matrix (m1):"
matrix4 = new_matrix(0, 4)
add_edge(matrix4, 1, 3, 0, 5, 9, 0)
add_edge(matrix4, 4, 2, 0, 6, 3, 0)
print_matrix( matrix4 )

print "\nResult (m1 * m2):"
matrix_mult( matrix4, matrix3 )
print_matrix( matrix3 )


print "Creating Image..."
matrix = new_matrix(0, 4)

add_edge(matrix, XRES/2, YRES, 0, XRES, 7*YRES/8, 0 )
add_edge(matrix, 0, 7*YRES/8, 0, XRES/2, YRES, 0 )
add_edge(matrix, 0, 7*YRES/8, 0, XRES/2, 3*YRES/4, 0 )
add_edge(matrix, XRES/2, 3*YRES/4, 0, XRES, 7*YRES/8, 0 )

diff = 2
for i in range(0, 3*YRES/4, 2):
    add_edge(matrix, diff, 7*YRES/8 - i, 0, XRES/2, 3*YRES/4 - i, 0 )
    add_edge(matrix, XRES/2, 3*YRES/4 - i, 0, XRES - diff, 7*YRES/8 - i, 0 )
    diff += 2

draw_lines( matrix, screen, color)

display(screen)
save_extension(screen, 'img.png')
