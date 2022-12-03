from dataclasses import dataclass

@dataclass
class Compartment:
    items: str


@dataclass
class Rucksack:
    compartment1: Compartment
    compartment2: Compartment

    def priority(self, letter:str) -> int:
        if letter.isupper():
            return ord(letter) - ord('Z') + 52
        return ord(letter) - ord('z') + 26

    def find_intersect(self) -> set[str]:
        return set(self.compartment1.items) & set(self.compartment2.items)

    def compute_sum(self) -> int:

        intersect = self.find_intersect()

        res = 0
        for l in intersect:
            res += self.priority(l)
        return res

    def get_all_items(self) -> str:
        return self.compartment1.items + self.compartment2.items 


@dataclass
class Group:
    elf1: Rucksack
    elf2: Rucksack
    elf3: Rucksack

    def find_common(self) -> set[str]:
        return set(self.elf1.get_all_items()) & set(self.elf2.get_all_items()) \
               & set(self.elf3.get_all_items())

    def priority(self, letter:str) -> int:
        if letter.isupper():
            return ord(letter) - ord('Z') + 52
        return ord(letter) - ord('z') + 26

    def compute_priority(self) -> int:

        common = self.find_common()

        res = 0
        for c in common:
            res += self.priority(c)

        return res

def fill_rucksacks(file_name:str) -> list[Rucksack]:
    lst = []

    with open(file_name, "r") as f:
        for line in f:
            stripped = line.strip()
            n = len(stripped)
            part1, part2 = stripped[:n//2], stripped[n//2:]
            c1, c2 = Compartment(part1), Compartment(part2)
            r = Rucksack(c1, c2)
            lst.append(r)
    return lst

def compute_sum(rucksacks: list[Rucksack]) -> int:
    res = 0
    for r in rucksacks:
        res += r.compute_sum()
    return res

def make_groups(rucksacks: list[Rucksack]) -> list[Group]:
    groups = []
    n = len(rucksacks)

    for i in range(0, n, 3):
        elf1 = rucksacks[i]
        elf2 = rucksacks[i+1]
        elf3 = rucksacks[i+2]
        

        g = Group(elf1, elf2, elf3)
        groups.append(g)

    return groups

def compute_groups(groups: list[Group]) -> int:
    res = 0

    for g in groups:
        res += g.compute_priority()
    return res

    




if __name__ == "__main__":
    FILE_NAME = "input.txt"

    rucksacks = fill_rucksacks(FILE_NAME)
    s = compute_sum(rucksacks)
    print(f"{s=}")
    groups = make_groups(rucksacks)
    s = compute_groups(groups)
    print(f"{s=}")
 
    
        
        
    
