from collections import deque

class HillClimb:
    def __init__(self, file_name:str):
        self.start, self.end, self.map = self.parse_input(file_name)

    def parse_input(self, file_name:str):
        with open(file_name, "r") as f:
            lines = [line.strip() for line in f]
        #print(*lines, sep="\n")

        rows = len(lines)
        cols = len(lines[0])
        #print(rows, cols)
        map = [[None]*cols for _ in range(rows)]
        #print(*map, sep="\n")

        for y in range(rows):
            for x in range(cols):
                match lines[y][x]:
                    case "S":
                        start = y, x
                        map[y][x] = ord('a')
                    case "E":
                        end = y, x
                        map[y][x] = ord('z')
                    case _:
                        map[y][x] = ord(lines[y][x])
        return start, end, map

    def neigbours(self, y, x):
        n, m = len(self.map), len(self.map[0])
        res = []
        if y > 0:
            res.append((y-1, x))
        if y < n - 1:
            res.append((y+1, x))
        if x > 0:
            res.append((y, x-1))
        if x < m - 1:
            res.append((y, x+1))
        return res
        

    def fitness(self, y, x):
        return self.map[y][x]

    def hill_climb(self, start=None) -> int|float:
        if start is None: start = self.start

        queue = deque([(start, 0)])
        visited = set()

        while queue:
            pos, count = queue.popleft()
            if pos in visited:
                continue

            if pos == self.end:
                return count

            visited.add(pos)
            
            for n in self.neigbours(*pos):
                if self.fitness(*n) - self.fitness(*pos) <= 1:
                    queue.append((n, count+1))

        return float("inf")

    def all_starts(self):
        n, m = len(self.map), len(self.map[0])
        res = []
        for y in range(n):
            for x in range(m):
                if self.map[y][x] == ord('a'):
                    res.append((y, x))
        return res
    
    def all_climbs(self):
        res = []
        for start in self.all_starts():
            res.append(self.hill_climb(start))
        return min(res)

if __name__ == "__main__":
    map = HillClimb("test_input.txt")
    map = HillClimb("input.txt")
    part1 = map.hill_climb()

    print(f"{part1=}")
    part2 = map.all_climbs()
    print(f"{part2=}")
