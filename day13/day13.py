from functools import cmp_to_key

def process_input(file_name: str):
    with open(file_name, "r") as f:
        text = f.read().strip().split("\n\n")
        res = []
        for line in text:
            lst1, lst2 = map(eval, line.split())
            res.append([lst1, lst2])
    return res

def compare(part1, part2):
    if isinstance(part1, list) and isinstance(part2, int):
        part2 = [part2]

    if isinstance(part2, list) and isinstance(part1, int):
        part1 = [part1]

    if isinstance(part1, int) and isinstance(part2, int):
        if part1 < part2:
            return 1
        if part1 == part2:
            return 0
        return -1
    
    if isinstance(part1, list) and isinstance(part2, list):
        i, j = 0, 0
        while i < len(part1) and j < len(part2):
            temp = compare(part1[i], part2[j])
            if temp == -1:
                return -1
            if temp == 1:
                return 1
            i += 1
            j += 1

        if i == len(part1):
            if len(part1) == len(part2):
                return 0
            return 1
        return -1

    

def compute_result(data):
    res = 0
    index = 1
    for p1, p2 in data:
        val = compare(p1, p2)
        if val == 1:
            res += index
        index += 1
    return res

def transfrom_data(data):
    res = []
    for group in data:
        res.extend(group)
    res.extend(([[2]], [[6]]))
    return res



    

if __name__ == "__main__":
    #data = process_input("test_input.txt")
    data = process_input("input.txt")
    part1 = compute_result(data)
    print(part1)
    new_data = transfrom_data(data)
    new_data.sort(key=cmp_to_key(compare), reverse=True)


    part2 = 1
    #print(*new_data,sep="\n")
    for index, lst in enumerate(new_data, start=1):
        if lst in ([[2]], [[6]]):
            part2 *= index
    print(part2)