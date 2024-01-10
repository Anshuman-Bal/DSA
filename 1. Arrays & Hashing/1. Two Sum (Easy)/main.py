from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for idx, x in enumerate(nums):
            
            y = target - x
            
            if y not in seen:
                seen[x] = idx
            
            elif y in seen:
                return [seen[y], idx]
    
if __name__ == "__main__":

    x = Solution()
    print(x.twoSum([0,4,3,0], 0))