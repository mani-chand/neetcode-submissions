class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num
        res = []
        for num in nums:
            if zero_count == 0:
                res.append(product//num)
            elif zero_count == 1:
                if num == 0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                res.append(0)
        return res
        