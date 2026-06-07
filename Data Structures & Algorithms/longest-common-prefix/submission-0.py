class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        size = len(strs[0])
        prefix = strs[0]

        for word in strs:
            next_w = word[:size]

            while prefix != word[:size]:
                size -= 1
                prefix = prefix[:size]
        
        return prefix