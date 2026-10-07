class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[mid] < target:
                left = mid + 1
                mid = (left + right) // 2
            elif nums[mid] > target:
                right = mid - 1
                mid = (left + right) // 2
            else:
                return mid

        return -1
        
    # T: O(logn)
    # S: O(1)
