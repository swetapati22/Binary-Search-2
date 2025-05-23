"""
# Time Complexity :
- O(log n), binary search is used

# Space Complexity :
- O(1), no extra space used

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid  # Peak is on the left side including mid
            else:
                left = mid + 1  # Peak is on the right side excluding mid

        return left  # or right, both point to the peak
