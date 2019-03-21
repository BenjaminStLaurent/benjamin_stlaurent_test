import sys

'''
Input : x1 => integer
        x2 => integer
        x3 => integer
        x4 => integer

Test cases : 

(0, 2) (1, 3) => true
(0, 1) (2, 3) => false
(4, 1) (3, 2) => true
(0, 0) (0, 0) => true
(0, 1) (1, 2) => false
(-4, -2) (-3, -1) => true

I'm assuming that when the end of line 1 and the start of line 2 
it doesn't count as intersecting. 
If the lines are just points (0, 0) and are on the exact same point,
it counts as intersecting.

I'm also assuming that inputs are valid. (QuestionA.py x1 x2 x3 x4)
All Xs must be integers

Output: True (The lines intersect) False (The lines don't intersect)

'''


def rotate_points(x1, x2):
    if x1 > x2:
        return (x2, x1)
    else:
        return (x1, x2)


def check_if_between(point_a, point_b):
    if point_a[0] < point_b[0]:
        if point_a[1] <= point_b[0]:
            return False
    elif point_b[0] < point_a[0]:
        if point_b[1] <= point_a[0]:
            return False

    return True


pointA_x1 = sys.argv[1]
pointA_x2 = sys.argv[2]
pointB_x1 = sys.argv[3]
pointB_x2 = sys.argv[4]

pointA = rotate_points(pointA_x1, pointA_x2)
pointB = rotate_points(pointB_x1, pointB_x2)

print(check_if_between(pointA, pointB))
