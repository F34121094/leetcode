class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)

        return [candy + extraCandies  >= max_c for candy in candies]
        