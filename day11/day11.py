from dataclasses import dataclass
from collections import deque
from math import prod

@dataclass
class Monkey:
    items: deque[int]
    fun: any
    true: int
    false: int
    modulo: int = None

def parse_monkey(text:str) -> Monkey:
    lst = text.split("\n")
    items = map(int, lst[1].split(":")[1].split(", "))
    f_info = lst[2].split(" = ")[1].split(" ")
    #print(f"{f_info=}")

    if f_info[-1] == "old":
        if f_info[1] == "+":
            f = lambda x: 2*x
        else:
            f = lambda x: x**2
    else:
        if f_info[1] == "+":
            f = lambda x: x + int(f_info[-1])
        else:
            f = lambda x: x * int(f_info[-1])
    mod = int(lst[3].split()[-1])
    true, false = int(lst[4].split()[-1]), int(lst[5].split()[-1])

    return Monkey(deque(items), f, true, false, mod)

def parse_input(file_name:str):
    with open(file_name,"r") as f:
        info = f.read().split("\n\n")
    res = []

    for text in info:
        monkey = parse_monkey(text)
        res.append(monkey)

    return res

def round_divided(monkeys: list[Monkey], counts, divisor:int=3):
    for index, monkey in enumerate(monkeys):
        while monkey.items:
            item = monkey.items.popleft()
            counts[index] += 1
            val = monkey.fun(item)//divisor
            if val % monkey.modulo == 0:
                monkeys[monkey.true].items.append(val)
            else:
                monkeys[monkey.false].items.append(val)

def perform_rounds(rounds: int, monkeys: list[Monkey], counts, divisor:int=3):
    for _ in range(rounds):
        round(monkeys, counts, divisor)

def perform_round_lcm(monkeys: list[Monkey], counts, lcm: int):
    for index, monkey in enumerate(monkeys):
        while monkey.items:
            item = monkey.items.pop()
            item %= lcm
            counts[index] += 1
            val = monkey.fun(item)
            if val % monkey.modulo == 0:
                monkeys[monkey.true].items.append(val)
            else:
                monkeys[monkey.false].items.append(val)

def perform_rounds_lcm(rounds: int, monkeys: list[Monkey], counts):
    lcm = prod(monkey.modulo for monkey in monkeys)

    for _ in range(rounds):
        perform_round_lcm(monkeys, counts, lcm)

if __name__ == "__main__":
    monkeys = parse_input("test_input.txt")
    monkeys = parse_input("input.txt")
    
    n = len(monkeys)
    counts = {i:0 for i in range(n)}
    perform_rounds_lcm(10000, monkeys, counts)
    vals = list(counts.values())
    vals.sort()
    print(vals[-1]*vals[-2])


