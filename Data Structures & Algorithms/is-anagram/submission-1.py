class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #dict1 = {}
        #for letter in s:
        #    if letter in dict1:
        #        dict1[letter] = dict1.get(letter) + 1
        #    else:
        #        dict1[letter] = 1

        #dict2 = {}
        #for letter in t:
        #    if letter in dict2:
        #        dict2[letter] = dict2.get(letter) + 1
        #    else:
        #        dict2[letter] = 1

        #dict1 = dict(sorted(dict1.items()))
        #dict2 = dict(sorted(dict2.items()))

        #print(dict1)
        #print(dict2)
        #if dict1 == dict2:
        #    return True
        #else:
        #    return False
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
