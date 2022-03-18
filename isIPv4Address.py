"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
solution(inputString) = true;

For inputString = "172.316.254.1", the output should be
solution(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
solution(inputString) = false.

There is no first number.
"""

import numpy


def solution(inputString):
    
    list_of_string = inputString.split('.')
    for x in list_of_string:
        if not x.isnumeric():
            return False
    if len(list_of_string) != 4:
        return False
    list_of_numbers = [x for x in list_of_string if int(x) > 255]
    if len(list_of_numbers) > 0:
        return False
    list_start_with_zero = [x.startswith('0') for x in list_of_string if len(list(x)) > 1]

    if numpy.any(list_start_with_zero):
        return False

    return True

# p = s.split('.')

# return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)

if __name__ == '__main__':
    solution(".254.255.0")