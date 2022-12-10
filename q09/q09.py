def is_touching(hx, hy, tx, ty):
    return abs(hx - tx) < 2 and abs(hy - ty) < 2

d_to_delta = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

def part1(data):
    hx, hy, tx, ty = 0, 0, 0, 0
    seen = set()
    seen.add((tx, ty))
    for d, n in data:
        dx, dy = d_to_delta[d]
        for _ in range(n):
            hx_prev, hy_prev = hx, hy
            hx += dx
            hy += dy
            if is_touching(hx, hy, tx, ty):
                continue
            tx, ty = hx_prev, hy_prev
            seen.add((tx, ty))

    return len(seen)


def visualize(positions):

    xs = [x for position in positions for (x, _) in position]
    ys = [y for position in positions for (_, y) in position]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    # change of coordinates
    new_positions = []
    for position in positions:
        new_position = []
        for (x, y) in position:
            new_x, new_y = x - min_x, y - min_y
            new_position.append([new_x, new_y])
        new_positions.append(new_position)

    nx = max_x - min_x
    ny = max_y - min_y

    import curses
    import time
    console = curses.initscr()

    for position in new_positions:
        grid = [ ['.' for _ in range(nx+1)] for _ in range(ny+1) ]
        for i in range(len(position)):
            x, y = position[i]
            c = 'H' if i == 0 else str(i)
            grid[y][x] = c

        grid_str = '\n'.join(''.join(row) for row in grid)

        console.clear()
        console.addstr(0, 0, grid_str)
        console.refresh()
        time.sleep(0.1)

    curses.endwin()


def part2(data):

    viz = []

    positions = [[0, 0] for _ in range(10)]
    seen = set()
    seen.add(tuple(positions[-1]))
    for d, n in data:
        dx, dy = d_to_delta[d]
        for _ in range(n):
            # head always moves
            positions[0][0] += dx
            positions[0][1] += dy
            for i in range(1, 10):
                if is_touching(*positions[i-1], *positions[i]):
                    # no more pieces moving, early exit
                    break
                ax, ay = positions[i-1]
                bx, by = positions[i]
                # hack to clamp between -1 and 1
                cx = ax - bx
                cy = ay - by
                # hack to clamp between -1 and 1
                cx = cx and cx//abs(cx)
                cy = cy and cy//abs(cy)

                positions[i] = [bx + cx, by + cy]
            seen.add(tuple(positions[-1]))
            import copy
            viz.append(copy.deepcopy(positions))

    #visualize(viz)

    return len(seen)


def main():
    data = []
    with open('input.txt') as f:
        for line in f.read().splitlines():
            d, n = line.split()
            data.append((d, int(n)))

    p1 = part1(data)
    print('Part 1:', p1)

    p2 = part2(data)
    print('Part 2:', p2)


main()
