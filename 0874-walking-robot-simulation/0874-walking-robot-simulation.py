class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0 
        x = y = 0
        best = 0

        for cmd in commands:
            if cmd == -2:
                d = (d - 1) % 4
            elif cmd == -1:
                d = (d + 1) % 4
            else:
                dx, dy = directions[d]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) not in obstacle_set:
                        x, y = nx, ny
                        best = max(best, x*x + y*y)

        return best