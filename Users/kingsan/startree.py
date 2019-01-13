flag = True

while flag:
    star_count = int(input("그리고 싶은 별 트리의 줄 수를 입력하세요(1~79): "))
    line_count = 1
    space_count = 0
    count = 0

    if star_count < 0:
        print("종료합니다.")
        flag = False
    elif star_count < 80:
        while line_count <= star_count:
            space_count = star_count + 1 - line_count
            while space_count > 0:
                print(" ", end="")
                space_count -= 1
            while count < line_count:
                print("*", end="")
                count += 1
            count = 1
            while count < line_count:
                print("*", end="")
                count += 1
            print("")
            line_count += 1
            count = 0
            space_count = 0

    else:
        print("1에서 79까지의 범위만 입력할 수 있습니다.")
