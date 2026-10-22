class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        left, right = 0, len(products) - 1
        result = []

        for index, char in enumerate(searchWord):
            while left <= right:
                current_product = products[left]

                if index >= len(current_product) or current_product[index] != char:
                    left += 1
                else:
                    break
            
            while left <= right:
                current_product = products[right]

                if index >= len(current_product) or current_product[index] != char:
                    right -= 1
                else:
                    break
                
            suggestions = products[left:min(left + 3, right + 1)]
            result.append(suggestions)
        
        return result
        
        # T: O(NL log N + M)
        # S: O(N)