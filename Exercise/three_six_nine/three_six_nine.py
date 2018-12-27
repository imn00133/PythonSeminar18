end_num = int(input("마지막 숫자를 입력하세요: "))

for number in range(1, end_num + 1):
    # 숫자를 str로 바꾸면 각 자리를 분리하여 접근할 수 있다.
    times_count = str(number).count('3') \
        + str(number).count('6') \
        + str(number).count('9')
    if times_count == 0:
        print(number, end=" ")
    else:
        for i in range(times_count):
            print("짝", end="")
        print("", end=" ")

    # 20번마다 /n을 넣어준다.
    if number % 20 == 0:
        print()
