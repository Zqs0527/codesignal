"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
"""

def solution(inputString):
    x = map(lambda x: inputString.count(x) % 2, set(inputString))
    print(list(x))
    return sum(map(lambda x: inputString.count(x) % 2, set(inputString))) <= 1



if __name__ == '__main__':
    solution('aacbb')