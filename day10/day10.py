def parse_input(file_name: str) -> list[tuple[str|int]]:
    res = []

    with open(file_name, "r") as f:
        for line in f:
            stripped = line.strip().split()
            if len(stripped) == 1:
                res.append(tuple(stripped))
            else:
                com, val = stripped
                res.append((com, int(val)))
    return res

def execute_commands(commands: list[tuple[str|int]]):
    signal_strengths = []
    counter = 1
    value = 1

    for index, command in enumerate(commands):
        if command[0] == "addx":
            for _ in range(2):
                if counter % 20 == 0:
                    signal_strengths.append(value*counter)
                counter += 1
            value += command[1]
        else:
            if counter % 20 == 0:
                    signal_strengths.append(value*counter)
            counter += 1
    return signal_strengths

def make_indices(cycle_nums: list[int]):
    res = []
    for x in cycle_nums:
        res.append(x//20 - 1)
    return res
def compute_sum(indices: list[int], signals: list[int]) -> int:
    sum = 0
    for i in indices:
        sum += signals[i]
    return sum

def build_array(commands, length):
    arr = [1]*(length+1)
    count = 0
    val = 1 

    for com in commands:
        if com[0] == "noop":
            count += 1
            arr[count] = val
        else:
            for _ in range(2):
                count += 1
                arr[count] = val
            val += int(com[1])
            arr[count] = val
    return arr

def make_matrix(n, m, arr):
    mat = [[None]*m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            count = n*y + x + 1
            if abs(arr[count-1] - x) <= 1:
                mat[y][x] = "##"
            else:
                mat[y][x] = "  "
    return mat



if __name__ == "__main__":
    #commands = parse_input("test_input.txt")
    commands = parse_input("input.txt")
    sig = execute_commands(commands)
    indices = make_indices([20, 60, 100, 140, 180, 220])
    sum = compute_sum(indices, sig)
    print(sum)
    arr = build_array(commands, 240)
    mat = make_matrix(6, 40, arr)
    for row in mat:
        print("".join(row))

