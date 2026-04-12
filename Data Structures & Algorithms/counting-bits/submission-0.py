class Solution:
    def countBits(self, n: int) -> List[int]:
        

        a = bin(n)
        #print(a)

        res = []
        for i in range(0, n + 1):
            b = bin(i)
            count = 0
            for j in range(2, len(b)):
                if b[j] == "1":
                    count += 1
            res.append(count)
        return res