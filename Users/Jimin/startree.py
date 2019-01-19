while True:
    height = int(input("별나무 높이 입력해(1~79) : "))
    if height < 0:
        print("종료")
        break
    elif height > 79 or height < 1:
        print("1~79만 입력해라")
    else:
        i = 1
        while i <= height:
            j = 1
            while j <= height - i:
                print(" ", end="")
                j = j + 1
            k = 1
            while k <= 2*i - 1:
                print("*", end="")
                k = k + 1
            print("")
            i = i + 1
