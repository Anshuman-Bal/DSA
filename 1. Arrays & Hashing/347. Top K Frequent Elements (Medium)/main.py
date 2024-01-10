from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for x in nums:
            freq[x] += 1

        max_values = []
        for i in range(k):
            max_val = max(freq.keys(), key=freq.get)
            max_values.append(max_val)
            freq.pop(max_val)

        return max_values

if __name__ == "__main__":

    x = Solution()
    print(x.topKFrequent([1, 1, 1, 2, 2, 3], 2))