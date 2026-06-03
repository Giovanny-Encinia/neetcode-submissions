from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        K = 2
        ADADDACJJJALLIIOOAX
        ADCJKIOX
        AAAAAAAAAAAAAAAABB
        WHAT ARE THE MOST FREQUENT LETTER?
        WE CAN USE THIS TO CREATE THE MAX LEN SUBS
        CONTAINING ONE DISTINCT CHAR
        FIRST SEARCH THE TOP MOST FREQUENT LETTERS
        WHAT ARE THE DISTANCES BETWEEN THIS LETTERS
        CAN I FILL THE DISTANCES USING K?
        """
        if not s:
            return 0
        
        left = 0
        max_len = 1
        countletters = defaultdict(int)

        for right in range(len(s)):
            countletters[s[right]] += 1

            while right - left + 1 - max(countletters.values()) > k:
                print(left)
                countletters[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
        