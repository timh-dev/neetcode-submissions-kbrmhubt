class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = ""
        for d in digits:
            s += str(d)

        s = int(s) + 1
        s = str(s)

        tmp = []
        for c in s:
            tmp.append(int(c))
        return tmp