JJAK_LIST = (3, 6, 9)
JJAK_STRING = '짝'
PPOK_LIST = (2, 4, 6, 8)
PPOK_STRING = '뽁'
LINE_COUNT = 20
cnt = int(input('마지막 숫자를 입력하세요: '))

for i in range(1, cnt + 1):
    # 전 단계의 결과물을 출력
    if i > 1:
        print((i - 1, state)[state != ''],
              end=(' ', '\n')[(i - 1) % LINE_COUNT == 0])
    # 사실상 루프는 여기서 시작
    state = ''
    # 끝 자리수 하나씩 체크(끝 자리수 = i % 10)
    # 끝 자리부터 보기 때문에 처리 순서와 출력 순서는 반대가 되고
    # 따라서 3을 우선 출력하려면 2를 우선 처리해야 합니다.
    while True:
        if i % 10 in PPOK_LIST:
            state += PPOK_STRING
        if i % 10 in JJAK_LIST:
            state += JJAK_STRING
        i = i // 10
        if i == 0:
            break
    state = ''.join(reversed(state))
print((cnt, state)[state != ''])
