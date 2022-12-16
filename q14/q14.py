def part1(grid):
    start = (500, 0)
    _, max_y = max(grid.keys(), key=lambda x: x[1])

    def drop_sand():
        sand = start
        while True:
            if sand[1] > max_y:
                return False
            if not grid.get((sand[0], sand[1] + 1)):
                sand = (sand[0], sand[1] + 1)
            elif not grid.get((sand[0] - 1, sand[1] + 1)):
                sand = (sand[0] - 1, sand[1] + 1)
            elif not grid.get((sand[0] + 1, sand[1] + 1)):
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                grid[sand] = 'o'
                return True

    sand_dropped = 0
    while drop_sand():
        sand_dropped += 1

    return sand_dropped


def part2(grid):
    start = (500, 0)
    _, max_y = max(grid.keys(), key=lambda x: x[1])
    max_y += 2

    def drop_sand():
        sand = start
        while True:
            if sand[1] == max_y - 1:
                # floor below
                grid[sand] = 'o'
                return sand
            if not grid.get((sand[0], sand[1] + 1)):
                sand = (sand[0], sand[1] + 1)
            elif not grid.get((sand[0] - 1, sand[1] + 1)):
                sand = (sand[0] - 1, sand[1] + 1)
            elif not grid.get((sand[0] + 1, sand[1] + 1)):
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                grid[sand] = 'o'
                return sand

    sand_dropped = 1
    while drop_sand() != start:
        sand_dropped += 1

    return sand_dropped


def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    grid = {}
    for d in data:
        coords = d.split(' -> ')
        for i in range(len(coords)-1):
            c1, c2 = coords[i:i+2]
            x1, y1 = list(map(int, c1.split(',')))
            x2, y2 = list(map(int, c2.split(',')))
            if x1 == x2:
                if y1 > y2:
                    y1, y2 = y2, y1
                for y in range(y1, y2 + 1):
                    grid[(x1, y)] = '#'
            elif y1 == y2:
                if x1 > x2:
                    x1, x2 = x2, x1
                for x in range(x1, x2 + 1):
                    grid[(x, y1)] = '#'

    import copy
    p1 = part1(copy.deepcopy(grid))
    print('Part 1:', p1)

    p2 = part2(copy.deepcopy(grid))
    print('Part 2:', p2)


main()
