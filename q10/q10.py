def part1_and_part2(data):
    # value _during_ ith cycle, adding a 0th cycle for ease
    vals = [1, 1]
    for op in data:
        cmd = op.split()[0]
        if cmd == 'noop':
            vals.append(vals[-1])
        else:
            assert cmd == 'addx'
            n = int(op.split()[1])
            # 2 cycles to add
            vals.append(vals[-1])
            vals.append(vals[-1] + n)

    cycles = [20, 60, 100, 140, 180, 220]
    part1 = sum(c*vals[c] for c in cycles)

    # part 2, print grid
    grid = []
    for j in range(6):
        row = []
        for i in range(40):
            sprite_middle = vals[40*j + i + 1]
            if sprite_middle - 1 <= i <= sprite_middle + 1:
                row.append('#')
            else:
                row.append('.')
        grid.append(row)

    print('\n'.join(''.join(row) for row in grid))

    return part1


def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    p1 = part1_and_part2(data)
    print('Part 1:', p1)
    print('Part 2:', 'read image')


main()
