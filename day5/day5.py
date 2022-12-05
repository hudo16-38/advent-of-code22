class Ship:

    def __init__(self, file_name:str): 

        with open(file_name, "r") as f:
            text = f.read()
            stacks, commands = text.split("\n\n")
            stacks = stacks.split("\n")
            commands = commands.split("\n")
            keys = list(map(int,stacks.pop().strip().split()))
            n = len(keys)
            height = len(stacks)
            #print(f"{n=}")

            self.stacks = [[] for _ in range(n)]
            self.commands = self.process_commands(commands)

            for line in stacks:
                crates = line[1::4]
                for i in range(len(crates)):
                    if crates[i] != " ":
                         self.stacks[i].append(crates[i])

            for i in range(n):
                self.stacks[i] = list(reversed(self.stacks[i]))

    def process_commands(self, commands: list[str]) -> list[tuple[int]]:
        res = []

        for line in commands:
            stripped = line.strip().split()
            if len(line) < 1:
                continue

            amount, row1, row2 = map(int, (stripped[1], stripped[3], stripped[5]))
            res.append((amount, row1, row2))
            
        return res

    def perform_commands(self) -> None:
        #print("state:", self.stacks)
        for amount, r1, r2 in self.commands:
            #print(amount, r1, r2)
            for _ in range(amount):
                val = self.stacks[r1-1].pop()
                self.stacks[r2-1].append(val)
            #print(self.stacks)

    def perform_better_commands(self) -> None:
        for amount, r1, r2 in self.commands:
            temp = []
            for _ in range(amount):
                val = self.stacks[r1-1].pop()
                temp.append(val)
            self.stacks[r2-1].extend(reversed(temp))


    def __str__(self) -> str:
        res = ""
        for s in self.stacks:
            if s:
                res += s[-1]
        return res


if __name__ == "__main__":
    #ship = Ship("test_input.txt")
    ship = Ship("input.txt")
    #ship.perform_commands()
    ship.perform_better_commands()
    print(ship)


