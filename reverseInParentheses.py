"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
"""
def solution(inputString):
    chars = list(inputString)
    open_bracket_indexes = []
    for i, c in enumerate(chars):
        if c == '(':
            open_bracket_indexes.append(i)
        elif c == ')':
            j = open_bracket_indexes.pop()
            chars[j:i] = chars[i:j:-1]
        
    return ''.join(c for c in chars if c not in '()')

# def solution(s):
#     for i in range(len(s)):
#         if s[i] == "(":
#             start = i
#         if s[i] == ")":
#             end = i
#             return solution(s[:start] + s[start+1:end][::-1] + s[end+1:])
#     return s

#     start_index, end_index = get_index(inputString)
    
#     for i, j in zip(start_index, end_index):
#         str = inputString[i+1:j][::-1]
#         inputString[i+1:j] = str

#     return inputString


# def get_index(input_string):
#     i = 0
#     start_index = []
#     end_index = []
#     for c in input_string:
#         if c == '(':
#             start_index.append(i)
#         if c == ')':
#             end_index.append(i)
#         i += 1
#     return start_index, end_index
           

if __name__ == '__main__':
    t= solution("foo(bar)baz")