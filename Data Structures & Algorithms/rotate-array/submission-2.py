class Solution:
    def reverse(self, a, left, right):

        while left < right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1, 2, 3, 4, 5, 6, 7 k = 3
        5, 6, 7, 1, 2, 3, 4
        7, 6, 5, 4, 3, 2, 1
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)