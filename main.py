import math

def main():
    # Initialize empty lists to store the quadrilateral
    # quadrilateral = []
    # quadrilateral = [(1,1), (1,-1), (-1,-1), (-1,1)]

    quadrilateral = get_coordinates()

    quadrilateral = sort_points_anticlockwise(quadrilateral)

    # print(f"sorted quadrilateral={quadrilateral}")

    properties = get_properties(quadrilateral)

    # Output results
    print("Properties of the quadrilateral:")
    print(f"One pair of parallel sides: {properties['one_pair_parallel_sides']}")
    print(f"Two pairs of parallel sides: {properties['two_pairs_parallel_sides']}")
    print(f"All sides equal: {properties['all_sides_equal']}")
    print(f"All angles 90 degrees: {properties['all_angles_90_degrees']}")
    print(f"Two pairs of adjacent equal sides: {properties['two_pairs_of_adjacent_equal_sides']}")

    print(f"Perpendicularity of diagonals: {properties['diagonals_perpendicular']}")
    print(f"One diagonal bisecting another: {properties['one_diagonal_bisects_the_other']}")
    print(f"Both diagonals bisecting each other: {properties['both_diagonal_bisects_each_other']}")
    print(f"One diagonal bisecting the angles it passes through: {properties['one_diagonal_bisects_angle']}")
    print(f"Both diagonals bisecting the angles they pass through: {properties['both_diagonals_bisect_angles']}")
    print(f"Diagonals being equal in length: {properties['diagonals_equal']}")

    name = {
        "trapezium": False,
        "kite": False,
        "parallelogram": False,
        "rectangle": False,
        "rhombus": False,
        "square": False,
    }

    # Check side length and angle properties
    name["trapezium"] = properties["one_pair_parallel_sides"]

    name["kite"] = properties["two_pairs_of_adjacent_equal_sides"]

    name["parallelogram"] = properties["one_pair_parallel_sides"] and properties["two_pairs_parallel_sides"]

    name["rectangle"] = properties["one_pair_parallel_sides"] and properties["two_pairs_parallel_sides"] \
                        and properties["all_angles_90_degrees"]

    name["rhombus"] = properties["one_pair_parallel_sides"] and properties["two_pairs_parallel_sides"] \
                    and properties["all_sides_equal"] and properties["two_pairs_of_adjacent_equal_sides"]

    name["square"] = properties["one_pair_parallel_sides"] and properties["two_pairs_parallel_sides"] \
                    and properties["all_sides_equal"] and  properties["all_angles_90_degrees"] \
                    and properties["two_pairs_of_adjacent_equal_sides"]

    print("After checking side length and angle properties")
    print(f"name={name}")

    name["kite"] = properties["diagonals_perpendicular"] \
                    and properties["one_diagonal_bisects_the_other"]  \
                    and properties["one_diagonal_bisects_angle"]

    name["parallelogram"] = properties["one_diagonal_bisects_the_other"] and properties["both_diagonal_bisects_each_other"]

    name["rectangle"] = properties["one_diagonal_bisects_the_other"] and properties["both_diagonal_bisects_each_other"] \
                    and properties["diagonals_equal"]

    name["rhombus"] = properties["diagonals_perpendicular"] \
                    and properties["one_diagonal_bisects_the_other"] and properties["both_diagonal_bisects_each_other"] \
                    and properties["one_diagonal_bisects_angle"] and properties["both_diagonals_bisect_angles"]

    name["square"] = properties["diagonals_perpendicular"] \
                    and properties["one_diagonal_bisects_the_other"] and properties["both_diagonal_bisects_each_other"] \
                    and properties["one_diagonal_bisects_angle"] and properties["both_diagonals_bisect_angles"] \
                    and properties["diagonals_equal"]

    print("After checking properties of diagonals")
    print(f"name={name}")


def get_coordinates():
    # Initialize empty lists to store the quadrilateral
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

    return coordinates


def calculate_angle(point, centroid):
    x, y = point
    cx, cy = centroid

    # print(f"x={x}, y={y}, cx={cx}, cy={cy}, atan2={math.atan2(y - cy, x - cx)}, angle={math.atan2(y - cy, x - cx)*180/math.pi}")

    # math.atan2 return radian
    # angle = (radian*180)/pi
    return math.atan2(y - cy, x - cx)


def sort_points_anticlockwise(points):
    # Calculate the centroid
    cx = sum(x for x, y in points) / 4
    cy = sum(y for x, y in points) / 4

    # Calculate angles for each point with respect to the centroid
    angles = [(point, calculate_angle(point, (cx, cy))) for point in points]
    # print(f"angles={angles}")

    # Sort points based on angles in ascending order
    sorted_points = [point for point, angle in sorted(angles, key=lambda x: x[1])]

    return sorted_points


def calculate_slope(point1, point2):
    # Calculate the slope (gradient) of a line given two points
    # print(f"calculate_slope--point1={point1}, point2={point2}")
    if point1[0] == point2[0]:
        # Handling vertical lines (undefined slope)
        return float('inf')
    else:
        return (point2[1] - point1[1]) / (point2[0] - point1[0])


def is_parallel(line1, line2):
    # Check if two lines are parallel based on their slopes
    # print(f"line1={line1}, line2={line2}")

    slope1 = calculate_slope(line1[0], line1[1])
    slope2 = calculate_slope(line2[0], line2[1])
    # print(f"slope1={slope1}, slope2={slope2}")

    if (slope1 == float('inf') and slope2 == float('inf')):
        return True
    else:
        return abs(slope1 - slope2) < 1e-6

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def is_all_sides_equal(side1_length, side2_length, side3_length, side4_length):
    return abs(side1_length - side2_length) < 1e-6 and abs(side2_length - side3_length) < 1e-6 \
           and abs(side3_length - side4_length) < 1e-6


def is_two_pairs_of_adjacent_equal_sides(side1_length, side2_length, side3_length, side4_length):
    return abs(side1_length - side2_length) < 1e-6 and abs(side3_length - side4_length) < 1e-6


def is_right_angle(side1, side2, side3):
    sides = [side1, side2, side3]
    sides.sort()  # Sort the sides in ascending order
    a, b, c = sides

    # Check if it's a right angle by comparing the squares of the sides
    if abs(a**2 + b**2 - c**2) < 1e-6:
        return True
    else:
        return False


def is_all_angles_90_degrees(side1_length, side2_length, side3_length, side4_length, \
                                                             diagonal1_length, diagonal2_length):
    angle1 = is_right_angle(side1_length, side2_length, diagonal1_length)
    angle2 = is_right_angle(side2_length, side3_length, diagonal2_length)
    angle3 = is_right_angle(side3_length, side4_length, diagonal1_length)
    angle4 = is_right_angle(side4_length, side1_length, diagonal2_length)

    return angle1 and angle2 and angle3 and angle4


def is_diagonals_equal(diagonal1_length, diagonal2_length):
    return abs(diagonal1_length - diagonal2_length) < 1e-6



def is_perpendicular(line1, line2):
    slope1 = calculate_slope(line1[0], line1[1])
    slope2 = calculate_slope(line2[0], line2[1])

    if slope1 == 0 and slope2 == float('inf'):
        return True

    if slope1 == float('inf') and slope2 == 0:
        return True

    return slope1*slope2 == -1


def midpoint(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def do_lines_bisect_each_other(line1, line2):
    # Line1 represented by two points (x1, y1) and (x2, y2)
    x1, y1 = line1[0]
    x2, y2 = line1[1]

    # # Line2 represented by two points (x3, y3) and (x4, y4)
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    # Calculate the midpoint of Line1
    mid_x1 = (x1 + x2) / 2
    mid_y1 = (y1 + y2) / 2

    # Calculate the midpoint of Line2
    mid_x2 = (x3 + x4) / 2
    mid_y2 = (y3 + y4) / 2

    # Check if the midpoints coincide
    return abs(mid_x1 - mid_x2) < 1e-6 and abs(mid_y1 - mid_y2) < 1e-6


def does_line_bisect_the_other(line1, line2):
    # Line1 represented by two points (x1, y1) and (x2, y2)
    x1, y1 = line1[0]
    x2, y2 = line1[1]

    # # Line2 represented by two points (x3, y3) and (x4, y4)
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    # Calculate the midpoint of Line1
    mid_x1 = (x1 + x2) / 2
    mid_y1 = (y1 + y2) / 2

    # Calculate the equation of Line2: y = mx + b
    m2 = (y4 - y3) / (x4 - x3) if x4 - x3 != 0 else float('inf')  # Handle vertical lines
    b2 = y3 - m2 * x3 if x4 - x3 != 0 else None

    # Check if the midpoint of Line1 lies on Line2
    on_line2 = (x3 <= mid_x1 <= x4) and (y3 <= mid_y1 <= y4)
    if b2 is not None:
        on_line2 = on_line2 and abs(mid_y1 - (m2 * mid_x1 + b2)) < 1e-6
    else:
        # Handle vertical lines
        on_line2 = on_line2 and abs(mid_x1 - x3) < 1e-6 and abs(mid_y1 - (y3 + y4) / 2) < 1e-6

    # Calculate the midpoint of Line2
    mid_x2 = (x3 + x4) / 2
    mid_y2 = (y3 + y4) / 2

    # Calculate the equation of Line1: y = mx + b
    m1 = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf')  # Handle vertical lines
    b1 = y1 - m1 * x1 if x2 - x1 != 0 else None

    # Check if the midpoint of Line2 lies on Line1
    on_line1 = (x1 <= mid_x2 <= x2) and (y1 <= mid_y2 <= y2)
    if b1 is not None:
        on_line1 = on_line1 and abs(mid_y2 - (m1 * mid_x2 + b1)) < 1e-6
    else:
        # Handle vertical lines
        on_line1 = on_line1 and abs(mid_x2 - x2) < 1e-6 and abs(mid_y2 - (y1 + y2) / 2) < 1e-6

    # Return True if one line bisects the other
    return on_line2 or on_line1


def do_diagonals_bisect_angles(side1_length, side2_length, side3_length, side4_length, \
                                    diagonal1_length, diagonal2_length):
    # Use law of consines
    # quadrilateral ABCD
    cosCAB = (side1_length ** 2 + diagonal1_length ** 2 - side2_length ** 2) / 2 * side1_length * diagonal1_length
    cosCAD = (side4_length ** 2 + diagonal1_length ** 2 - side3_length ** 2) / 2 * side4_length * diagonal1_length

    cosACB = (side2_length ** 2 + diagonal1_length ** 2 - side1_length ** 2) / 2 * side2_length * diagonal1_length
    cosACD = (side3_length ** 2 + diagonal1_length ** 2 - side4_length ** 2) / 2 * side3_length * diagonal1_length

    diagonal1_bisects = abs(cosCAB - cosCAD) < 1e-6 and abs(cosACB - cosACD) < 1e-6

    cosABD = (side1_length ** 2 + diagonal2_length ** 2 - side4_length ** 2) / 2 * side1_length * diagonal2_length
    cosDBC = (side2_length ** 2 + diagonal2_length ** 2 - side3_length ** 2) / 2 * side2_length * diagonal2_length

    cosADB = (side4_length ** 2 + diagonal2_length ** 2 - side1_length ** 2) / 2 * side4_length * diagonal2_length
    cosBCD = (side3_length ** 2 + diagonal2_length ** 2 - side2_length ** 2) / 2 * side3_length * diagonal2_length

    diagonal2_bisects = abs(cosABD - cosDBC) < 1e-6 and abs(cosADB - cosBCD) < 1e-6

    return (diagonal1_bisects or diagonal2_bisects, diagonal1_bisects and diagonal2_bisects)


    # print(f"quadrilateral={quadrilateral}")

    properties = {
        "one_pair_parallel_sides": False,
        "two_pairs_parallel_sides": False,
        "all_sides_equal": False,
        "all_angles_90_degrees": False,
        "two_pairs_of_adjacent_equal_sides": False,
        "diagonals_perpendicular": False,
        "one_diagonal_bisects_the_other": False,
        "both_diagonal_bisects_each_other": False,
        "one_diagonal_bisects_angle": False,
        "both_diagonals_bisect_angles": False,
        "diagonals_equal": False,
    }

    side1 = [quadrilateral[0], quadrilateral[1]]
    side2 = [quadrilateral[1], quadrilateral[2]]
    side3 = [quadrilateral[2], quadrilateral[3]]
    side4 = [quadrilateral[3], quadrilateral[0]]

    side1_length = distance(side1[0], side1[1])
    side2_length = distance(side2[0], side2[1])
    side3_length = distance(side3[0], side3[1])
    side4_length = distance(side4[0], side4[1])

    diagonal1 = [quadrilateral[0], quadrilateral[2]]
    diagonal2 = [quadrilateral[1], quadrilateral[3]]

    # Calculate diagonal lengths
    diagonal1_length = distance(quadrilateral[0], quadrilateral[2])
    diagonal2_length  = distance(quadrilateral[1], quadrilateral[3])

    # Check properties
    properties["one_pair_parallel_sides"] = is_parallel(side1, side3)

    properties["two_pairs_parallel_sides"]  = properties["one_pair_parallel_sides"] and is_parallel(side2, side4)

    properties["all_sides_equal"] = is_all_sides_equal(side1_length, side2_length, side3_length, side4_length)

    properties["all_angles_90_degrees"] = is_all_angles_90_degrees(side1_length, side2_length, side3_length, side4_length,
                                                             diagonal1_length, diagonal2_length)

    properties["two_pairs_of_adjacent_equal_sides"] = \
        is_two_pairs_of_adjacent_equal_sides(side1_length, side2_length, side3_length, side4_length)

    properties["diagonals_perpendicular"] = is_perpendicular(diagonal1, diagonal2)
    properties["one_diagonal_bisects_the_other"] = does_line_bisect_the_other(diagonal1, diagonal2)
    properties["both_diagonal_bisects_each_other"] = do_lines_bisect_each_other(diagonal1, diagonal2)
    properties["one_diagonal_bisects_angle"], properties["both_diagonals_bisect_angles"] = \
        do_diagonals_bisect_angles(side1_length, side2_length, side3_length, side4_length, diagonal1_length, diagonal2_length)

    properties["diagonals_equal"]= is_diagonals_equal(diagonal1_length, diagonal2_length)

    return properties

if __name__ == "__main__":
    main()