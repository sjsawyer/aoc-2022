from collections import deque
import copy


def is_neighbour(source, dest):
    return ord(dest) - ord(source) < 2


def get_nbrs(row, col, grid):
    nbrs = set()
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        i, j = row + dy, col + dx
        if ((i == row and j == col)
             or i < 0 or j < 0
             or i == len(grid) or j == len(grid[0])):
            continue
        if is_neighbour(grid[row][col], grid[i][j]):
            nbrs.add((i, j))

    return nbrs


def part1(grid):

    nbrs = {}
    start = (0, 0)
    end = (0, 0)

    # map S to ` and E to {
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'S':
                grid[row][col] = '`'
                start = (row, col)
            if grid[row][col] == 'E':
                grid[row][col] = '{'
                end = (row, col)
            nbrs[(row, col)] = get_nbrs(row, col, grid)

    # breadth first search, all edges equal weight, so we can prevent exploring
    # neighbours we've already seen (and not visited)
    # nodes in the queue will automatically pop off with the shortest path seen
    # so far to that node
    seen = {start}
    to_visit = deque(((start, 0), ))

    while to_visit:
        node, length = to_visit.popleft()
        seen.add(node)

        if node == end:
            return length

        row, col = node
        for nbr in get_nbrs(row, col, grid):
            if nbr in seen:
                continue
            to_visit.append((nbr, length + 1))
            seen.add(nbr)


def part2(grid):

    nbrs = {}
    start = (0, 0)
    end = (0, 0)

    # store all of the 'a's
    starts = []

    # map S to ` and E to {
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'S':
                grid[row][col] = '`'
            if grid[row][col] == 'E':
                grid[row][col] = '{'
                end = (row, col)
            if grid[row][col] == 'a':
                starts.append((row, col))
            nbrs[(row, col)] = get_nbrs(row, col, grid)


    # keep track of optimal path for each 'a'
    distances = {node: None for node in starts}

    for start in starts:
        if distances[start] is not None:
            # we already found the shortest path from this node 'a'
            continue
        if distances[start] == -1:
            # we already determined no path from here
            continue

        # solve from here
        seen = {start}
        to_visit = deque(((start, 0), ))
        parent = {}

        while to_visit:
            node, length = to_visit.popleft()
            seen.add(node)

            if node == end:
                break

            row, col = node
            for nbr in get_nbrs(row, col, grid):
                if nbr in seen:
                    continue

                parent[nbr] = node
                to_visit.append((nbr, length + 1))
                seen.add(nbr)

        if node != end:
            # no path found
            for node in seen:
                row, col = node
                if grid[row][col] == 'a':
                    distances[node] == -1
            continue

        # reconstruct path
        path = []
        current = node
        while current is not None:
            path.append(current)
            current = parent.get(current)

        # not only have we found the optimal path from this 'a' but each 'a'
        # which is also along our path
        for i, node in enumerate(path):
            row, col = node
            if grid[row][col] == 'a':
                distances[node] = i

    return min(v for v in distances.values() if v is not None and v != -1)


def main():
    with open('input.txt') as f:
        data = f.read().splitlines()
        data = [list(row) for row in data]

    p1 = part1(copy.deepcopy(data))
    print('Part 1:', p1)

    p2 = part2(copy.deepcopy(data))
    print('Part 2:', p2)


main()
