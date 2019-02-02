import random
import copy
import os

# 0 ~ 9까지의 수를 무작위로 섞은 후 지정된 자릿수만큼 자른다.
# 중복되지 않게 하기 위해 쓰는 방식
# 정답은 ['1', '3', ...] 의 리스트 형태로 answer에 저장된다.
# NUM_LIST의 내용을 ['a', 'b', 'c', ...] 로 바꾸면 알파벳 야구가 된다.
# random.shuffle 기능을 쓰기 위해 일부러 리스트로 만들었으므로 문자열로 바꾸면 에러가 난다.

# <예시>
# 초기 상태: NUM_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# shuffle 후: NUM_LIST = ['4', '8', '9', '3', '1', '7', '6', '2', '0', '5']
# 잘라서 정답 생성: answer = ['4', '8', '9'] >> 정답 489


def random_sampling(population, count):
    # copy 하지 않으면 참조 값이 전달 되는 듯함(원본이 변경됨)
    clone = copy.copy(population)
    if count > len(clone):
        raise ValueError
    random.shuffle(clone)
    return clone[:count]


# 로그 출력용 함수
def print_log(log):
    os.system('clear')
    if len(log) > 0:
        print('\n'.join(log))


# 개수를 조절하고 싶으면 NUM_CNT 값을 바꾸면 된다. 최대 10개
NUM_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
NUM_CNT = 4

answer = random_sampling(NUM_LIST, NUM_CNT)
os.system('clear')
play_cnt = 0
log = list()
while(True):
    # 입력받기
    i_answer = input("Answer: ")

    # 데이터 유효성 검사 영역

    # gg를 선언한 경우 답을 알려주고 종료
    if i_answer.lower() == "gg":
        print_log(log)
        print("gg를 선언하였습니다.\n프로그램을 종료합니다.")
        print("(정답: %s)" % ''.join(answer))
        break

    # 띄어쓰기, 쉼표 등 제거하기
    i_answer = i_answer.replace(',', '')
    i_answer = i_answer.replace(' ', '')

    # 하나라도 조건에 맞지 않으면 i_valid 값을 False로 만들고, 그 경우를 걸러낸다.
    i_valid = True

    for x in i_answer:
        # 지정된 값(숫자) 외의 값이 들어간 경우 걸러내기
        i_valid = i_valid and (x in NUM_LIST)
        # 중복 값이 있는 경우 걸러내기
        i_valid = i_valid and (i_answer.count(x) == 1)

    # 개수가 맞지 않는 경우 걸러내기
    i_valid = i_valid and len(i_answer) == NUM_CNT

    if not i_valid:
        os.system('clear')
        print_log(log)
        print("정상적인 값을 써 주세요 ㅠ_ㅠ 중복은 안 된답니다...")
        continue

    # 이상 없으면 시행 횟수 1 증가 후 검사 실행
    play_cnt += 1

    # s = strike, b = ball, o = out
    s = 0
    b = 0
    o = 0

    # 본격적인 검사
    # 입력 값의 a번째 자리에 n이 들어가있는 상태
    # 정답에 n이 있는지 찾고, 그게 a번째 자리인 경우 strike 추가
    # 그렇지 않은 경우 ball 추가
    for a in range(NUM_CNT):
        n = i_answer[a]
        if n in answer:
            if answer.index(n) == a:
                s += 1
            else:
                b += 1
    o = NUM_CNT - (s + b)
    # 결과 표시 후 끝나지 않은 경우 되풀이
    # 문자 포맷팅 이용하여 더 깔끔하게 정리할 것

    # 정답 알아맞힌 경우
    if s == NUM_CNT:
        log.append('''%s → 플레이어가 정답을 맞힘

축하드립니다! %d번만에 정답을 알아맞히셨습니다!''' % (i_answer, play_cnt))
        print_log(log)
        while True:
            i_answer = input('다시 하시겠습니까? ')
            if i_answer.lower() in ('yes', 'y'):
                # 초기화한 후 반복
                play_cnt = 0
                log.clear
            elif i_answer.lower() in ('no', 'n'):
                exit()
            else:
                continue
            break
    else:
        log.append("%s → %ds %db %do" % (i_answer, s, b, o))
        # (테스트용) 답 출력 print(''.join(answer))
    print_log(log)
