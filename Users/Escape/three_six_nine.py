JJAK_LIST = (3, 6, 9)
JJAK_STRING = '짝'
LINE_COUNT = 20
cnt = int(input('마지막 숫자를 입력하세요: '))

for i in range(1, cnt + 1):
    # 전 단계의 짝 횟수만큼 출력
    # if 문이 들어가는 이유는 첫 단계(i=1)에 이 명령을 실행하지 않기 위함입니다.
    if i > 1:
        print((i - 1, JJAK_STRING * jjak)[jjak > 0],
              end=(' ', '\n')[(i - 1) % LINE_COUNT == 0])
    # 사실상 루프는 여기서 시작

    # 루프 시작이 for 문 중간에 있는 이유는 체크 도중 i값이 변경되기 때문입니다.
    # i //= 10    ← 이 부분입니다.

    # 따라서 루프 마지막에서는 원래의 i값을 알 수 없으므로
    # i값이 한 번 for문을 거쳐서 (원래 값 + 1)이 됐을 때 처리하도록 했습니다.

    jjak = 0

    # 끝 자리수 하나씩 체크(끝 자리수 = i % 10)
    # '짝' 1개를 찾으면

    # 예:
    # i = 167 → i % 10 = 7 (16 '7')    : 3, 6, 9가 아니므로 jjak += 0
    # i //= 10 → i = 16
    # i = 16 → i % 10 = 6 (1 '6' 7)    : 3, 6, 9가 맞으므로 jjak += 1
    # i //= 10 → i = 1
    # i = 1 → i % 10 = 1 ('1' 67)      : 3, 6, 9가 아니므로 jjak += 0
    # i //= 10 → i = 0
    # i > 0 이 아니므로 종료 → 결론: jjak = 1

    while i > 0:
        jjak += i % 10 in JJAK_LIST
        i //= 10
print((cnt, JJAK_STRING * jjak)[jjak > 0])
