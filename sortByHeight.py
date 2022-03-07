"""
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""
def solution(n):
    sorted_list = sorted([i for i in n if i!=-1])
    pos = 0
    
    for i in range(len(n)):
        if n[i]== -1:
            continue
        n[i] = sorted_list[pos]
        pos += 1
        
    
    return n

if __name__=='__main__':
    solution([4, 2, 9, 11, 2, 16])