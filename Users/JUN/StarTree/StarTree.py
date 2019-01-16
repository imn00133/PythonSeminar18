from time import sleep
while True:
    n = (int)(input("트리의 높이를 입력하세요: "))
    n = (int)(input("삐빅 간절합이 부족합니다.\n좀더 간절함을 추가해 입력해주세요: "))
    i = 10
    while i < 100:
        print("간절함: %d%%" % i)
        n = (int)(input("좀더: "))
        i += 10
    print("간절함: %d%%" % i)
    if n <= 0 or n >= 80:
        print("저런 간절함이 충분했지만 범위를 잘못입력 하셨군요")
        print("1~79까지중 다시 입력 해주세요")
        continue
    else:
        print("당신의 간절함이 통하였습니다.\n트리를 생성합니다.")
        i = 0
        while i < 3:
            print("%d" % (3-i))
            sleep(1)
            i += 1
        for i in range(1, n+1):
            for j in range(i, n):
                print(" ", end='')
            for j in range(0, i*2-1):
                print("*", end='')
            print("")
