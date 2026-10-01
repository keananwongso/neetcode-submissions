class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # {value: index}
        # [3 : 1]

        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i

# T: O(n)
# S: O(n)