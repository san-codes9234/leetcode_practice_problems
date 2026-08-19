class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        # Store reserved seats 2 to 9 as a bitmask
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rows[row] = rows.get(row, 0) | (1 << (seat - 2))

        # Every completely empty row can fit 2 families
        answer = 2 * (n - len(rows))

        # Masks for possible family positions
        left = 0b00001111      # seats 2,3,4,5
        middle = 0b00111100    # seats 4,5,6,7
        right = 0b11110000     # seats 6,7,8,9

        for mask in rows.values():
            if mask & left == 0 and mask & right == 0:
                # Both sides are available
                answer += 2
            elif mask & left == 0 or mask & middle == 0 or mask & right == 0:
                # At least one arrangement is available
                answer += 1

        return answer