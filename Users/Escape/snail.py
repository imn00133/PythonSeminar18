# m × n 행렬 만들기
m, n = int(input('행 수 입력: ')), int(input('열 수 입력: '))
# 음수를 입력하면 꺼집니다
if m < 0 or n < 0:
    print('음수를 입력하시면 어떡합니까')
elif m > 30 or n > 30:
    print('행과 열의 수는 각각 30을 넘어갈 수 없습니다.')
else:
    # 빈 행렬 만들기
    # [None for x in range(m)] >> m개의 None으로 이루어진 리스트
    # [[~] for x in range(n)] >> 위의 리스트 n개로 이루어진 리스트
    matrix = [[None for x in range(n)] for x in range(m)]

    # 처리
    # x_direction = 1 인 경우 오른쪽으로 한 칸씩 이동, -1이면 왼쪽으로 한 칸씩 이동, 0이면 정지
    # +x >> +y >> -x >> -y >> ...
    # loop = 반복 횟수, x 위치는 loop ~ (m-loop)를 순환
    x, y = 0, 0
    x_direction, y_direction = 1, 0
    loop = 0
    for cnt in range(1, m * n + 1):
        # 배치되는 수의 범위를 고려하여 자릿수 맞춤
        matrix[y][x] = \
         ('%1d', '%2d', '%3d')[(m * n >= 100) + (m * n >= 10)] % cnt
        # 위아래로 움직이고 있을 때
        if x_direction == 0:
            # 위쪽 끝이나 아래쪽 끝에 부딪혔을 때
            if (y, y_direction) in ((loop, -1), (m - loop - 1, 1)):
                # 아래로 가던 경우 왼쪽, 위로 가던 경우 오른쪽으로 방향 변경
                x_direction, y_direction = -y_direction, 0
        elif y_direction == 0:
            if (x, x_direction) in ((loop, -1), (n - loop - 1, 1)):
                # 왼쪽으로 가고 있었다면 다음 순서는 위쪽이고, 위로는 한 칸 덜 가야 하므로 loop 1 증가
                if x_direction == -1:
                    loop += 1
                # 왼쪽으로 가던 경우 위쪽, 오른쪽으로 가던 경우 아래쪽으로 방향 변경
                x_direction, y_direction = 0, x_direction
        # 지정된 방향으로 이동
        x += x_direction
        y += y_direction

    # 출력 부분
    for line in matrix:
        print(' '.join(line))
