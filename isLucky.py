"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
"""
def solution(n):
    string = str(n)
    length = len(string)
    if length == 2:
        return string[0] == string[1]
    return sum([int(x) for x in string[:int(length/2)]])==sum([int(x) for x in string[int(length/2):]])


'''
def solution(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    return sum(map(int, left)) == sum(map(int, right))
'''

if __name__ == '__main__':
    solution(1023)
