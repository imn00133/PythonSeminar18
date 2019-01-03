while True:
    row = int(input("행을 입력하세요: "))
    if row < 0:
        break
    column = int(input("열을 입력하세요: "))
    if column < 0:
        break

    snail = [[0] * column for i in range(row)]
    # 이 방법 외에도 [[0 for cols in range(column)] for rows in range(row)로 가능하다.
    start_row, end_row = 0, row - 1
    start_column, end_column = 0, column - 1
    num, exit_num = 1, column * row
    while num <= exit_num:
        # 열의 숫자를 증가시키며 숫자를 채워 나간다. 다 차면 다음행을 지시
        for j in range(start_column, end_column + 1):
            snail[start_row][j] = num
            num += 1
        start_row += 1
        if num > exit_num:
            break
        # 행의 숫자를 증가시키며 숫자를 채워 나간다. 다 차면 맨 뒤에서 앞 열로 만든다.
        for i in range(start_row, end_row + 1):
            snail[i][end_column] = num
            num += 1
        end_column -= 1
        if num > exit_num:
            break
        # range(start, end, step): 스타트를 포함, end를 포함안함, step만큼 이동
        for j in range(end_column, start_column - 1, -1):
            snail[end_row][j] = num
            num += 1
        end_row -= 1
        if num > exit_num:
            break
        for i in range(end_row, start_row - 1, -1):
            snail[i][start_column] = num
            num += 1
        start_column += 1
        if num > exit_num:
            break

    for i in range(row):
        for j in range(column):
            print("%3d" % snail[i][j], end=" ")
        print("")
