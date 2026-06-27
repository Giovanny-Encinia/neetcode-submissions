class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        current_comb = []
        current_sum = 0

        def search_combination(current_comb, index, current_sum):
            if current_sum == target:
                results.append(current_comb[:])
                return None
            if index >= len(nums) or current_sum > target:
                return None
        
            current_comb.append(nums[index])
            search_combination(current_comb, index, current_sum + nums[index])
            current_comb.pop()
            search_combination(current_comb, index + 1, current_sum)

        search_combination(current_comb, 0, current_sum)
        return results

