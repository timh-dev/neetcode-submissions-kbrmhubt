class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        l = 0
        r = len(temperatures) - 1

        #count = 0
        res = []
        while l < r:

            count = 0
            for i in range(l, r):
                count += 1
                if temperatures[l] >= temperatures[i + 1]:
                    #print(f"t1: {temperatures[l]}")
                    #print(f"t2: {temperatures[i + 1]}")

                    if temperatures[l] >= temperatures[i + 1] and (i + 1) == r:
                        print(i)
                        print(r)
                        count = 0
                    
                    continue
                else:
                    if temperatures[l] > temperatures[i + 1] and (i) == r:
                        print(i)
                        print(r)
                        count = 0
                    break
                

            res.append(count)
            l += 1
        res.append(0)

        return res