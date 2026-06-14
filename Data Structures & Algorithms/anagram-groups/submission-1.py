class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        seen = set()
        for i in range(len(strs)):
            if i in seen:
                continue
            outer = {}
            word = strs[i]
            group = [word]
            for c in word:
                outer[c] = outer.get(c, 0) + 1
            
            seen.add(i)
            for j in range(i + 1, len(strs)):
                if j in seen:
                    continue
                inner = {}
                word = strs[j]
                for c in word:
                    inner[c] = inner.get(c, 0) + 1
                if inner == outer:
                    group.append(word)
                    seen.add(j)

            groups.append(group)
        return groups