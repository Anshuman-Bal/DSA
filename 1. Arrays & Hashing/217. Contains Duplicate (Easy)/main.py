from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if not nums:
            return "No data"

        elif len(nums) == len(set(nums)):
            return False

        else:
            return True
            
if __name__ == "__main__":
    

    testcase = [1,2,3,1]
    solution_instance = Solution()


    value = solution_instance.containsDuplicate(testcase)

    print(value)