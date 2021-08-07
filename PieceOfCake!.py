"""
DESCRIPTION:
    It is Greg’s birthday! To celebrate, his friend Sam invites Greg and two other friends for a small party. Of course,
     every birthday party must have cake.

    Sam ordered a square cake. She makes a single horizontal cut and a single vertical cut. In her excitement to eat
    cake, Sam forgot to make these cuts through the middle of the cake.

    Of course, the biggest piece of cake should go to Greg since it is his birthday. Help Sam determine the volume of
    the biggest piece of cake that resulted from these two cuts.

INPUT:
    The input consists of a single line containing three integers n (2≤n≤10000), the length of the sides of the square
    cake in centimeters, h (0<h<n), the distance of the horizontal cut from the top edge of the cake in centimeters,
    and v (0<v<n), the distance of the vertical cut from the left edge of the cake in centimeters. This is illustrated
    in the figure above.

    Each cake is 4 centimeters thick.

OUTPUT:
    Display the volume (in cubic centimeters) of the largest of the four pieces of cake after the horizontal and
    vertical cuts are made.

EXAMPLES:
    (1)
    Input:              Output:
    10 4 7              168

    (2)
    Input:              Output:
    5 2 2               36

    (3)
    Input:              Output:
    4 2 1               24
"""

global x, y;
n, h, v = [int(i) for i in input().split()]

if h < n/2:
    y = n - h
elif h > n/2:
    y = h
else:
    y = n/2

if v < n / 2:
    x = n - v
elif v > n / 2:
    x = v
else:
    x = n / 2

sol = int(4 * x * y)

print(sol)