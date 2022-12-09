def part1(data):

    N = len(data)
    visible = [[False for _ in range(N) ] for _ in range(N)]
    # horizontal
    for i in range(N):
        for j, dx in ((0, 1), (N-1, -1)):
            max_ = -float('inf')
            while 0 <= j <= N-1:
                if data[i][j] > max_:
                    visible[i][j] = True
                max_ = max(max_, data[i][j])
                j += dx
    # vertical
    for i in range(N):
        for j, dy in ((0, 1), (N-1, -1)):
            max_ = -float('inf')
            while 0 <= j <= N-1:
                if data[j][i] > max_:
                    visible[j][i] = True
                max_ = max(max_, data[j][i])
                j += dy

    return sum(is_visible for row in visible for is_visible in row)


def part2(data):
    N = len(data)
    max_scenic_score = -1
    for y in range(N):
        for x in range(N):
            height = data[y][x]
            scenic_score = 1
            for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                xx, yy = x + dx, y + dy
                n = 0
                while xx in range(N) and yy in range(N):
                    n += 1
                    if data[yy][xx] < height:
                        xx += dx
                        yy += dy
                    else:
                        break
                scenic_score *= n
            max_scenic_score = max(max_scenic_score, scenic_score)

    return max_scenic_score



def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    data = [list(map(int, row)) for row in data]
    p1 = part1(data)
    print('Part 1:', p1)

    p2 = part2(data)
    print('Part 2:', p2)


main()
