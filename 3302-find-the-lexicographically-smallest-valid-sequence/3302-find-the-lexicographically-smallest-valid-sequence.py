class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)
        
        # suffix[i] = smallest index in word1 >= i that can match word2[j..m-1] greedily
        # Actually: suf[i] = the word2 index we can match from word1[i:] going right
        # Let's build: for each position in word1 from the right,
        # suf[i] = if we start matching word2 from the end at word1[i], how far back in word2 can we reach
        
        # suf[i] = smallest word2 suffix index matchable from word1[i:]
        # i.e., suf[i] means word2[suf[i]:] can be matched in word1[i:] greedily from right
        
        suf = [m] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1]
            if j >= 0 and word1[i] == word2[j]:
                suf[i] = j
                j -= 1
        # After this, suf[i] = the word2 index that word1[i:] starts matching from (suffix match)
        
        # Now greedily build the answer from left
        result = []
        j = 0  # current word2 index to match
        used_wildcard = False
        
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                result.append(i)
                j += 1
            elif not used_wildcard:
                # Use wildcard here: change word1[i] to word2[j]
                # But we need word2[j+1:] to be matchable in word1[i+1:]
                if suf[i + 1] <= j + 1:
                    result.append(i)
                    j += 1
                    used_wildcard = True
        
        if j == m:
            return result
        return []