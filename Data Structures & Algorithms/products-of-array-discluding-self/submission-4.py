class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        l = 0
        r = len(nums)
        prod = 1
        res = []
        while l < r:
            for i in range(0, len(nums)):
                if l != i:
                    prod *= nums[i]
            res.append(prod)
            prod = 1
            l += 1
        return res