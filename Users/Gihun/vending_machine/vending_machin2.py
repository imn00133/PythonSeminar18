def item_print(item_list):

    prt_index = 0
    for index in item_list:
        print("{0}.{1} 가격:{2}원 잔여수량:{3}".format(prt_index+1,
              item_list[prt_index]['품명'],
              item_list[prt_index]['단가'],
              item_list[prt_index]['수량']))
        prt_index = prt_index + 1
    print("{0}.돈 투입".format(prt_index+1))
    prt_index = prt_index + 1
    print("{0}.거스름 돈".format(prt_index+1))
    prt_index = prt_index + 1
    print("{0}.종료".format(prt_index+1))


def select_item(slt_num):
    

item_list = [
    {'품명': '쇠도끼', '수량': 1, '단가': 100},
    {'품명': '은도끼', '수량': 1, '단가': 200},
    {'품명': '금도끼', '수량': 1, '단가': 300},
    {'품명': '미스릴도끼', '수량': 1, '단가': 450}
]

item_print(item_list)
slt_num = input("상품 번호 입력:")
select_item(slt_num)
