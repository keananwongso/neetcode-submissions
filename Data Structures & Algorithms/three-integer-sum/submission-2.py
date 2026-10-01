class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]

        output = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                target = nums[i] + nums[l] + nums[r]
                # we want target == 0

                if target == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif target < 0:
                    l += 1
                else:
                    r -= 1
    
        return output

    # T: O(n^2)
    # S: O(1)

            

