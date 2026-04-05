class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #count = [0] * 10 ** 5
        #for num in nums:
        #    count[ord(str(num)) - ord(str(1))] += 1
        #print(count)
        #max_values = []
        #for max_val in range(0, k):
        #    max_count = max(count)
        #    max_values.append(count.index(max_count) + 1)
        #    count[count.index(max_count)] = 0
        #return max_values

        cd = {}
        for i in nums:
            cd[i] = 1 + cd.get(i, 0)

        cd_sorted = sorted(cd.items(), key=lambda x: x[1], reverse=True)
        res = []
        for i in cd_sorted:
            res.append(i[0])
        return res[0:k]
