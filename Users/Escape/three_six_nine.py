JJAK_LIST = (3, 6, 9)
JJAK_STRING = '짝'
LINE_COUNT = 20
cnt = int(input('마지막 숫자를 입력하세요: '))

for i in range(1, cnt + 1):
    # 전 단계의 짝 횟수만큼 출력
    if i > 1:
        print((i - 1, JJAK_STRING * jjak)[jjak > 0],
              end=(' ', '\n')[(i - 1) % LINE_COUNT == 0])
    # 사실상 루프는 여기서 시작
    jjak = 0
    # 끝 자리수 하나씩 체크(끝 자리수 = i % 10)
    while True:
        if i % 10 in JJAK_LIST:
            jjak += 1
        i = i // 10
        if i == 0:
            break
print((cnt, JJAK_STRING * jjak)[jjak > 0])
