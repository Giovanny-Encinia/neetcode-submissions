from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = set()
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

            if count[n] > len(nums) // 3:
                result.add(n)
        
        return list(result)
