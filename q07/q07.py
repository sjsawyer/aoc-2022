from collections import defaultdict


def part1_and_part2(data):
    dirs = []
    dirsizes = defaultdict(lambda: 0)
    for line in data:
        if line.startswith('$'):
            _, command = line.split(' ', 1)
            if 'cd' in command:
                _, dir_ = command.split(' ', 1)
                if dir_ == '..':
                   dirs.pop()
                else:
                    dirs.append(dir_)
            else:
                assert 'ls' in command
                pass
        elif line.startswith('dir'):
            pass
        else:
            # file
            size, filename = line.split()
            for i in range(len(dirs)):
                dir_path = tuple(dirs[:i+1])
                dirsizes[dir_path] += int(size)

    part1 = sum(v for v in dirsizes.values() if v <= 100000)

    disk_size = 70000000
    space_needed = 30000000
    used_space = dirsizes[('/', )]
    free_space = disk_size - used_space
    looking_for = space_needed - free_space

    _, part2 = min((v - looking_for, v) for v in dirsizes.values()
                   if v - looking_for >= 0)

    return part1, part2


def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    p1, p2 = part1_and_part2(data)
    print('Part 1:', p1)
    print('Part 2:', p2)


main()
