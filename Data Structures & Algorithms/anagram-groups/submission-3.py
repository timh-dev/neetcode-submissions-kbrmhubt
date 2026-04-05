class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #new_list = {}
        #for i in range(0, len(strs)):
        #    new = ""
        #    str_sort = sorted(strs[i])
        #    for s in str_sort:
        #        new += s 
        #    new_list[strs[i]] = new
#
        #a = []
        #for key1, value1 in new_list.items():
        #    b = []
        #    for key2, value2 in new_list.items():
        #        if value1 == value2:
        #            if key1 not in b:
        #                b.append(key1)
        #            if key2 not in b:
        #                b.append(key2)
        #    b.sort()
        #    if b not in a:
        #        a.append(b)
        #return a

        res = defaultdict(list)
        print(res)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            print(count)
            res[tuple(count)].append(s)
        return list(res.values())
   


