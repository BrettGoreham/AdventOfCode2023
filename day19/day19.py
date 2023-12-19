import copy
with open('day19Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


class Thing:
    def __init__(self, x, m, a, s):

        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def total(self):
        return self.x + self.m + self.a + self.s


rulesDict = {}
coolthings = []
thingsStart = False
for line in content:
    if line == "":
        thingsStart = True
    else:
        if thingsStart:
            z = line[1:-1].split(',')
            x = int(z[0].split('=')[1])
            coolthings.append(Thing(int(z[0].split('=')[1]), int(z[1].split('=')[1]), int(z[2].split('=')[1]), int(z[3].split('=')[1])))
        else:
            ruleName = line[:line.index("{")]
            rulelist = line[line.index("{") + 1: line.index("}")].split(',')
            rulesDict[ruleName] = rulelist


finalTotal = 0
for thing in coolthings:
    ruleName = 'in'
    while ruleName != 'A' and ruleName != 'R':
        rules = rulesDict[ruleName]
        for rule in rules:
            if ':' not in rule:
                ruleName = rule
            else:
                r, result = rule.split(':')
                left = r[0]
                leftval = 0
                if left == 'x':
                    leftval = thing.x
                elif left == 'm':
                    leftval = thing.m
                elif left == 'a':
                    leftval = thing.a
                else:
                    leftval = thing.s

                rightval = int(r[2:])

                if r[1] == '<':
                    if leftval < rightval:
                        ruleName = result
                        break
                else:
                    if leftval > rightval:
                        ruleName = result
                        break
    if ruleName == 'A':
        finalTotal += thing.total()

print('part 1: ' + str(finalTotal))

#Find all possible paths that lead to an A
valid = []
tup = ('in', '')
paths = [[tup]]
while len(paths):
    path = paths.pop()
    s = path[len(path) - 1][0]
    for rule in rulesDict[s]:
        x = copy.deepcopy(path)
        val = ()
        if ':' not in rule:
            val = (rule, rule)

        else:
            vals = rule.split(':')
            val = (vals[1], rule)

        x.append(val)
        if val[0] == 'A':
            valid.append(x)
        elif val[0] != 'R':
            paths.append(x)


# go through the paths and reduce space that allows you to get there
total = 0
for path in valid:
    map = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
    curr = 0

    while curr < len(path) - 1:
        for rule in rulesDict[path[curr][0]]:
            val = ''
            if ':' not in rule:
                val = rule
            else:
                r, val = rule.split(':')
                left = r[0]
                sign = r[1]
                value = int(r[2:])
                val = val
                if rule == path[curr + 1][1]:
                    if sign == '<':
                        if map[left][1] > value - 1:
                            map[left][1] = value - 1
                    else:
                        if map[left][0] < value + 1:
                            map[left][0] = value + 1
                else:
                    if sign == '<': # opposite day
                        if map[left][0] < value:
                            map[left][0] = value
                    else :
                        if map[left][1] > value:
                            map[left][1] = value

            if rule == path[curr + 1][1]:
                break
        curr += 1

    tot = 1
    for val in map.values():
        tot *= (val[1] - val[0] + 1)

    total += tot
print('part 2: ' + str(total))
