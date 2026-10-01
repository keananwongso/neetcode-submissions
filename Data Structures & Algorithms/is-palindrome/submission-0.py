class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1
        
        # the loop
        while l < r:
            #skip if not alphanumeric 
            if s[l].isalnum() is False:
                l += 1
            elif s[r].isalnum() is False:
                r -= 1

            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        
        return True
        

# T: O(n) 
# S: O(1)