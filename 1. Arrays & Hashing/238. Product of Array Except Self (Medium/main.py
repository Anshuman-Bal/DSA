from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        val = [1] * n

        prefix = 1
        for i in range(n):
            val[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            val[i] *= suffix 
            suffix *= nums[i]

        return val
    
if __name__ == "__main__":

    x = Solution()

print(x.productExceptSelf([1, 2, 3, 4]))