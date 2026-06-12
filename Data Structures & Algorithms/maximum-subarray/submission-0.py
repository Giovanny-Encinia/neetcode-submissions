class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        global_sum = float("-inf")
        current_sum = float("-inf")

        for n in nums:
            current_sum = max(n, n + current_sum)
            global_sum = max(current_sum, global_sum)
        
        return global_sum