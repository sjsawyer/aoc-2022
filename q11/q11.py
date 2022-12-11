from collections import deque
import copy
import functools
import re


def part1(monkeys):

    for _ in range(20):
        for m in monkeys:
            while m.items:
                m.inspections += 1
                worry_level = m.items.popleft()
                worry_level = m.operation(worry_level)
                worry_level //= 3
                res = m.test(worry_level)
                if res:
                    monkeys[m.true_action].items.append(worry_level)
                else:
                    monkeys[m.false_action].items.append(worry_level)

    i1, i2 = sorted((m.inspections for m in monkeys), reverse=True)[:2]
    return i1 * i2


def part2(monkeys):

    supermodulo = functools.reduce(
        lambda x, y: x*y, (m.divisor for m in monkeys))

    for _ in range(10000):
        for m in monkeys:
            while m.items:
                m.inspections += 1
                worry_level = m.items.popleft()
                worry_level = m.operation(worry_level)
                # the trick
                # worry_level //= 3
                worry_level %= supermodulo
                res = m.test(worry_level)
                if res:
                    monkeys[m.true_action].items.append(worry_level)
                else:
                    monkeys[m.false_action].items.append(worry_level)

    i1, i2 = sorted((m.inspections for m in monkeys), reverse=True)[:2]
    return i1 * i2


class Monkey:
    def __init__(
        self,
        idx,
        items,
        operation,
        true_action,
        false_action,
        divisor
    ):
        self.idx = idx
        self.items = items
        self.operation = operation
        self.true_action = true_action
        self.false_action = false_action

        self.inspections = 0
        self.divisor = divisor

    def test(self, n):
        return  n % self.divisor == 0


def main():
    with open('input.txt') as f:
        data = f.read().strip().split('\n\n')

    monkeys = []
    for m in data:
        res = [l.strip() for l in m.splitlines()]
        idx, items, op, test, ta, fa = res
        idx = int(idx[7])
        items = deque(map(int, re.findall(r"\d+", items)))
        op1, op2 = re.search(r"old (\+|\*) (\d+|old)", op).groups()
        f = None
        if op1 == '+':
            if op2 == 'old':
                f = lambda x: x+x
            else:
                n = int(op2)
                f = lambda x,n=n: x + n
        elif op1 == '*':
            if op2 == 'old':
                f = lambda x: x*x
            else:
                n = int(op2)
                f = lambda x,n=n: x * n
        op = f
        divisor = int(test.split()[3])
        true_action = int(ta.split()[5])
        false_action = int(fa.split()[5])
        monkeys.append(
            Monkey(idx, items, op, true_action, false_action, divisor))

    p1 = part1(copy.deepcopy(monkeys))
    print('Part 1:', p1)

    p2 = part2(copy.deepcopy(monkeys))
    print('Part 2:', p2)


main()
