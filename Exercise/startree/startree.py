while True:
    rotation_num = int(input("그리고 싶은 별 트리의 개수를 입력하세요(1~79): "))
    if rotation_num < 0:
        break
    elif rotation_num == 0 or rotation_num >= 80:
        print("1에서 79까지의 범위만 입력할수 있습니다.")
        continue
    row = 1
    while row <= rotation_num:
        print(" " * (rotation_num - row), end="")
        print("*" * ((2 * row) - 1))
        row += 1

print("종료합니다.")
