class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = []
        d = {}
        for s in strs:
            sort.append("".join(sorted(s)))
        for i in range(len(sort)):
            s = sort[i]
            if s in d:
                d[s].append(strs[i])
            else:
                d[s] = [strs[i]] 
        ret = []
        for s in d:
            ret.append(d[s])
        return ret