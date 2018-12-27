end_num = int(input("마지막 숫자를 입력하세요: "))

for number in range(1, end_num + 1):
    # 1자리씩 끊어서 계산한다.
    # remainder는 나머지이다.
    temp_num = number
    remainder = temp_num % 10
    temp_num //= 10
    clap_str = []

    while True:
        if remainder != 0 and remainder % 3 == 0:
            clap_str.append("짝")
        if remainder != 0 and remainder % 2 == 0:
            clap_str.append("뽁")
        if temp_num == 0:
            break
        remainder = temp_num % 10
        temp_num //= 10

    if clap_str:
        # step을 -1로 하면 역순의 리스트를 반환한다.
        clap_str = clap_str[::-1]
        for clap in clap_str:
            print(clap, end='')
        print(' ', end='')
    else:
        print(number, end=' ')
    if number % 20 == 0:
        print()
