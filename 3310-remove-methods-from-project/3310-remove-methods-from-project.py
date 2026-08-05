from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        # build adjacency list (directed: caller -> callee)
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)

        # step 1: BFS from k to find all suspicious methods
        suspicious = set()
        queue = deque([k])
        suspicious.add(k)
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)

        # step 2: check if any non-suspicious method invokes a suspicious one
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                # can't remove — return all methods
                return list(range(n))

        # step 3: safe to remove — return everything outside suspicious group
        return [m for m in range(n) if m not in suspicious]