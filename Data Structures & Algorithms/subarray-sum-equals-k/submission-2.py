
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        right = 0
        count_subarray = 0

        for n in nums:
            right += n
            left = right - k
            
            if left in prefix_sum:
                count_subarray += prefix_sum[left]
            
            prefix_sum[right] += 1

        return count_subarray
