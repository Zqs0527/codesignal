# %%
s = "abcsd"

# %%
t = s[::-1]

# %%
t

# %%
sequence = [1, 2, 1, 2]

# %%
sequence[:2]

# %%
sequence[2:]

# %%
# increasing_sequence(sequence[:2]) and increasing_sequence(sequence[2:])

# %%
def increasing_sequence(splitted_sequence):
        if len(splitted_sequence) == 2:
            if splitted_sequence[1] - splitted_sequence[0] > 0:
                return True
            else:
                return False
        else:
            for i in range(len(splitted_sequence)-1):
                if splitted_sequence[i+1] < splitted_sequence[i]:
                    return False
                else:
                    return True
def solution(sequence):
    if len(sequence)<=2:
        return True
        
    for i in range(len(sequence)-1):
        if sequence[i+1] < sequence[i]:
            seq_1 = sequence[:i+1]
            seq_2 = sequence[i+1:]
            if increasing_sequence(seq_1) and increasing_sequence(seq_2):
                return True
            else:
                return False
        else:
            continue
    return True

# %%
solution(sequence)

# %%
def solution_1(sequence):
    removed_one = False
    prev_maxval = None
    maxval = None
    for s in sequence:
        if not maxval or s > maxval:
            prev_maxval = maxval
            maxval = s
        elif not prev_maxval or s > prev_maxval:
            if removed_one:
                return False
            removed_one = True
            maxval = s
        else:
            if removed_one:
                return False
            removed_one = True
    return True

# %%
solution_1(sequence)

# %%
import numpy as np
matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]


# %%
def find_zero_index(matrix):
    list_of_index = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                list_of_index.append((i,j))
    return list_of_index
# %%
find_zero_index(matrix)
# %%
def solution(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0 and i+1 < len(matrix):
                matrix[i+1][j] = 0
            count += matrix[i][j]  
    
    return count
# %%
matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
# %%
solution(matrix)
# %%
s1="aabcc"
s2="adcaa"

# %%
def solution(s1, s2):
    dic1 = {chara : s1.count(chara) for chara in set(s1)}
    dic2 = {chara : s2.count(chara) for chara in set(s2)}
    
    return sum(min(dic1[x], dic2[x]) for x in dic1.keys() & dic2.keys())
# %%
solution(s1,s2)