class MedianFinder:
    import heapq

    def __init__(self):
        self.small = []  #maxHeap
        self.large = []  #minHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # make sure val in small is always <= large
        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # moving largest val from small->large
        if len(self.small) - len(self.large) > 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # moving smallest val from large->small
        if len(self.large) - len(self.small) > 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]

        elif len(self.large) > len(self.small):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2
        
    # add num
        # T: O(m lg n)
    # find median
        # T: O(m)
    # S: O(n)
        