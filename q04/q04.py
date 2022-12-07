def part1(intervals):
    overlaps = 0
    for interval in intervals:
        a1, a2, b1, b2 = interval
        if (
            (a1 >= b1 and a2 <= b2) or
            (a1 <= b1 and a2 >= b2)
        ):
            overlaps += 1
    return overlaps


def part2(intervals):
    overlaps = 0
    for interval in intervals:
        a1, a2, b1, b2 = interval
        overlaps += bool(
            set(range(a1, a2+1)).intersection(set(range(b1, b2+1))))

    return overlaps


def main():
    with open('input.txt') as f:
        intervals = []
        data = f.read().splitlines()
        for line in data:
            int1, int2 = line.split(',')
            intervals.append(
                tuple(map(int, (*int1.split('-'), *int2.split('-')))))

    p1 = part1(intervals)
    print('Part 1:', p1)

    p2 = part2(intervals)
    print('Part 2:', p2)


main()
