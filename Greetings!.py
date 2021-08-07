"""
    File name: Greetings!.py
    Author: Nicholas Brummitt
    Date created: 06/08/2021 (DD/MM/YYYY)
    Date last modified: 06/08/2021
    Python Version: 3.8

DESCRIPTION:
    Now that Snapchat and Slingshot are soooo 2018, the teenagers of the world have all switched to the new hot app
    called BAPC (Bidirectional and Private Communication). This app has some stricter social rules than previous
    iterations. For example, if someone says goodbye using Later!, the other person is expected to reply with Alligator!
    You can not keep track of all these social conventions and decide to automate any necessary responses, starting with
    the most important one: the greetings. When your conversational partner opens with he...ey, you have to respond with
    he...ey as well, but using twice as many e’s!

    Given a string of the form he...ey of length at most 1000, print the greeting you will respond with, containing twice
    as many e’s.


INPUT:
    The input consists of one line containing a single string s as specified, of length at least 3 and at most 1000.


OUTPUT:
    Output the required response.


EXAMPLES:
    (1)
    Input:                          Output:
    hey                             heey

    (2)
    Input:                          Output:
    heeeeey                         heeeeeeeeeey

"""

n = str(input().strip().lower())

temp_index = n.find("y")

for i in range(1, temp_index):
    index = n.find("y")
    n = n[:index] + "e" + n[index:]

print(n)