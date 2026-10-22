from bisect import bisect_left

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""

        for char in searchWord:
            prefix += char 
            start = bisect_left(products, prefix)
            suggestions = []

            for index in range(start, min(start + 3, len(products))):
                product = products[index]

                if not product.startswith(prefix):
                    break
                suggestions.append(product)
            result.append(suggestions)
                                     
        return result

    # T: O(n * l * lgn + m * l * lgn)
    # S: O(n + m)