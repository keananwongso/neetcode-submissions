class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # if val is too high, move r -= 1
        # is val too low, move l += 1

        l = 0
        r = len(numbers) - 1


        while l < r:
            value = numbers[l] + numbers[r]

            if value < target:
                l += 1
            elif value > target:
                r -= 1
            else:
                return [l + 1, r + 1]

    # T: O(n)
    # S: O(1)
            
