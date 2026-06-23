class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def dfs(nums, result, current_set, index):

            if index >= len(nums):
                result.append(current_set.copy())    

                return None

            current_set.append(nums[index])
            dfs(nums, result, current_set, index + 1)

            current_set.pop()

            while index+1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            dfs(nums, result, current_set, index + 1)

        result = []
        current_set = []
        dfs(nums, result, current_set, 0)
        return result
