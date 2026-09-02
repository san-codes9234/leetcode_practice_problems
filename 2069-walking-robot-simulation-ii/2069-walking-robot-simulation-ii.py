class Robot:
    def __init__(self, width: int, height: int):
        self.perimeter = 2 * (width + height - 2)
        self.pos = 0
        self.moved = False

        self.cells = []
        for x in range(width):
            self.cells.append((x, 0, "East"))
        for y in range(1, height):
            self.cells.append((width-1, y, "North"))
        for x in range(width-2, -1, -1):
            self.cells.append((x, height-1, "West"))
        for y in range(height-2, 0, -1):
            self.cells.append((0, y, "South"))

        self.cells[0] = (0, 0, "South")

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> list[int]:
        x, y, _ = self.cells[self.pos]
        return [x, y]

    def getDir(self) -> str:
        if not self.moved:
            return "East"  
        _, _, d = self.cells[self.pos]
        return d