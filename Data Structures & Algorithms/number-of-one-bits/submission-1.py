class Solution:
    def hammingWeight(self, n: int) -> int:

        a = bin(n)

        res = 0
        for i in range(2, len(a)):
            print(a[i])
            if a[i] == "1":
                res += 1
        return res
        
        #res = 0
        #for i in range(32):
        #    if (1 << i) & n:
        #        res += 1
        #return res