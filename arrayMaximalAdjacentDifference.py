"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
solution(inputArray) = 3.
"""
from numpy import diff


def solution(inputArray):
    return max(abs(diff(inputArray)))
    

if __name__ == '__main__':
    solution([2, 4, 1, 0])