"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted([interval.start for interval in intervals]) # [0, 5, 15]
        end_times = sorted([interval.end for interval in intervals])    # [10, 20, 40]

        end_pointer = 0
        rooms_in_use = 0 #2
        max_rooms = 0    #2

        for start_time in start_times:
            if start_time < end_times[end_pointer]:
                rooms_in_use += 1
            else:
                end_pointer += 1
            
            max_rooms = max(max_rooms, rooms_in_use)
        
        return max_rooms

        # T: O(n log n)
        # S: O(n)
