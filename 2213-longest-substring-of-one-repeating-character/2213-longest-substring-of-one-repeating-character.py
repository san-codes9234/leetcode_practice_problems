class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        s = list(s)
        n = len(s)
        # each node stores: (max_run, left_run, right_run, left_char, right_char, seg_len)
        tree = [None] * (4 * n)

        def merge(L, R):
            if L is None: return R
            if R is None: return L
            l_max, l_ll, l_rl, l_lc, l_rc, l_len = L
            r_max, r_ll, r_rl, r_lc, r_rc, r_len = R

            # left run of merged: extend into right child if entire left is same char
            new_ll = l_ll + r_ll if l_lc == r_lc and l_ll == l_len else l_ll
            # right run of merged: extend into left child if entire right is same char
            new_rl = r_rl + l_rl if l_rc == r_rc and r_rl == r_len else r_rl
            # max run: left max, right max, or spanning the boundary
            new_max = max(l_max, r_max)
            if l_rc == r_lc:
                new_max = max(new_max, l_rl + r_ll)

            return (new_max, new_ll, new_rl, l_lc, r_rc, l_len + r_len)

        def build(node, lo, hi):
            if lo == hi:
                tree[node] = (1, 1, 1, s[lo], s[lo], 1)
                return
            mid = (lo + hi) // 2
            build(2*node, lo, mid)
            build(2*node+1, mid+1, hi)
            tree[node] = merge(tree[2*node], tree[2*node+1])

        def update(node, lo, hi, idx):
            if lo == hi:
                tree[node] = (1, 1, 1, s[idx], s[idx], 1)
                return
            mid = (lo + hi) // 2
            if idx <= mid:
                update(2*node, lo, mid, idx)
            else:
                update(2*node+1, mid+1, hi, idx)
            tree[node] = merge(tree[2*node], tree[2*node+1])

        build(1, 0, n - 1)

        result = []
        for qi, qc in zip(queryIndices, queryCharacters):
            s[qi] = qc
            update(1, 0, n - 1, qi)
            result.append(tree[1][0])  # max_run is always at index 0

        return result