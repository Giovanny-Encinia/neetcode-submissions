from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        history = defaultdict(int)
        history[0] = 1
        result = 0
        suma = 0
        for n in nums:
            suma += n
            previous_sub = suma - k

            if previous_sub in history:
                result += history[previous_sub]
            
            history[suma] += 1

        return result
        