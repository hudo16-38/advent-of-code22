from dataclasses import dataclass
class Directory:
    def __init__(self, name:str, parent=None):
        self.name, self.parent, self.children = name, parent, {}

    def get_child(self, x:str):
        return self.children[x]
    
    def put_child(self, name, child):
            self.children[name] = child
            child.parent = self
    def __str__(self):
        res = self.name
        for ch in self.children.values():
            res += "\n" + str(ch)
        return res
    def __repr__(self):
        return self.name

@dataclass
class File:
    name: str
    memory: int
    parent: Directory = None

class Tree:
    def __init__(self, file_path: str):
        with open(file_path, "r") as f:
            lines = [line.strip() for line in f]

        commands = self.parse_commands(lines)
        self.root = self.build_tree(commands)
        
    def parse_commands(self, lines: list[str]) -> list[tuple[str]]:
        res = []

        for line in lines:
            res.append(tuple(line.split()))

        return res

    def build_tree(self, commands: list[tuple[str]]) -> Directory:
        node = Directory("\\")
        n = len(commands)
        index = 0

        while index < n:
            command = commands[index]
            beg = command[0]
            if beg == "$":
                c = command[1]
                match c:
                    case "cd":
                        x = command[2]
                        match x:
                            case "/":
                                while node.parent != None:
                                    node = node.parent
                            case  "..":
                                node = node.parent
                            case _:
                                node = node.get_child(x)
                        index += 1
                    case "ls":
                        index += 1
            else:
                part1, part2 = command
                #print("parts", part1, part2)
                match part1:
                    case "dir":
                        child = Directory(part2)
                        node.put_child(part2, child)
                    case _:
                        child = File(part2, int(part1))
                        node.put_child(part2, child)
                index += 1
        
        while node.parent != None:
            node = node.parent
        return node

    def _mem(self, node) -> list[list[str, int]]:
        if isinstance(node, File):
            return [[node.name, node.memory, "file"]]
        res = 0
        out = []
        for ch in node.children.values():
            rec = self._mem(ch)
            n, v, t = rec[-1]
            out.extend(rec)
            res += v
        out.append([node.name, res, "dir"])
        return out

    def get_info(self) -> list[list[str, int]]:
        return self._mem(self.root)

    def get_directories(self):
        return [(name, val) for name, val, type in self.get_info() if type == "dir"]

    def find_sum_with_boundary(self, boundary=100000) -> int:
        dirs = self.get_directories()
        res = sum(val for name, val in dirs if val <= boundary)
        return res
    
    def used_memory(self) -> int:
        dirs = self.get_directories()
        used_memory = max(dirs, key=lambda x: x[1])
        return used_memory[1]

    def find_directory_to_remove(self, update=30000000) -> tuple[str, int]:
        dirs = self.get_directories()
        dirs.sort(key=lambda x:x[1])
        used_memory = self.used_memory()
        free_memory = 70000000 - used_memory
        needed_memory = update - free_memory

        for name, val in dirs:
            if val >= needed_memory:
                return name, val

if __name__ == "__main__":
    tree = Tree("test_input.txt")
    tree = Tree("input.txt")
    part1 = tree.find_sum_with_boundary()
    print(f"{part1=}")
    _, part2 = tree.find_directory_to_remove()
    print(f"{part2=}")


    

