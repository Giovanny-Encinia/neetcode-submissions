class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def create_combinations(n, k, index, current_comb, results):
            if len(current_comb) == k:
                results.append(current_comb[:])
                return None
            if index > n:
                return None
            
            current_comb.append(index)
            create_combinations(n, k, index + 1, current_comb, results)
            current_comb.pop()
            create_combinations(n, k, index + 1, current_comb, results)
        
        results = []
        current_comb = []
        index = 1
        create_combinations(n, k, index, current_comb, results)
        return results
