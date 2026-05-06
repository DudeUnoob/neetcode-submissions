class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums = nums1 + nums2

        nums.sort()
        total_length = len(nums1) + len(nums2)

        if total_length % 2 == 0:
            l = 0
            r = len(nums) - 1

            mid = (l + r) // 2

            return (nums[mid] + nums[mid + 1]) / 2

        else:
            l = 0
            r = len(nums) - 1

            mid = (l + r) // 2

            return nums[mid]

