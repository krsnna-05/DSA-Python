from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        j = 1

        k = 1

        done = False

        while j <= len(nums) - 1:

            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
                k += 1
                print(k)

            j += 1

        return k


s = Solution()

print(s.removeDuplicates([1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5]))
