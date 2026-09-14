from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = [False] * len(strs)  # Tracks which words are already grouped

        for i in range(len(strs)):
            if seen[i]:
                continue
            group = [strs[i]]
            seen[i] = True
            for j in range(i + 1, len(strs)):
                if not seen[j] and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    seen[j] = True
            result.append(group)
        
        return result
