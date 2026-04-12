class Solution:
    def reverseBits(self, n: int) -> int:
        
        val = bin(n)
        val = val[2:]
        val = val[::-1]
        print(val)

        for i in range(0, 32 - len(val)):
            val += "0"

        return int(val, 2)