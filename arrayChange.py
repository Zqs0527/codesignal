"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3.
"""

def solution(inputArray):
    moves = 0
    for i in range(1,len(inputArray)):
        if inputArray[i] <= inputArray[i-1]:
            #moves to increase to one number greater than previous
            moves += inputArray[i-1] - inputArray[i] + 1
            #modify current to previous plus one
            inputArray[i] = inputArray[i-1] + 1
    return moves


if __name__ == "__main__":
    solution([1,3,1])