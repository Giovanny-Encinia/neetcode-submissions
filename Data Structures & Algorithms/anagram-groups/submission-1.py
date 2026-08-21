from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            anagram_dict[key]
        
        for word in strs:
            key = tuple(sorted(word))
            anagram_dict[key].append(word)
        
        return list(anagram_dict.values())
