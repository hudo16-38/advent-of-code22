from dataclasses import dataclass

@dataclass
class Elf:
    rooms: set[int]

@dataclass
class Pair:
    elf1: Elf
    elf2: Elf

    def fully_contains(self) -> bool:
        s1 = self.elf1.rooms
        s2 = self.elf2.rooms
        return not (bool(s1-s2) and bool(s2-s1))
    
    def overlap(self) -> set[int]:
        return self.elf1.rooms & self.elf2.rooms

@dataclass
class CleaningPlan:
    paires: list[Pair]

    def compute_subsets(self) -> int:
        return sum(p.fully_contains() for p in self.paires)

    def compute_overlaps(self) -> int:
        return sum(p.overlap() > set() for p in self.paires)

def process_input(file_name:str) -> CleaningPlan:
    res = []
    
    with open(file_name, "r") as file:
        for line in file:
            stripped = line.strip()
            e1, e2 = stripped.split(",")

            beg, end = map(int, e1.split("-"))
            elf1 = Elf(set(range(beg, end+1)))

            beg, end = map(int,e2.split("-"))
            elf2 = Elf(set(range(beg, end+1)))

            pair = Pair(elf1, elf2)
            res.append(pair)
    return CleaningPlan(res)

if __name__ == "__main__":
    plan = process_input("test_input.txt")
    plan = process_input("input.txt")
    print(plan.compute_subsets())
    print(plan.compute_overlaps())
