with open('day16Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


class Light:
    def __init__(self, x, y, dir):

        self.x = x
        self.y = y
        self.dir = dir


def bounce_light(first_light):
    spots = set()
    seen = []
    lights = [first_light]
    while len(lights) > 0:
        new_lights = []
        for light in lights:
            #move
            if light.dir == 'R':
                light.x += 1
            elif light.dir == 'L':
                light.x -= 1
            elif light.dir == 'D':
                light.y += 1
            elif light.dir == 'U':
                light.y -= 1
            else:
                raise Exception('unknown dir')

            if 0 <= light.x < len(content[0]) and 0 <= light.y < len(content):
                if (light.x, light.y) not in spots:
                    spots.add((light.x, light.y))
                # light in the same spot going same direction will always end up the same
                if (light.x, light.y, light.dir) not in seen:
                    seen.append((light.x, light.y, light.dir))
                    at_pos = content[light.y][light.x]
                    new_lights.append(light)
                    if at_pos != '.':
                        if at_pos == '-' and (light.dir == 'U' or light.dir == 'D'):
                            light.dir = 'R'
                            new_lights.append(Light(light.x, light.y, 'L'))
                        elif at_pos == '|' and (light.dir == 'R' or light.dir == 'L'):
                            light.dir = 'U'
                            new_lights.append(Light(light.x, light.y, 'D'))
                        if at_pos == '/':
                            if light.dir == 'R':
                                light.dir = 'U'
                            elif light.dir == 'L':
                                light.dir = 'D'
                            elif light.dir == 'D':
                                light.dir = 'L'
                            elif light.dir == 'U':
                                light.dir = 'R'
                        if at_pos == '\\':
                            if light.dir == 'R':
                                light.dir = 'D'
                            elif light.dir == 'L':
                                light.dir = 'U'
                            elif light.dir == 'D':
                                light.dir = 'R'
                            elif light.dir == 'U':
                                light.dir = 'L'

        lights = new_lights

    return len(spots)


print('part 1: ' + str(bounce_light(Light(-1, 0, 'R'))))


part2Tests = []
for y in range(len(content)):
    part2Tests.append(Light(-1, y, 'R'))
    part2Tests.append(Light(len(content[0]), y, 'L'))

for x in range(len(content[0])):
    part2Tests.append(Light(x, -1, 'D'))
    part2Tests.append(Light(x, len(content), 'U'))


max = 0
print('testing ' + str(len(part2Tests)) + ' combinations')
for idx, test in enumerate(part2Tests):
    if idx % 19 == 0:
        print('running test ' + str(idx + 1))
    res = bounce_light(test)
    if res > max:
        print('new high of ' + str(res))
        max = res

print('part 2 max is: ' + str(max))
