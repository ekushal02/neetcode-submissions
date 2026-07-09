class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = {}
        for i in s:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        hash_map2 = {}
        for i in t:
            if i not in hash_map2:
                hash_map2[i] = 1
            else:
                hash_map2[i] += 1 

        return hash_map == hash_map2 
