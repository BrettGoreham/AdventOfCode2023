with open('day9Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

part1Sum, part2Sum = 0, 0

for line in content:
    arrays = [[int(x) for x in line.split(' ')]]

    done = False
    while not done:
        array = []
        done = True
        for x in range(0, len(arrays[-1]) - 1):
            val = arrays[-1][x + 1] - arrays[-1][x]
            if val != 0:
                done = False
            array.append(val)

        arrays.append(array)

    arrays[len(arrays) - 1].append(0)
    for x in range(len(arrays) - 2, -1, -1):
        arrays[x].append(arrays[x][len(arrays[x]) - 1] + arrays[x+1][len(arrays[x+1]) - 1])
        arrays[x].insert(0, arrays[x][0] - arrays[x + 1][0])


    part1Sum += arrays[0][len(arrays[0]) - 1]
    part2Sum += arrays[0][0]


print(part1Sum)
print(part2Sum)
