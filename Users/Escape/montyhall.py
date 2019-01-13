from random import randint, shuffle
# 귀찮아서 변수 한 글자로 지었습니다.
# 문의 개수 n, 사회자가 여는 문의 수 k, 자동차 있는 위치 c

n = int(input('총 문의 개수를 입력하세요: '))
k = int(input('사회자가 여는 문의 개수를 입력하세요: '))
repeat = int(input('반복 횟수를 입력하세요: '))

MC_PICK_RANGE = list(range(1, n + 1))
MY_PICK_RANGE = list(range(1, n + 1))

# 이론적 확률 계산
P_WIN = (n - 1) / n / (n - k - 1)
P_LOSE = 1 - P_WIN

# 생존 신고 주기
CYCLE = 10000

# 시뮬레이션
# win = 이긴 횟수
win = 0
cnt = 0
while cnt < repeat:
    cnt += 1
    # 생존 신고
    if cnt % CYCLE == 0:
        print('시뮬레이션 진행 중: %d번째입니다.' % cnt)
    # 자동차 랜덤 배치
    c = randint(1, n)
    
    my_pick = randint(1, n)
    # 사회자가 문을 공개
    MC_PICK_RANGE.shuffle()
    mc_pick = MC_PICK_RANGE[0:k-1]
    # 참여자가 다른 문을 고릅니다.
    my_pick = randint(k + 2, n)
    # 현재 고른 문에 자동차가 있다면 이긴 횟수 1회가 증가합니다.
    win += c == my_pick

p_win = win / cnt
p_lose = 1 - p_win

print('''
총 횟수: %d
바꾸지 않았을 때 이긴 횟수: %d
바꿨을 때 이긴 횟수: %d
바꾸지 않았을 때 이길 이론적 확률: %0.4f
바꾸지 않았을 때 이긴 시뮬레이션 확률: %0.4f
바꿨을 때 이길 이론적 확률: %0.4f
바꿨을 때 이긴 시뮬레이션 확률: %0.4f
''' % (
        cnt, cnt - win, win, P_LOSE, p_lose, P_WIN, p_win
    )
)
