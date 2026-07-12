class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_freq = {}
        for num in nums:
            if num in num_freq:
                return True
            num_freq[num] = True
        return False
        