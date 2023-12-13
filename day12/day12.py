import functools

with open('day12Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


def count_valid(_string, _filled, _expected_groups):
    g_count = 0
    g = 0
    _groups = []
    for x in range(len(_string)):
        if _string[x] == '#' or x in _filled:
            g += 1
        elif g > 0:
            if _expected_groups[g_count] != g:
                return False
            g = 0
            g_count += 1

    if 0 != g == _expected_groups[g_count]:
        g_count += 1

    if g_count != len(_expected_groups):
        return False
    return True



validsPart1 = []
for line in content:
    chars, groups = line.split(' ')
    groups = [int(x) for x in groups.split(',')]

    chars = chars
    groups = groups

    questions = [i for i, x in enumerate(chars) if x == "?"]
    filled = chars.count('#')
    toFill = sum(groups) - filled

    toFillArray = []
    for x in range(toFill):
        toFillArray.append(x)

    valid = 0
    done = False
    while not done:
        questionsFilled = []
        for x in toFillArray:
            questionsFilled.append(questions[x])

        if count_valid(chars, questionsFilled, groups):
            valid += 1

        done = True
        for x in range(len(toFillArray) - 1, -1, -1):
            if toFillArray[x] != len(questions) - 1 - (len(toFillArray) - 1 - x):
                toFillArray[x] += 1
                done = False
                #resetallafterxback
                plus = 1
                for y in range(1, len(toFillArray) - x):
                    toFillArray[y+x] = toFillArray[x] + y
                break

    validsPart1.append(valid)

print(sum(validsPart1))

part2Tot = 0

@functools.cache
def checkState(c, state):

    if state in statesSolution.values():
        return statesSolution[state]

    if state[0] >= len(newChars):
        groupsFound = state[2]
        if state[3] != 0:
            if state[2] < len(newGroups) and newGroups[state[2]] == state[3]:
                groupsFound += 1

        if groupsFound == len(newGroups):
            statesSolution[state] = 1
        else:
            statesSolution[state] = 0

        return statesSolution[state]
    else:

        charAtIndex = newChars[state[0]]
        statesToAdd = []
        if charAtIndex == '#':
            statesToAdd.append((state[0] + 1, state[1], state[2], state[3] + 1))
        elif charAtIndex == '.':
            if state[3] == 0:
                statesToAdd.append((state[0] + 1, state[1], state[2], 0))
            elif state[2] < len(newGroups) and newGroups[state[2]] == state[3]:
                statesToAdd.append((state[0] + 1, state[1], state[2] + 1, 0))
        else:
            # ? where .
            if state[3] == 0:
                statesToAdd.append((state[0] + 1, state[1], state[2], 0))
            elif state[2] < len(newGroups) and newGroups[state[2]] == state[3]:
                statesToAdd.append((state[0] + 1, state[1], state[2] + 1, 0))

            # ? where #
            if state[1] < toFill and state[3] + 1 <= newGroups[state[2]]:
                statesToAdd.append((state[0] + 1, state[1] + 1, state[2], state[3] + 1))

        ret_val = -1
        if len(statesToAdd) == 0:
            ret_val = 0
        elif len(statesToAdd) == 1:
            ret_val = checkState(c, statesToAdd[0])

        else:
            ret_val = checkState(c, statesToAdd[0]) + checkState(c, statesToAdd[1])

        statesSolution[state] = ret_val
        return ret_val



tot = 0
for idx, line in enumerate(content):

    chars, groups = line.split(' ')
    groups = [int(x) for x in groups.split(',')]

    newChars = chars + '?' + chars + '?' + chars + '?' + chars + '?' + chars
    newGroups = groups + groups + groups + groups + groups


    questions = [i for i, x in enumerate(newChars) if x == "?"]
    filled = newChars.count('#')
    toFill = sum(newGroups) - filled

    statesSolution = {}
    checkState(idx, (0, 0, 0, 0))

    print(statesSolution[(0, 0, 0, 0)])
    tot += statesSolution[(0,0,0,0)]


print(tot)







