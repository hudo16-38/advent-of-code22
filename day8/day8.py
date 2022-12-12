from numpy import array

def process_input(file_name:str):
    res = []
    
    with open(file_name, "r") as f:
        for line in f:
            lst = list(map(int, list(line.strip())))
            res.append(array(lst))
    return array(res)

def is_visible(y, x, arr):
    n = arr.shape[0]
    if y in (0, n-1): return True
    if x in (0, n-1): return True

    col = arr[:, x]
    row = arr[y, :]

    left_part = row[:x]
    right_part = row[x+1:]
    upper_part = col[:y]
    lower_part = col[y+1:]

    left = all(left_part < row[x])
    right = all(right_part < row[x])
    upper = all(upper_part < col[y])
    lower = all(lower_part < col[y])

    return left or right or upper or lower

def count_visible(arr):
    n, m = arr.shape
    res = 0

    for y in range(n):
        for x in range(m):
            res += is_visible(y, x, arr)
    return res

def count_score(y, x, arr):
    n = arr.shape[0]
    col = arr[:, x]
    row = arr[y, :]

    res1 = res2 = res3 = res4 = 0
    index = x
    while index >= 0 and row[index] < row[x]:
        res1 += 1
        index -= 1
    
    index = x
    while index < n and row[index] < row[x]:
        res2 += 1
        index += 1

    index = y
    while index >= 0 and col[index] < col[y]:
        res3 += 1
        index -= 1
    
    index = y
    while index < n and col[index] < col[y]:
        res4 += 1
        index += 1

    return res1*res2*res3*res4

def find_highest_score(arr):
    n,m = arr.shape

    res = []
    for y in range(n):
        for x in range(m):
            res.append(count_score(y, x, arr))
    return max(res)

def process_input(input):
    result = 0
    for i, row in enumerate(input):
        for j, _ in enumerate(row):
            tmp = heigh_value(i, j, input, len(input))
            result = tmp if tmp > result else result
    return result
def heigh_value(row, column, input, max_size):
    directions = ["r", "l", "u", "d"]
    res = 1
    for i in range(1, max_size):
        tmp_directions = directions.copy()
        for direction in tmp_directions:
            if direction == "r":
                if column + i == max_size:
                    res *= i - 1
                    directions.remove(direction)
                elif input[row][column] <= input[row][column + i]:
                    res *= i
                    directions.remove(direction)
            if direction == "l":
                if column - i < 0:
                    res *= i - 1
                    directions.remove(direction)
                elif input[row][column] <= input[row][column - i]:
                    res *= i
                    directions.remove(direction)
            if direction == "d":
                if row + i == max_size:
                    res *= i - 1
                    directions.remove(direction)
                elif input[row][column] <= input[row + i][column]:
                    res *= i
                    directions.remove(direction)
            if direction == "u":
                if row - i < 0:
                    res *= i - 1
                    directions.remove(direction)
                elif input[row][column] <= input[row - i][column]:
                    res *= i
                    directions.remove(direction)
        if not len(directions):
            break
    # print("[" + str(row) + "," + str(column) + "] -> " + str(res))
    return res

def read_file(file_name):
    res = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            res.append([int(x) for x in line.strip()])
    return res


if __name__ == "__main__":
    arr = process_input("test_input.txt")
    print(arr)
    part1 = count_visible(arr)
    print(f"{part1=}")
    
    input = read_file("input.txt")
    part2 = process_input(input)
    print(f"{part2=}")
    
