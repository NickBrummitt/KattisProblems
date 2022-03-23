"""
DESCRIPTION:
    George has bought a pizza. George loves cheese. George thinks the pizza does not have enough cheese. George gets angry.
    George’s pizza is round, and has a radius of R cm. The outermost C cm is crust, and does not have cheese. 
    What percent of George’s pizza has cheese?

INPUT:
    The input consists of a single line with two space separated integers, R and C.

OUTPUT:
    Output the percentage of the pizza that has cheese. Your answer must have an absolute or relative error of at most 10^−6.

EXAMPLES:
    (1)
    Input:              Output:
    1 1                 0.000000000

    (2)
    Input:              Output:
    2 1                 25.000000
"""
import math

r, c = [int(i) for i in input().split()]

cheeseArea = ((math.pi)*r)**2;

crustArea = ((math.pi)*(r-c))**2;

percentCheese = abs((cheeseArea/crustArea)*100);

print('{:.6f}'.format(percentCheese));
