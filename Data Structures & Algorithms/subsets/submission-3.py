class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
                      []
               [1]                          []
    [1, 2]                [1]            [2]   []
[1, 2, 3]  [1, 2]   [1, 3]  [1]         [2, 3]   []
    """
        def dfs(nums, results, current_subset, index):
            if index >= len(nums):
                results.append(current_subset[:])
                return None
            
            current_subset.append(nums[index])
            dfs(nums, results, current_subset, index + 1)
            current_subset.pop()
            dfs(nums, results, current_subset, index + 1)
        
        results = []
        current_subset = []
        index = 0
        dfs(nums, results, current_subset, index)
        return results