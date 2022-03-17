"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

solution(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""
# def solution(picture):
#     top_bottom_frame = ""
#     framed_picture = []

#     for i in range(len(picture)):
#         if i == 0:
#             top_bottom_frame = '*' * (len(picture[0])+2)
#             framed_picture.append(top_bottom_frame)

#         framed_str = '*' + picture[i] + '*'
#         framed_picture.append(framed_str)

#         if i == len(picture)-1:
#             framed_picture.append(top_bottom_frame)

#     return framed_picture

def solution(picture):
    l=len(picture[0])+2
    return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l]

if __name__ == '__main__':
     solution(["abc",
           "ded"])