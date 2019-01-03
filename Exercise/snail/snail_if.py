"""
for문을 사용하지 않고, if문을 통해 O(n)으로 만들려 하였다.
마지막이 세 번째 조건이나 네 번째 조건으로 끝날 때, 2이상 차이나면
first와 second가 한 번씩 작동해 앞 뒤로 왔다갔다하는 것을 볼 수 있다.
ppt만드는 시간 관계상, 일단 여기서 접고 나중에 다시 고려해보기로 한다.
"""
while True:
    row = int(input("행을 입력하세요: "))
    if row < 0:
        break
    column = int(input("열을 입력하세요: "))
    if column < 0:
        break

    snail = [[0] * column for i in range(row)]
    start_row, end_row = 0, row - 1
    start_column, end_column = 0, column - 1
    snail_row, snail_column = 0, 0
    for num in range(1, row * column + 1):
        if snail_row == start_row and snail_column < end_column:
            if snail_column == end_column - 1:
                start_row += 1
            snail[snail_row][snail_column] = num
            snail_column += 1
        elif snail_column == end_column and snail_row < end_row:
            if snail_row == end_row - 1:
                end_column -= 1
            snail[snail_row][snail_column] = num
            snail_row += 1
        elif snail_row == end_row and snail_column > start_column:
            if snail_column == start_column + 1:
                end_row -= 1
            snail[snail_row][snail_column] = num
            snail_column -= 1
        else:
            if snail_row == start_row + 1:
                start_column += 1
            snail[snail_row][snail_column] = num
            snail_row -= 1

    for i in range(row):
        for j in range(column):
            print("%3d" % snail[i][j], end=" ")
        print("")
