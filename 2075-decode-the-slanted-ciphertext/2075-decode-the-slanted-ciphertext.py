class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText

        cols = len(encodedText) // rows
        result = []

        for c in range(cols):
            for r in range(rows):
                col = c + r
                if col < cols:
                    result.append(encodedText[r * cols + col])

        return "".join(result).rstrip()