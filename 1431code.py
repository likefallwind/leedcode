class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        childNo = len(candies)
        maxCandieNo = max(candies)
        resultCandie = []
        for i, candy in enumerate(candies):
            if candy + extraCandies >= maxCandieNo:
                resultCandie.append(True)
            else:
                resultCandie.append(False)
        return resultCandie