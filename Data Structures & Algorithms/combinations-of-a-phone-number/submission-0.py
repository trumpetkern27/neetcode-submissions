class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def recursiveFor(idx):
            arr = []
            if idx == len(digits):
                return arr
            for c in map[digits[idx]]:
                cs = recursiveFor(idx + 1)
                if len(cs) == 0:
                    arr.append(c)
                    continue
                for c2 in cs:
                    arr.append(c + c2)
            return arr

        return recursiveFor(0)
        