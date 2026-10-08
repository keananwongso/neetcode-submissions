class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = defaultdict(int)
        window = defaultdict(int)

        for c in s1:
            s1_count[c] += 1 
        
        l = 0

        for r in range(len(s2)):
            window[s2[r]] += 1

            if (r - l + 1) > len(s1):
                window[s2[l]] -= 1
                
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
        
            if window == s1_count:
                return True
        return False
    
    # T: O(n) 
    # S: O(1)