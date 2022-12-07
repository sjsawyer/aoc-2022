import copy
import re


def part1(stacks, moves):
    stacks = copy.deepcopy(stacks)
    for n, i, j in moves:
        for _ in range(n):
            stacks[j-1].append(stacks[i-1].pop())

    return ''.join(s[-1] for s in stacks)


def part2(stacks, moves):
    stacks = copy.deepcopy(stacks)
    for n, i, j in moves:
        tmp  = []
        for _ in range(n):
            tmp.append(stacks[i-1].pop())
        for _ in range(n):
            stacks[j-1].append(tmp.pop())

    return ''.join(s[-1] for s in stacks)


def main():
    with open('input.txt') as f:
        stack_data, moves_data = f.read().split('\n\n')
        transposed = list(map(''.join, zip(*stack_data.splitlines())))
        stacks = []
        for col in transposed:
            letters = re.findall('[A-Z]', col)
            if letters:
                stacks.append(letters[::-1])

        moves_ = moves_data.splitlines()
        moves = []
        for move in moves_:
            moves.append(tuple(map(int, re.findall(r'\d+', move))))

    p1 = part1(stacks, moves)
    print('Part 1:', p1)

    p2 = part2(stacks, moves)
    print('Part 2:', p2)


main()
