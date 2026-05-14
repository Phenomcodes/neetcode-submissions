class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 0
            count_dict[num] += 1
        for k, v in count_dict.items():
            if v > 1:
                return True
        return False
        