class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones] # O(n)
        heapq.heapify(stones) # O(n)

        while len(stones) > 1:
            y = -heapq.heappop(stones) #biggest number
            x = -heapq.heappop(stones) #2nd biggest
            
            if y != x:
                heapq.heappush(stones, -(y - x))
            
        if stones:
            return -stones[0]
        return 0
    
    # T: O(n lgn)
    # S: O(n)