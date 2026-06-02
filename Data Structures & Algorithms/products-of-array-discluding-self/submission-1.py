class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        pre = [1] * len(nums)
        post = [1] * len(nums)

        i = 1
        prod = 1
        while i < len(nums):
            pre[i] = nums[i - 1] * prod
            prod = pre[i]
            i += 1
        
        prod = 1
        j = len(nums) - 2
        while j >= 0:
            post[j] = nums[j + 1] * prod
            prod = post[j]
            j -= 1
        
        for i in range(len(nums)):
            output[i] = pre[i] * post[i]
        
        return output
