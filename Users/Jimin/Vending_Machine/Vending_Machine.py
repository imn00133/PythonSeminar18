"""
04. 문제정의, 변수, 자료형(숫자와 문자열) - 18.12.29
고객이 프로토타입으로 자판기의 외형을 만들기 원한다.

프로그램을 시작하면 다음을 입출력하고 종료한다.
돈을 넣으세요: (사용자로부터 입력받기)
1. 블랙커피(100원)
2. 밀크커피(150원)
3. 고급커피(200원)
4. 거스름돈
넣은 돈: (입력 받은 돈 출력)원

단, 프로그램에 입력받는 값은 정수이다.(에러처리를 하지 않는다.)
본인의 디렉터리 아래에 vending_machine 디렉터리를 만들어 저장한다
아스키코드를 넣어 외형을 꾸며도 좋다.
"""
money = input("돈을 넣으세요: ")

print("1. 오라떼 사과(550원)")
print("2. 오란C 오렌지맛(550원)")
print("3. 갈아만든 배(800원)")
print("4. 박카스F(1000원)")
print("거스름돈")
print("넣은 돈:%s원" %money)
#print("넣은 돈:",money,"원")