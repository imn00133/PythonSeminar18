min_line = 1
max_line = 79

while True:
    in_line = int(input("그리고 싶은 별 트리의 줄 수를 입력하세요 (%d ~ %d) : "
                        % (min_line, max_line)))
    cnt = 0
    if in_line < 0:
        print("종료합니다.")
        break
    elif not min_line <= in_line <= max_line:
        print("%d 부터 %d 까지의 숫자만 입력 할 수 있습니다." % (min_line, max_line))
    else:
        while cnt < in_line:
            cnt += 1
            print(' ' * (in_line - cnt) + '*' * (2 * cnt - 1))
