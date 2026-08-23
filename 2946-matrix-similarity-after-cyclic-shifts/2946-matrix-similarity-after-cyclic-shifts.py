class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        n = len(mat[0])
        shift = k % n   # effective shift after k steps

        if shift == 0:
            return True

        for i, row in enumerate(mat):
            if i % 2 == 0:  # even row: cyclic left shift by `shift`
                if row != row[shift:] + row[:shift]:
                    return False
            else:            # odd row: cyclic right shift by `shift`
                if row != row[-shift:] + row[:-shift]:
                    return False

        return True