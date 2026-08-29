class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        
        
   
   
        sr, sc = source
        tr, tc = target

        # Different colors -> impossible
        if (sr + sc) % 2 != (tr + tc) % 2:
            return -1

        # Same diagonal -> 1 move
        if abs(sr - tr) == abs(sc - tc):
            return 1

        # Same color, but different diagonal -> 2 moves
        return 2
        