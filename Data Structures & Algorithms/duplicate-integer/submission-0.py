class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dup_list = list(set(nums))
        if len(nums) == len(dup_list):
            return False
        else:
            return True