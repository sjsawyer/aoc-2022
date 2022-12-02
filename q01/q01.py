def part1(data):
    return max(sum(nums) for nums in data)


def part2(data):
    # Top 3, Let's keep it linear
    total = 0
    sums = list(map(sum, data))
    for _ in range(3):
        i, sum_ = max(enumerate(sums), key=lambda t: t[1])
        total += sum_
        sums.pop(i)
    return total


def main():
    with open('input.txt') as f:
        data = [
            [int(i) for i in chunk.splitlines()]
            for chunk in f.read().split('\n\n')
        ]

    p1 = part1(data)
    print('Part 1:', p1)

    p2 = part2(data)
    print('Part 2:', p2)


main()
