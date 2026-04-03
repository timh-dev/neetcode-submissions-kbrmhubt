class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # brute force
        #prod = 1
        #res = []
        #for i in range(0, len(nums)):
        #    for j in range(0, len(nums)):
        #        if j != i:
        #            prod *= nums[j]
        #    res.append(prod)
        #    prod = 1
        #return res

        
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