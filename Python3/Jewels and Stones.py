class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
            n=0
            for a in J:
                n+=S.count(a)
            return n
