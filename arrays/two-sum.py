from typing import List

class Optimal:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,num in enumerate(nums):
          
          if num in seen:
            return [i,seen[num]]
          
          req = target - num
          seen[req] = i
          
            
        return seen
      

         
sol = Optimal()

nums = [2,7,11,15]

target = 9

print(sol.twoSum(nums,target))