from dataclasses import dataclass

@dataclass
class Buffer:
    buffer: str

    def get_splits(self, length: int) -> list[str]:
        res = []

        part = self.buffer[:length]
        index = length

        while index < len(self.buffer):
            res.append(part)
            part = part[1:] + self.buffer[index]
            index += 1

        return res

    def is_correct(self, split: str, length: int) -> bool:
        return len(set(split)) == length

    def find_subsequence(self, length: int=4) -> int:
        splits = self.get_splits(length)

        for i, split in enumerate(splits):
            if self.is_correct(split, length):
                return i+length
    
def process_file(file_name: str) -> list[Buffer]:
    res = []

    with open(file_name, "r") as f:
        for line in f:
            res.append(Buffer(line.strip()))
    return res

if __name__ == "__main__":
    #buffers = process_file("test_input.txt")
    buffers = process_file("input.txt")

    for buffer in buffers:
        print(buffer.find_subsequence())
        print(buffer.find_subsequence(14))