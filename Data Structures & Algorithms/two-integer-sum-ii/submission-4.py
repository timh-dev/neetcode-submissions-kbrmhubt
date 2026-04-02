class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # brute force
        #for i in range(0, len(numbers)):
        #    for j in range(i + 1, len(numbers)):

        #        if numbers[i] + numbers[j] == target:
        #            return [i + 1, j + 1]

        # pointer solution
        lp = 0 
        rp = len(numbers) - 1

        while lp < rp:

            if numbers[lp] + numbers[rp] == target:
                return [lp + 1, rp + 1]
            
            if numbers[lp] + numbers[rp] > target:
                rp -= 1

            if numbers[lp] + numbers[rp] < target:
                lp += 1