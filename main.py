
def main():
    # Initialize empty lists to store the quardrilateral
    # quardrilateral = []
    quardrilateral = [(1,1), (-1,1), (-1,-1), (-1,1)]

    # quardrilateral = get_coordinates()

    # print("Collected Coordinates:")
    # for i, (x, y) in enumerate(quardrilateral, 1):
    #     print(f"Point {i}: x = {x}, y = {y}")

    check_properties(quardrilateral)

def get_coordinates():
    # Initialize empty lists to store the quardrilateral
    coordinates = []

    print("Enter comma-separated coordinates in anticlockwise order:")

    # Loop to input and save coordinates for each point
    for i in range(1, 5):
        while True:
            # Get user input for each coordinate in the format 'x,y'
            coordinate_str = input(f"Vertex {i}: ")

            # Split the input into x and y values
            x_str, y_str = coordinate_str.split(',')

             # Try to convert x and y to floating-point numbers
            try:
                x = float(x_str)
                y = float(y_str)
                coordinates.append((x, y))
                break
            except ValueError:
                print("Invalid input. Please enter valid numeric coordinates.")

    # print("Collected Coordinates:")
    # for i, (x, y) in enumerate(coordinates, 1):
    #     print(f"Point {i}: x = {x}, y = {y}")

    return coordinates


def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def is_parallel(side1, side2):
    return abs(side1 - side2) < 1e-6

def is_perpendicular(diagonal1, diagonal2):
    return abs(diagonal1 * diagonal2) < 1e-6

def midpoint(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def check_properties(coordinates):
    # Calculate side lengths
    # The use of (i + 1) % 4 ensures that the calculation wraps around from the last point to the first point to close the quadrilateral.
    sides = [distance(coordinates[i], coordinates[(i + 1) % 4]) for i in range(4)]
    print(sides)

    # Calculate diagonal lengths
    diagonals = [distance(coordinates[0], coordinates[2]), distance(coordinates[1], coordinates[3])]
    print(diagonals)

    # Check properties
    parallel_sides = is_parallel(sides[0], sides[2])
    two_pairs_parallel_sides = parallel_sides and is_parallel(sides[1], sides[3])
    equal_sides = all(is_parallel(sides[0], s) for s in sides)
    right_angles = is_perpendicular(diagonals[0], diagonals[1])
    two_pairs_equal_sides = is_parallel(sides[0], sides[1]) and is_parallel(sides[2], sides[3])
    perpendicular_diagonals = is_perpendicular(diagonals[0], diagonals[1])
    one_diagonal_bisects_another = midpoint(coordinates[0], coordinates[2]) == midpoint(coordinates[1], coordinates[3])
    both_diagonals_bisect_each_other = midpoint(coordinates[0], coordinates[2]) == midpoint(coordinates[1], coordinates[3]) and midpoint(coordinates[0], coordinates[1]) == midpoint(coordinates[2], coordinates[3])
    one_diagonal_bisects_angles = is_perpendicular(distance(coordinates[0], midpoint(coordinates[1], coordinates[3])), distance(coordinates[1], midpoint(coordinates[0], coordinates[2])))
    both_diagonals_bisect_angles = one_diagonal_bisects_angles and is_perpendicular(distance(coordinates[0], midpoint(coordinates[1], coordinates[3])), distance(coordinates[2], midpoint(coordinates[0], coordinates[1])))
    diagonals_equal_length = is_parallel(diagonals[0], diagonals[1])

    # Output results
    print("Properties of the quadrilateral:")
    print(f"One pair of parallel sides: {parallel_sides}")
    print(f"Two pairs of parallel sides: {two_pairs_parallel_sides}")
    print(f"All sides equal: {equal_sides}")
    print(f"All angles 90 degrees: {right_angles}")
    print(f"Two pairs of adjacent equal sides: {two_pairs_equal_sides}")
    print(f"Perpendicularity of diagonals: {perpendicular_diagonals}")
    print(f"One diagonal bisecting another: {one_diagonal_bisects_another}")
    print(f"Both diagonals bisecting each other: {both_diagonals_bisect_each_other}")
    print(f"One diagonal bisecting the angles it passes through: {one_diagonal_bisects_angles}")
    print(f"Both diagonals bisecting the angles they pass through: {both_diagonals_bisect_angles}")
    print(f"Diagonals being equal in length: {diagonals_equal_length}")

if __name__ == "__main__":
    main()