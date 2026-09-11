class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        result = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and j != k and i != k:
                        num = digits[i]*100 + digits[j]*10 + digits[k]
                        if 100 <= num <= 999 and num % 2 == 0:
                            result.add(num)
        return len(result)