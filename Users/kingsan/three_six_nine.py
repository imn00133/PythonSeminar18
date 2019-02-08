def tsn(number):
    if number % 3 == 0 and number != 0:
        print("짝", end="")


def number(number):
    if number < 10:
        if number % 3 == 0:
            tsn(number)
        else:
            print(number, end="")
    elif number < 100:
        a = number // 10
        b = number % 10
        if b == 0 and a % 3 != 0:
            print(number, end="")
        elif a % 3 == 0 or b % 3 == 0:
            tsn(a)
            tsn(b)
        else:
            print(number, end="")
    elif number < 1000:
        a = number // 100
        b = (number - a * 100) // 10
        c = number - (a * 100 + b * 10)
        if number % 100 == 0 and a % 3 != 0:
            print(number, end="")
        elif ((a % 3 == 0 and a != 0) or
              (b % 3 == 0 and b != 0) or (c % 3 == 0 and c != 0)):
            tsn(a)
            tsn(b)
            tsn(c)
        else:
            print(number, end="")


N = int(input("몇까지 찾아드릴까요? : "))

for i in range(1, N+1):
    number(i)
    print(" ", end="")
    if i % 20 == 0:
        print("")
print("")
