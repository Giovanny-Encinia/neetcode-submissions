class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 1
        left = 0

        if not s:
            return 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            current_size = right - left + 1
            max_len = max(current_size, max_len)
        return max_len

        