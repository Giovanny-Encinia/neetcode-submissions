from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        repeated = Counter(nums)

        rep = [(key, values) for key, values in repeated.items()]

        result = sorted(rep, key=lambda x: -x[1])
        return [k for k, v in result][:k]
        # 1, 2, 3, 4       