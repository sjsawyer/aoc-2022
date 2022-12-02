def part1(data):

    outcomes = {
        ('A', 'X'): 3,
        ('B', 'Y'): 3,
        ('C', 'Z'): 3,
        ('C', 'X'): 6,
        ('A', 'Y'): 6,
        ('B', 'Z'): 6,
        ('A', 'Z'): 0,
        ('B', 'X'): 0,
        ('C', 'Y'): 0,
    }

    choice_score = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    score = 0
    for round_ in data:
        score += outcomes[round_] + choice_score[round_[1]]

    return score


def part2(data):

    required_move = {
        ('A', 'X'): 'Z',
        ('B', 'Y'): 'Y',
        ('C', 'Z'): 'X',
        ('C', 'X'): 'Y',
        ('A', 'Y'): 'X',
        ('B', 'Z'): 'Z',
        ('A', 'Z'): 'Y',
        ('B', 'X'): 'X',
        ('C', 'Y'): 'Z',
    }

    choice_score = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    outcome_score = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }

    score = 0
    for round_ in data:
        score += outcome_score[round_[1]] + choice_score[required_move[round_]]

    return score


def main():
    with open('input.txt') as f:
        data = [tuple(line.split()) for line in f.readlines()]

    p1 = part1(data)
    print('Part 1:', p1)

    p2 = part2(data)
    print('Part 2:', p2)


main()
