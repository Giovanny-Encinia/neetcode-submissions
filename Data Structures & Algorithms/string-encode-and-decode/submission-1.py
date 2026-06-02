
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for word in strs:
            r = str(len(word)) + "#" + word
            encoded.append(r)
        
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):

            length_end = int(s.find("#", i))

            length = int(s[i:length_end])
            start = length_end + 1
            end = start + length
            word = s[start:end]

            result.append(word)

            i = end

        return result


