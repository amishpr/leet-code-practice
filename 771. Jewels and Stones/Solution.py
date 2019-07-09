class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for jewel in J:
            count = count + S.count(jewel)
        return count