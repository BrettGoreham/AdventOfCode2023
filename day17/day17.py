with open('day17Input.txt') as f:
    content = f.readlines()
content = [list(x.strip()) for x in content]


class Car:
    def __init__(self, x, y, direc, dircount, cost):

        self.x = x
        self.y = y
        self.direc = direc
        self.dircount = dircount
        self.cost = cost

    def copy(self):
        return Car(self.x, self.y, self.direc, self.dircount, self.cost)


Right = {'R': 'D', 'D': 'L', 'L': 'U', 'U': 'R'}
Left = {'R': 'U', 'D': 'R', 'L': 'D', 'U': 'L'}
start = Car(0, 0, 'R', 0, 0)

find = (len(content[0]) - 1, len(content) - 1)

#place : CostToGetThere
placesBeen = {(0, 0, 'R', 0): 0}

cars = [start]
found = False
finalCost = 0
while not found:
    car = cars.pop(0)

    newCars = []
    if car.dircount < 3:
        newCars.append(car.copy())

    left = car.copy()
    left.dircount = 0
    left.direc = Left[left.direc]
    newCars.append(left)

    right = car.copy()
    right.dircount = 0
    right.direc = Right[right.direc]
    newCars.append(right)


    for candidate in newCars:
        if candidate.direc == 'R':
            candidate.x += 1
        elif candidate.direc == 'L':
            candidate.x -= 1
        elif candidate.direc == 'U':
            candidate.y -= 1
        elif candidate.direc == 'D':
            candidate.y += 1
        else:
            raise Exception('wrong direc')

        candidate.dircount += 1
        # still in box
        if 0 <= candidate.x <= find[0] and 0 <= candidate.y <= find[1]:
            candidate.cost += int(content[candidate.y][candidate.x])
            if find == (candidate.x, candidate.y):
                found = True
                finalCost = candidate.cost
                break
            # maybe add this back if we loop too long
            if candidate.cost < placesBeen.get((candidate.x, candidate.y, candidate.direc, candidate.dircount), 999999999):
                placesBeen[(candidate.x, candidate.y, candidate.direc, candidate.dircount)] = candidate.cost
                cars.append(candidate)

    cars.sort(key=lambda x: x.cost)


print('part 1: '+ str(finalCost))


placesBeen = {(0, 0, 'R', 0): 0, (0, 0, 'D', 0): 0}

cars = [Car(0, 0, 'R', 0, 0), Car(0, 0, 'D', 0, 0)]
finalCost = 99999999999999999999999
while len(cars) > 0:
    car = cars.pop(0)

    newCars = []
    if car.dircount < 10:
        newCars.append(car.copy())

    if car.dircount >= 4:
        left = car.copy()
        left.dircount = 0
        left.direc = Left[left.direc]
        newCars.append(left)

        right = car.copy()
        right.dircount = 0
        right.direc = Right[right.direc]
        newCars.append(right)


    for candidate in newCars:
        if candidate.direc == 'R':
            candidate.x += 1
        elif candidate.direc == 'L':
            candidate.x -= 1
        elif candidate.direc == 'U':
            candidate.y -= 1
        elif candidate.direc == 'D':
            candidate.y += 1
        else:
            raise Exception('wrong direc')

        candidate.dircount += 1
        # still in box
        if 0 <= candidate.x <= find[0] and 0 <= candidate.y <= find[1]:
            candidate.cost += int(content[candidate.y][candidate.x])
            if candidate.cost < finalCost:
                if find == (candidate.x, candidate.y) and candidate.dircount > 3:
                    finalCost = candidate.cost
                # maybe add this back if we loop too long
                elif candidate.cost < placesBeen.get((candidate.x, candidate.y, candidate.direc, candidate.dircount), 999999999):
                    placesBeen[(candidate.x, candidate.y, candidate.direc, candidate.dircount)] = candidate.cost
                    cars.append(candidate)

    cars.sort(key=lambda x: x.cost)


print('part 2: ' + str(finalCost))
