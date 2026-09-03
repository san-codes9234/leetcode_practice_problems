class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odds  = [x for x in nums1 if x % 2 == 1]
        evens = [x for x in nums1 if x % 2 == 0]

        all_even_ok = len(odds) == 0
        if len(evens) == 0:
            all_odd_ok = True
        elif len(odds) == 0:
            all_odd_ok = False
        else:
            all_odd_ok = min(odds) < min(evens)

        return all_even_ok or all_odd_ok