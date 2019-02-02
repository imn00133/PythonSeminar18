def combinations(population, r):
    combinations = list()

    n = len(population)
    x = list(range(0, r))

    while True:
        current = list()
        for i in range(0, r):
            current.append(population[x[i]])

        combinations.append(current)

        if x[0] == n - r:
            break

        walker = r - 1
        while x[walker] == n + walker - r:
            walker -= 1

        x[walker] += 1

        if walker != r - 1:
            for i in range(1, r - walker):
                x[walker + i] = x[walker] + i

    return combinations


NUM_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = combinations(NUM_LIST, 9)
for x in a:
    print(x)
