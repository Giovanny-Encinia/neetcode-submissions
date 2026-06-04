
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1dict = defaultdict(int)
        s2dict = defaultdict(int)

        for letter in s1:
            s1dict[letter] = s1dict.get(letter, 0) + 1

        for i in range(len(s1)):
            s2dict[s2[i]] = s2dict.get(s2[i], 0) + 1

        left = 0
        end = len(s2)
        # 4 - 3 = 1
        for right in range(len(s1) - 1, end):

            if left > 0:
                s2dict[s2[left - 1]] -= 1
                s2dict[s2[right]] += 1

                if s2dict[s2[left - 1]] == 0:
                    del s2dict[s2[left - 1]]

            #print(s2dict)
            if s2dict == s1dict:
                return True
            
            left += 1
        
        return False
