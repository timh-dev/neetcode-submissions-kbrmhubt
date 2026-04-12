class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        res = ""
        tmp = []
        for i in range(0, len(nums)):
            if i != nums[i]:
                tmp.append(i)
                res = i

        print(res)

        if res == "":
            return nums[-1] + 1
        else:
            return tmp[0]