JJAK_LIST = (3, 6, 9)
JJAK_STRING = '짝'
LINE_COUNT = 20
cnt = int(input('마지막 숫자를 입력하세요: '))


def jjakify(num):
    r = str(num)
    for x in JJAK_LIST:
        r = r.replace(str(x), JJAK_STRING)
    if r.isnumeric():
        return r
    else:
        # 숫자가 아닌 것만 추려내기
        r = [x for x in r if not x.isnumeric()]
        return ''.join(r)


jjaks = [jjakify(x) for x in range(0, cnt + 1)]
for i in range(1, cnt + 1, LINE_COUNT):
    print(' '.join(jjaks[i:i + LINE_COUNT]))
# print((cnt, JJAK_STRING * jjak)[jjak > 0])
