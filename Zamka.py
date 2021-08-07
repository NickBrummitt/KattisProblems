"""
DESCRIPTION:
The impossible has happened. Bear G. has fallen into his own trap. Lured by a delicious box of Domaćica, without even
 thinking, he rushed and fell into his trap. In order to get out of the trap, he must solve the following task with your
  help. You are given three integers L, D and X.

    -determine the minimal integer N such that L≤N≤D and the sum of its digits is X
    -determine the maximal integer M such that L≤M≤D and the sum of its digits is X

    Bear will be able to escape from the trap if he correctly determines numbers N and M.
    *The numbers N and M will always exist.

INPUT:
The first line of input contains the integer L (1≤L≤10000), the number from the task. The second line of input contains
 the integer D (1≤D≤10000, L≤D), the number from the task. The third line of input contains the integer X (1≤X≤36),
 the number from the task.

OUTPUT:
The first line of output must contain the integer N from the task. The second line of output must contain the integer M
from the task.

EXAMPLES:
    (1)
    Input:              Output:
    1                   4
    100                 40
    4

    (2)
    Input:              Output:
    100                 129
    500                 480
    12
"""

global X, min, max, minimal, maximal;

min = int(input());
max = int(input());
X = int(input());

temp_max = min;
temp_min = max;
maximal = temp_max;
minimal = temp_min;

# Find Min
while temp_min >= min:
    sep = [int(i) for i in str(temp_min)]
    s = sum(sep)

    if s == X:
        minimal = temp_min

    temp_min = temp_min - 1;

print(minimal)

# Find Max
while temp_max <= max:
    sep = [int(i) for i in str(temp_max)]
    s = sum(sep)

    if s == X:
        maximal = temp_max

    temp_max = temp_max + 1;

print(maximal)