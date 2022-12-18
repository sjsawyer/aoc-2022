def manhattan(p1, p2):
    p1x, p1y, p2x, p2y = (*p1, *p2)
    return abs(p1x - p2x) + abs(p1y - p2y)


def part1(sensors, y=10):

    # calculate distance each sensor covers
    distances = {}
    for sensor, beacon in sensors.items():
        distances[sensor] = manhattan(sensor, beacon)

    y_row_coords = set()
    for sensor, dy in distances.items():
        sx, sy = sensor
        if y in range(sy - dy, sy + dy + 1):
            # number of squares covered in y row
            # e.g. y = sy + dy => n = 1
            #      y = sy      => n = 2dy + 1
            #n = (dy - abs(y - sy))*2 + 1

            # get coords in y row
            n = dy - abs(y - sy)
            for x in range(sx - n, sx + n + 1):
                y_row_coords.add((x, y))

    coverage = len(y_row_coords)
    # subtract the beacons which already occur at these positions
    beacons_in_y_row = set(b for b in sensors.values()
                           if b in y_row_coords)
    return coverage - len(beacons_in_y_row)


def part2(sensors):

    # calculate distance each sensor covers
    distances = {}
    for sensor, beacon in sensors.items():
        distances[sensor] = manhattan(sensor, beacon)

    # The sensors together make a huge coverage area -- a bunch of diamonds
    # which overlap everywhere, except at one point. This location makes an
    # X-ish intersection. We can find the point in the middle by looking for
    # diamonds which _almost_ overlap but not quite. This will involve 2
    # parallel lines a distance of 2 apart, and 2 more parallel lines,
    # perpendicular to those lines, a distance of 2 apart. In fact, the slopes
    # of these lines will be +1 and -1

    pos_lines = []
    neg_lines = []

    for (sx, sy), d in distances.items():
        # 4 lines per point, 2 with + slope, 2 with - slope
        # let b be the y intercept
        # + slope: b = y1 - x1
        # we will store lines as y intercept (with m inferred)

        # +ve slope: b = y1 - x1
        pos_lines.append(sy + d - sx)
        pos_lines.append(sy - (sx + d))

        # -ve slope: b = y1 + x1
        neg_lines.append(sy + d + sx)
        neg_lines.append(sy - d + sx)

    # find a pair of +ve lines 2 apart, easy to do since we have y intercept
    pos_lines.sort(reverse=True)
    neg_lines.sort(reverse=True)

    # validate assumption (not true for the test data, apparently)
    assert sum(abs(x - y) == 2 for x, y in zip(pos_lines, pos_lines[1:])) == 1
    assert sum(abs(x - y) == 2 for x, y in zip(neg_lines, neg_lines[1:])) == 1

    # find where the top 2 lines intersect. Our point will be one below this 
    b1 = next(ba for (ba, bb) in zip(pos_lines, pos_lines[1:])
              if ba - bb == 2)
    b2 = next(ba for (ba, bb) in zip(neg_lines, neg_lines[1:])
              if ba - bb == 2)

    x, y = (b2 - b1) // 2, (b1 + b2) // 2
    # one below
    y -= 1

    return 4000000*x + y


def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    import re
    digit = r'(-?\d+)'
    reg = re.compile(
        f'Sensor at x={digit}, y={digit}: closest beacon is at x={digit}'
        f', y={digit}'
    )
    sensors = {}
    for line in data:
        sx, sy, bx, by = tuple(map(int, reg.match(line).groups()))
        sensors[(sx, sy)] = (bx, by)

    p1 = part1(sensors, y=2000000)
    print('Part 1:', p1)

    p2 = part2(sensors)
    print('Part 2:', p2)


main()
