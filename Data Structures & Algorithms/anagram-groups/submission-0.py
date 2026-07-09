class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            i = "".join(sorted(s))
            group[i].append(s)
        
        return list(group.values())