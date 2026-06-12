from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        numbers = defaultdict(int)
        for i, n in enumerate(nums):

            if n in numbers and i - numbers[n] <= k:
                return True

            numbers[n] = i

        return False