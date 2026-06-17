class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        suma = 0
        prefix_sum = []

        for n in nums:
            suma += n
            prefix_sum.append(suma)

        for pivot in range(len(nums)):
            if pivot == 0:
                result = prefix_sum[-1] - prefix_sum[0]
            elif pivot == len(nums) - 1:
                result = prefix_sum[-2]
            else:
                left = prefix_sum[pivot - 1]
                right = prefix_sum[-1] - prefix_sum[pivot]
                result = right - left

            if result == 0:
                return pivot
        
        return -1
        