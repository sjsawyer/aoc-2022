def part1(data):
    i = 0
    while True:
        marker = data[i:i+4]
        if len(set(marker)) == 4:
            return i + 4
        else:
            i += 1

def part2(data):
    i = 0
    while True:
        marker = data[i:i+14]
        if len(set(marker)) == 14:
            return i + 14
        else:
            i += 1


def main():
    with open('input.txt') as f:
        data = f.read().strip()

    p1 = part1(data)
    print('Part 1:', p1)

    p2 = part2(data)
    print('Part 2:', p2)


main()
