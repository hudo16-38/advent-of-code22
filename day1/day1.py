def split_file(file_name:str = "input.txt") -> list[int]:

    output = []

    with open(file_name, "r") as f:
        bucket = []

        for line in f:

            if line == "\n":
                if bucket != []:
                    output.append(bucket)
                    bucket = []
            else:
                bucket.append(int(line.strip()))
        if bucket != []:
            output.append(bucket)
            
    return output


def sum_buckets(buckets:list[list[int]]) -> list[int]:
    return list(map(sum, buckets))


if __name__ == "__main__":

    buckets = split_file()
    sums = sum_buckets(buckets)
    sums.sort(reverse=True)
    print("max = ", sums[0])
    print("top three = ", sum(sums[:3]))

