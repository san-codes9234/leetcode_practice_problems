class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        
        count = Counter(s)
        
        # Build the first half by sorting characters
        half = []
        middle = ""
        
        for char in sorted(count.keys()):
            freq = count[char]
            half.append(char * (freq // 2))
            if freq % 2 == 1:
                middle = char  # at most one odd character (guaranteed palindrome)
        
        half_str = "".join(half)
        return half_str + middle + half_str[::-1]