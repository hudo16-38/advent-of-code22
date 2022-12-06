from dataclasses import dataclass

@dataclass
class Buffer:
    buffer: str

    def get_splits(self) -> list[str]:
        res = []

        part = self.buffer[:4]
        index = 4

        while index < len(self.buffer):
            res.append(part)
            part = part[1:] + self.buffer[index]
            index += 1

        return res
    def get_message_splits(self) -> list[str]:
        res = []

        part = self.buffer[:14]
        index = 14

        while index < len(self.buffer):
            res.append(part)
            part = part[1:] + self.buffer[index]
            index += 1

        return res

    def is_marker(self, split: str) -> bool:
        return len(set(split)) == len(split)

    def is_message(self, split: str) -> bool:
        return len(set(split)) == len(split)

    def find_marker(self) -> int:
        splits = self.get_splits()

        for i, split in enumerate(splits):
            if self.is_marker(split):
                return i+4

    def find_message(self) -> int:
        splits = self.get_message_splits()

        for i, split in enumerate(splits):
            if self.is_marker(split):
                return i+14

    
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
        #print(buffer.find_marker())
        print(buffer.find_message())