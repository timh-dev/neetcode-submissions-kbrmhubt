class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1:
            return stones[0]
        
        while len(stones) > 1:
            
            smash = []
            for i in range(0, 2):
                inx = stones.index(max(stones))
                smash.append(stones.pop(inx))

            calc = smash[0] - smash[1]
            stones.append(calc)
            print(smash)
        return calc