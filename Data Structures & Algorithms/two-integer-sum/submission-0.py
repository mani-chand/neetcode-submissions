class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        helper_dict = {}
        for i in range(len(nums)):
            if nums[i] in helper_dict:
                return [helper_dict[nums[i]], i]
            helper_dict[target - nums[i]] = i
        