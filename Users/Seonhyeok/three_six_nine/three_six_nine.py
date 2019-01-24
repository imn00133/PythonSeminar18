end_num = int(input("마지막 숫자를 입력 하세요 : "))

for cnt in range(1, end_num+1):
    jj_cnt = str(cnt).count('3') + str(cnt).count('6') + str(cnt).count('9')

    if jj_cnt == 0:
        print("%d" % cnt, end='  ')
    else:
        print('짝' * jj_cnt, end='  ')

    if cnt % 20 == 0:
        print("")
print("")
