class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return count_char(s) == count_char(t)
    
def count_char(s):
    count_dict = {}

    for char in s:
        if char not in count_dict:
            count_dict[char] = 0
        count_dict[char] +=1

    return count_dict
        