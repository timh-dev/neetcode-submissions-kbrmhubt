class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        s = {}
        for i in nums:
            s[i] = 1 + s.get(i, 0)

        print(s)

        for i in s.items():
            if i[1] == 1:
                return i[0]