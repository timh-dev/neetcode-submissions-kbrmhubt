class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        def happy(val):
            if val == 1:
                return True
            if val in seen:
                return False
            seen.add(val)

            total = sum(int(digit) ** 2 for digit in str(val))

            return happy(total)

        return happy(n)
