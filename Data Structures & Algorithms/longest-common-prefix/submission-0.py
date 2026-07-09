class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = strs[0]
        for s in strs:
            if len(s) < len(shortest):
                shortest = s
        
        sol = ""
        for i in range(len(shortest)):
            for j in strs:
                if j[i] != shortest[i]:
                    return sol
            sol += shortest[i]
        return sol
