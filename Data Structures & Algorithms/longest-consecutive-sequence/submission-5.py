class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        set_of_nums = set(nums)
        seen = set()
        longest = 0

        for num in set_of_nums:
            if num in seen:
                continue
            
            seen.add(num)
            count = 1

            while num + 1 in set_of_nums:
                count += 1
                num += 1
                seen.add(num)
            
            longest = max(longest, count)
            
        return longest

    # T: O(n)
    # S: O(n)

