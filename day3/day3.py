with open('day3Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

ymax = len(content)
xmax = len(content[0])

y = 0
total = 0
while y < ymax:

    x = 0
    numstring = ""
    isNextToSymbol = False
    while x < xmax:
        curr = content[y][x]
        if not curr.isdigit():
            if numstring != "":
                if isNextToSymbol:
                    total += int(numstring)

                numstring = ""
                isNextToSymbol = False

        else:
            numstring += curr
            for ycheck in range(-1, 2):
                for xcheck in range(-1, 2):
                    if 0 <= ycheck + y < ymax and 0 <= xcheck + x < xmax:
                        check = content[ycheck + y][xcheck + x]
                        if not check.isdigit() and check != '.':
                            isNextToSymbol = True

        x += 1

    if numstring != "":
        if isNextToSymbol:
            total += int(numstring)
        numstring = ""
        isNextToSymbol = False

    y += 1


print('part 1 ' + str(total))

# part 2
y = 0
total = 0
while y < ymax:
    x = 0
    while x < xmax:
        curr = content[y][x]
        if curr == '*':
            adjnums = []
            adjCount = 0
            if y > 0:
                lastNum = False
                nums = []
                for checkx in range (-1, 2):
                    if 0 < checkx + x < xmax:
                        if content[y - 1][checkx + x].isdigit():
                            if not lastNum:
                                adjCount += 1
                                nums.append(checkx)
                            lastNum = True
                        else:
                            lastNum = False

                if len(nums) > 0:
                    if nums[0] == -1:
                        digit = True
                        start = x - 1
                        while digit:
                            if start - 1 < 0:
                                digit = False
                            else:
                                if content[y - 1][start - 1].isdigit():
                                    start -= 1
                                else:
                                    digit = False

                        num = ""
                        digit = True
                        while digit:
                            if start == xmax:
                                digit = False
                            else:
                                val = content[y - 1][start]
                                if val.isdigit():
                                    num += val
                                else:
                                    digit = False
                            start += 1

                        adjnums.append(num)
                    if nums[0] == 0 or nums[0] == 1:
                        num = ""
                        digit = True
                        start = x + nums[0]
                        while digit:
                            if start == xmax:
                                digit = False
                            else:
                                val = content[y - 1][start]
                                if val.isdigit():
                                    num += val
                                else:
                                    digit = False
                            start += 1

                        adjnums.append(num)
                    if len(nums) == 2 and nums[1] == 1:
                        num = ""
                        digit = True
                        start = x + 1
                        while digit:
                            if start == xmax:
                                digit = False
                            else:
                                val = content[y - 1][start]
                                if val.isdigit():
                                    num += val
                                else:
                                    digit = False
                            start += 1

                        adjnums.append(num)

            if x != 0 and content[y][x - 1].isdigit():
                adjCount += 1
                done = False
                num = ""
                minus = 1
                while not done:
                    if x - minus >= 0:

                        val = content[y][x - minus]
                        if val.isdigit():
                            num = val + num
                            minus += 1
                        else:
                            done = True
                    else:
                        done = True
                adjnums.append(num)

            if x != xmax - 1 and content[y][x + 1].isdigit():
                adjCount += 1
                done = False
                num = ""
                add = 1
                while not done:
                    if x+add <= xmax:
                        val = content[y][x + add]
                        if val.isdigit():
                            num = num + val
                            add += 1
                        else:
                            done = True
                    else:
                        done = True
                adjnums.append(num)

            lastNum = False
            if y < ymax - 1:
                lastNum = False
                nums = []
                for checkx in range (-1, 2):
                    if 0 < checkx + x < xmax:
                        if content[y + 1][checkx + x].isdigit():
                            if not lastNum:
                                adjCount += 1
                                nums.append(checkx)
                            lastNum = True
                        else:
                            lastNum = False

                if len(nums) > 0:
                    if nums[0] == -1:
                        digit = True
                        start = x - 1
                        while digit:
                            if start - 1 < 0:
                                digit = False
                            else:
                                if content[y + 1][start - 1].isdigit():
                                    start -= 1
                                else:
                                    digit = False

                        num = ""
                        digit = True
                        while digit:
                            if start == xmax:
                                digit = False
                            else:
                                val = content[y + 1][start]
                                if val.isdigit():
                                    num += val
                                else:
                                    digit = False
                            start += 1

                        adjnums.append(num)
                    if nums[0] == 0 or nums[0] == 1:
                        num = ""
                        digit = True
                        start = x + nums[0]
                        while digit:
                            if start == xmax:
                                digit = False
                            else:
                                val = content[y + 1][start]
                                if val.isdigit():
                                    num += val
                                else:
                                    digit = False
                            start += 1

                        adjnums.append(num)
                    if len(nums) == 2 and nums[1] == 1:
                        num = ""
                        digit = True
                        start = x + 1
                        while digit:
                            if start == xmax:
                                digit = False
                            else:
                                val = content[y + 1][start]
                                if val.isdigit():
                                    num += val
                                else:
                                    digit = False
                            start += 1

                        adjnums.append(num)

            if adjCount == 2:
                print("confirmed gear at " + str(x) + ' ' + str(y))
                print(adjnums)
                ratio = int(adjnums[0]) * int(adjnums[1])
                print(ratio)
                total += ratio

        x += 1
    y += 1

print('part 2 '+ str(total))
