class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        # puts in dict
        for num in nums:
            count[num] += 1
        # put in bucket sort freq
        for num, v in count.items():
            freq[v].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
    
    # T: O(n)
    # S: O(n)