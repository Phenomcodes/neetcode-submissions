class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i, j in set(zip(sorted(s), sorted(t))):
            if i != j:
                return False
                #break
        return True

        # return count_char(s) == count_char(t)
    
# def count_char(s):
#     count_dict = {}

#     for char in s:
#         if char not in count_dict:
#             count_dict[char] = 0
#         count_dict[char] +=1

#     return count_dict
        