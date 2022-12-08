from aocd import data, submit

# data = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k"""


def _parse():
    cwd = ['$ROOT']  # Path represented as a list of directories
    sizes = {'$ROOT': 0}
    for line in data.splitlines():
        if line.startswith('$ cd '):
            if line[5] == '/':
                cwd = ['$ROOT']
            elif line[5:] == '..':
                cwd = cwd[:-1]
            else:
                cwd.append(line[5:])
        elif line.startswith('$ ls'):
            continue
        elif line.startswith('dir '):
            directory_name = '/'.join(cwd) + '/' + line[4:]
            sizes[directory_name] = 0
        else:
            file_size = int(line.split(' ')[0])
            for index in range(len(cwd)):
                path = '/'.join(cwd[:index + 1])
                sizes[path] += file_size
    return sizes


def a():
    sizes = _parse()
    answer = sum(size for size in sizes.values() if size < 100000)
    submit(answer, part="a")


def b():
    sizes = _parse()
    space_needed = 30000000 - (70000000 - sizes['$ROOT'])
    answer = min(size for size in sizes.values() if size > space_needed)
    submit(answer, part="b")


a()
b()
