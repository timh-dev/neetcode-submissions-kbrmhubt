class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #dup_list = list(set(nums))
        #if len(nums) == len(dup_list):
        #    return False
        #else:
        #    return True

        #for i in range(len(nums)):
        #    for j in range(i + 1, len(nums)):
        #        if nums[i] == nums[j]: 
        #            return True
        #return False

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False



