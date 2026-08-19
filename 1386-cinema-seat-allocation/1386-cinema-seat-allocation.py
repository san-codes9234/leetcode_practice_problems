class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        from collections import defaultdict
        
        # Group reserved seats by row
        row_map = defaultdict(set)
        for row, seat in reservedSeats:
            row_map[row].add(seat)
        
        # Check blocks for each reserved row
        result = 0
        for row, reserved in row_map.items():
            left  = reserved.isdisjoint({2, 3, 4, 5})
            mid   = reserved.isdisjoint({4, 5, 6, 7})
            right = reserved.isdisjoint({6, 7, 8, 9})
            
            if left and right:
                result += 2
            elif left or mid or right:
                result += 1
            # else: 0
        
        # All unreserved rows contribute 2 groups each
        unreserved_rows = n - len(row_map)
        result += unreserved_rows * 2
        
        return result