class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(nums, current_perm, index_ignore, result):

            if len(current_perm) == len(nums):
                result.append(current_perm[:])
                return None
            
            for i in range(len(nums)):
                n = nums[i]
                if n not in current_perm:
                    current_perm.append(n)
                    dfs(nums, current_perm, i, result)
                    current_perm.pop()
            # 0, 3
            """
            0, 3
            current_perm [1]
            1, 3
            current_perm [1, 2]
            2, 3
            current_perm [1, 2, 3]
            return result [[1, 2, 3]]

            current_perm [1, 2]
            """

        current_perm = []
        result = []
        dfs(nums, current_perm, -1, result)
        return result