with open('day11Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

explodesVerticalAfter = []
explodesHorizontalAfter = []
for y in range(len(content)-1, -1, -1):
    empty = True
    for letter in content[y]:
        if letter == '#':
            empty = False
    if empty:
        explodesVerticalAfter.append(y)

for x in range(len(content[0])-1, -1, -1):
    empty = True
    for line in content:
        if line[x] == '#':
            empty = False

    if empty:
        explodesHorizontalAfter.append(x)

galaxies = []
for y in range(len(content)):
    for x in range(len(content[0])):
        if content[y][x] == '#':
            galaxies.append((y,x))


def dist_between(_galaxies, explodes_horizontal_after, explodes_vertical_after, explodes_count):
    total_dist = 0
    for indexX in range(len(_galaxies) - 1):
        for indexY in range(indexX+1, len(_galaxies)):
            galaxy_x = _galaxies[indexX]
            galaxy_y = _galaxies[indexY]
            max_x = max(galaxy_y[1], galaxy_x[1])
            min_x = min(galaxy_y[1], galaxy_x[1])
            max_y = max(galaxy_y[0], galaxy_x[0])
            min_y = min(galaxy_y[0], galaxy_x[0])

            dist = abs(galaxy_y[0] - galaxy_x[0]) + abs(galaxy_y[1] - galaxy_x[1])

            explode_count = 0
            explode_count += len([_x for _x in explodes_horizontal_after if min_x <= _x < max_x])
            explode_count += len([_y for _y in explodes_vertical_after if min_y <= _y < max_y])
            total_dist += dist + (explode_count * explodes_count) - explode_count # dist counts exploded rows once already so remove the extra

    return total_dist


print('part 1:' + str(dist_between(galaxies, explodesHorizontalAfter, explodesVerticalAfter, 2)))
print('part 2:' + str(dist_between(galaxies, explodesHorizontalAfter, explodesVerticalAfter, 1000000)))
