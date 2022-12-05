from functools import reduce


def priority(letter: str):
    if letter.islower():
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27


def part1(data):

    common_items = []

    for items in data:
        len_ = len(items)
        sack1, sack2 = items[:len_//2], items[len_//2:]
        common_item, = set(sack1).intersection(set(sack2))
        common_items.append(common_item)

    return sum(map(priority, common_items))


def part2(data):

    common_items = []

    for i in range(0, len(data), 3):
        itemss = data[i:i+3]
        common_item, = reduce(lambda x, y: x.intersection(y), map(set, itemss))
        common_items.append(common_item)

    return sum(map(priority, common_items))


def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    p1 = part1(data)
    print('Part 1:', p1)

    p2 = part2(data)
    print('Part 2:', p2)


main()
