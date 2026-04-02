class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        dict_struc = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        for c in s:
            if c in dict_struc:
                if stack and stack[-1] == dict_struc[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False