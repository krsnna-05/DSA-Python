from typing import List


class BruteForce:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        mergedNums = nums1 + nums2
        mergedNums.sort()

        isEven = True if len(mergedNums) % 2 == 0 else False

        if isEven:
            center2 = int(len(mergedNums) / 2)
            center1 = int(center2 - 1)
            return (mergedNums[center1] + mergedNums[center2]) / 2
        else:
            return mergedNums[int(len(mergedNums) / 2)]


sol = BruteForce()

nums1 = [1, 2]
nums2 = [3, 4]

print(sol.findMedianSortedArrays(nums1, nums2))

# nums = [1,2,3,4]
