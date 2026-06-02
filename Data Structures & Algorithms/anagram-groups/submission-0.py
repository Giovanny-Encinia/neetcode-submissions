from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for an in strs:

            word_key = tuple(sorted(an))

            anagrams[word_key].append(an)
        
        return [values for values in anagrams.values()]

