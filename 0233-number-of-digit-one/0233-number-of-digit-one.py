class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        place = 1   # current place value: 1, 10, 100, ...

        while place <= n:
            higher = n // (place * 10)  # digits above current place
            current = (n // place) % 10 # current digit
            lower = n % place           # digits below current place

            if current == 0:
                count += higher * place
            elif current == 1:
                count += higher * place + lower + 1
            else:
                count += (higher + 1) * place

            place *= 10

        return count