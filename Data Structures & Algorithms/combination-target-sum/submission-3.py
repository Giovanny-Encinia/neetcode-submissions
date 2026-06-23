from math import ceil
class Solution:
    def generate_search_space(self, nums, target):
        result = []

        for n in nums:
            result.extend([n] * ceil(target / n))
        
        result.sort()

        return result

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        set(3, 4, 5)
        result = target - 3
        check if it is greater than zero if greater then continue
        if it is zero then stop it and save combination
        what happen if the nums list is empty, 
        how many 3s can be contained in the 16, how many 4 can be contained in 16 ....
        the first approach, for each number how many times the number need to be appear
        tarjet / nums[i] = number times appear
        example
        16 / 3 = 5.3333333
        16/4 = 4
        16 / 5 = 3.5
        maybe ceil
        [3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
        then is a combination problem with repeated numbers, we need to sort
        what happen with duplicates solutions, we need to jump the repeated numbers
        """
        search_space = self.generate_search_space(nums, target)

        def find_combination(nums: list, result: list, target: int, current_comb: int, index: int, total: int):
            if total == target:
                
                result.append(current_comb.copy())
                return
            
            if index >= len(nums) or total > target:
                return
            
            current_comb.append(nums[index])
            find_combination(nums, result, target, current_comb, index + 1, total + nums[index])
            current_comb.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            
            find_combination(nums, result, target, current_comb, index + 1, total)
        
        result = []
        current_comb = []

        find_combination(search_space, result, target, current_comb, 0, 0)

        return result

        