
"""Example:
Input: "abcabcbb" → Output: 3 (the answer is "abc")
Input: "bbbbb" → Output: 1 (the answer is "b")
Input: "pwwkew" → Output: 3 (the answer is "wke" — note "pwke" is a subsequence, not a substring, so it doesn't count)
"""
from collections import defaultdict

def length_of_longest_substring(s: str) -> int:
    right=0
    left=0
    result=[]
    sub_dict=defaultdict()
    for letter in s:
        print(letter)
        if letter not in result:
            result.append(letter)
            right=right+1
        else:
            while letter in result:
                print(letter)
                result.pop(left)
                left=left+1
            result.append(letter)

    print(result)
    return len(result)


print(length_of_longest_substring("dvdf"))













# def length_of_longest_substring(s: str) -> int:
#     right=0
#     left=0
#     result=[]
#     maxl=0
#     for i in range(len(s)):

#         if s[i] not in result:
#             right=right+1
                    
#         else:
#             while s[i] in result:
#                 result.remove(s[left])
#                 left=left+1

#             maxl=max(maxl,len(result))
#         result.append(s[i])

#         print(right,left,result)

#     maxl=max(maxl,len(result))
#     return maxl


# print(length_of_longest_substring("abba"))

