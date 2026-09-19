class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int,
                     x1: int, y1: int, x2: int, y2: int) -> bool:
        cx = max(x1, min(xCenter, x2))
        cy = max(y1, min(yCenter, y2))

        return (cx - xCenter) ** 2 + (cy - yCenter) ** 2 <= radius ** 2