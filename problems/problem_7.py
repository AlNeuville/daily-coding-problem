"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def solution(message):
    length = len(message)

    temp0 = 1
    temp1 = 1

    for i in range(2, length + 1):
        count = 0

        if message[i - 1] > '0':
            count = temp1

        if message[i - 2] == '1' or (message[i - 2] == '2' and message[i - 1] < '7'):
            count += temp0

        temp0 = temp1
        temp1 = count

    return temp1
