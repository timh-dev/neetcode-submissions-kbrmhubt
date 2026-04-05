class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        r = len(s) - 1
        if len(s) == 1:
            return 1
        
        seen = set()
        max_count = 0
        count = 0
        while l < r:
            print(s[l:r + 1])
            for val in s[l:r + 1]:
                if val not in seen:
                    seen.add(val)
                    count += 1
                    max_count = max(max_count, count)
                else:
                    max_count = max(max_count, count)
                    count = 0
                    seen = set()
                    #seen = set(val)
            l += 1
        return max_count