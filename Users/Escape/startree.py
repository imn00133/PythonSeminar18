LINE_MIN = 1
LINE_MAX = 79

line = 0
while True:
    line = int(input('별 트리의 개수({}~{})를 입력해주세요: '.format(LINE_MIN, LINE_MAX)))
    if line < 0:
        print('종료합니다.')
    elif not LINE_MIN <= line <= LINE_MAX:
        print('%d에서 %d까지의 범위만 입력할 수 있습니다.' % (LINE_MIN, LINE_MAX))
        continue
    break

level = 0
while level < line:
    level += 1
    print(' ' * (line - level) + '*' * (level * 2 - 1))
