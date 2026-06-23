class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not list:
            return []

        def dfs(numbers: list[int], result: list[list[int]], current_list: list[int], index: int):
            """
            result is the output of the algorithm
            current list save the element of the result the combination
            index the index of the element that needs to be  added
            """
            if index >= len(numbers):
                result.append(current_list.copy())
                return None
            
            print(index, len(numbers))
            new_number = numbers[index]
            # add the new number
            current_list.append(new_number)
            dfs(numbers, result, current_list, index + 1)
            # remove the las number added this is binary add
            # and not add the last number
            current_list.pop()
            dfs(numbers, result, current_list, index + 1)
        result = []
        current_list = []
        
        dfs(nums, result, current_list, 0)

        return result
