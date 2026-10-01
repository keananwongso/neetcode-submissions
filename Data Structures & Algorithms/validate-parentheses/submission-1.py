class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        
        stack = []

        for c in s:
            if c in close_to_open:
                if stack and close_to_open[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)

        return not stack
            
        

    # T: O(n)
    # S: O(n)