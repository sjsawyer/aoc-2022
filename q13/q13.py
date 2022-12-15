def compare(packet1, packet2):
    if isinstance(packet1, int) and isinstance(packet2, int):
        if packet1 == packet2:
            return None
        return packet1 < packet2
    if isinstance(packet1, int):
        return compare([packet1], packet2)
    if isinstance(packet2, int):
        return compare(packet1, [packet2])

    # both are lists
    for p1, p2 in zip(packet1, packet2):
        res = compare(p1, p2)
        if res is None:
            continue
        else:
            return res

    # we reached the end of one list
    if len(packet1) == len(packet2):
        return None

    return len(packet1) < len(packet2)


def part1(pairs):
    results = [compare(*pair) for pair in pairs]
    return sum(i+1 for i, res in enumerate(results) if res)


def part2(pairs):
    packets = [p for pair in pairs for p in pair]
    packets.append([[2]])
    packets.append([[6]])

    from functools import cmp_to_key

    # match required return val for cmp_to_key
    def compare_int(p1, p2):
        return 1 if compare(p1, p2) else -1

    packets.sort(key=cmp_to_key(compare_int), reverse=True)

    return ((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))


def main():
    with open('input.txt') as f:
        data = f.read().strip().split('\n\n')
        pairs = []
        for s in data:
            pairs.append(list(map(eval, s.splitlines())))

    p1 = part1(pairs)
    print('Part 1:', p1)

    p2 = part2(pairs)
    print('Part 2:', p2)


main()
