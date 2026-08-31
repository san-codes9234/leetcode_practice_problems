class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        critical = []
        pos = 1
        prev = head
        curr = head.next

        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                critical.append(pos)
            prev = curr
            curr = curr.next
            pos += 1

        if len(critical) < 2:
            return [-1, -1]

        max_dist = critical[-1] - critical[0]

        min_dist = min(critical[i+1] - critical[i] for i in range(len(critical) - 1))

        return [min_dist, max_dist]