class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(num):
            product = 1
            for d in str(num):
                product *= int(d)
            return product

        while digit_product(n) % t != 0:
            n += 1

        return n