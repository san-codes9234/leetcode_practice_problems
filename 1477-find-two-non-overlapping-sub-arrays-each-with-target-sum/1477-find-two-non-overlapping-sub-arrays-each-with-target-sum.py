class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)

        # best[i] = length of shortest valid subarray ending at or before index i
        best = [float('inf')] * n

        left = 0
        curr_sum = 0
        best_so_far = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                best_so_far = min(best_so_far, right - left + 1)

            best[i := right] = best_so_far  # best[right] = shortest so far

        # second pass: for each valid subarray [left..right],
        # pair it with best subarray ending strictly before left
        left = 0
        curr_sum = 0
        result = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1
                if left > 0 and best[left - 1] != float('inf'):
                    result = min(result, length + best[left - 1])

        return result if result != float('inf') else -1