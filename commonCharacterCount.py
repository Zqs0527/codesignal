"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""

def solution(s1, s2):
    dic1 = {chara : s1.count(chara) for chara in set(s1)}
    dic2 = {chara : s2.count(chara) for chara in set(s2)}
    
    return sum(min(dic1[x], dic2[x]) for x in dic1.keys() & dic2.keys())