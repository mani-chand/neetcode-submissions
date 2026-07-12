class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num,0) + 1
        desc_nums = {k: v for k, v in sorted(nums_dict.items(), key=lambda item: item[1], reverse=True)}
        return list(desc_nums.keys())[:k]
        
        