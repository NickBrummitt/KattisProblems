"""
    File name: FizzBuzz.py
    Author: Nicholas Brummitt
    Date created: 07/08/2021 (DD/MM/YYYY)
    Date last modified: 07/08/2021
    Python Version: 3.8

DESCRIPTION:
    According to Wikipedia, FizzBuzz is a group word game for children to teach them about division. This may or may
    not be true, but this question is generally used to torture screen young computer science graduates during
    programming interviews.

    Basically, this is how it works: you print the integers from 1 to N, replacing any of them divisible by X with Fizz
    or, if they are divisible by Y, with Buzz. If the number is divisible by both X and Y, you print FizzBuzz instead.


INPUT:
    Input contains a single test case. Each test case contains three integers on a single line, X, Y and N (1≤X<Y≤N≤100).


OUTPUT:
    Print integers from 1 to N in order, each on its own line, replacing the ones divisible by X with Fizz, the ones
    divisible by Y with Buzz and ones divisible by both X and Y with FizzBuzz.


EXAMPLES:
    (1)
    Input:                          Output:
    2 3 7                           1
                                    Fizz
                                    Buzz
                                    Fizz
                                    5
                                    FizzBuzz
                                    7

    (2)
    Input:                          Output:
    2 4 7                           1
                                    Fizz
                                    3
                                    FizzBuzz
                                    5
                                    Fizz
                                    7

    (3)
    Input:                          Output:
    3 5 7                           1
                                    2
                                    Fizz
                                    4
                                    Buzz
                                    Fizz
                                    7

"""

X = "Fizz"
Y = "Buzz"
XY = "FizzBuzz"

n = [int(x) for x in input().split()]


for i in range(1, n[2] + 1):
    if i % n[0] == 0:
        if i % n[1] == 0:
            print(XY)
        else:
            print(X)
    elif i % n[1] == 0:
        print(Y)
    else:
        print(i)