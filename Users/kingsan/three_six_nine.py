def tsn(number):
    if number < 10:
        if number % 3 == 0:
            print("짝", end="")
        else:
            print(number, end="")
    elif number < 100:
        if (number // 10) % 3 == 0:
            print("짝", end="")
        else:
            print(number, end="")
        tsn(number % 10)
    elif number < 1000:
        if(number // 100) % 3 == 0:
            print("짝", end="")
        tsn(number % 100)


N = int(input("몇까지 찾아드릴까요? : "))

for i in range(1, N+1):
    tsn(i)
    print(" ", end="")
    if i % 20 == 0:
        print("")
