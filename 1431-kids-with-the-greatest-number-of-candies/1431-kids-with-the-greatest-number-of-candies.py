class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [True] * len(candies)
        max_c = max(candies)
        for i,element in enumerate(candies):
            if element + extraCandies < max_c:
                result[i] = False
        return result
        