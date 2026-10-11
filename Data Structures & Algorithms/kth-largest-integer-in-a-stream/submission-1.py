class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k

        heapq.heapify(self.minHeap)        # O(n)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)    # O(lg n)
    
    # T: O(n log n)
    # S: O(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)  # O(log k)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)    # O(log k)
        return self.minHeap[0]      

    # T: O(log k)
    # S: O(k)