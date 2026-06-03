class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """

        abdxddaax

        """
        if not s:
            return 0
        seen = set()
        left = 0
        max_len = 1

        for right in range(len(s)):
            while s[right] in seen and left < right:
                seen.remove(s[left])
                left += 1

            current_len = right - left + 1
            max_len = max(current_len, max_len)
            seen.add(s[right])
        return max_len
            
