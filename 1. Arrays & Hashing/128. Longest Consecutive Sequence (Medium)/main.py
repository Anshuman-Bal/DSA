from typing import List
def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for x in nums:
            if (x-1) not in numSet:
                length = 0
                while (x + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest