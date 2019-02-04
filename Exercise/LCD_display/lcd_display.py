def hori_output(disp_size, shape):
    """
    모양을 받아 각 행을 출력해준다.
    :param disp_size: int 출력할 크기
    :param shape: string '-', ' |', '||', '| ', ' '가 가능하다.
    :return: 행을 리스트로 되돌려준다.
    """
    hori_array = []
    if shape == '-':
        hori_array.append(" ")
        for i in range(disp_size):
            hori_array.append("-")
        hori_array.append(" ")
    elif shape == ' |':
        hori_array.append(" ")
        for i in range(disp_size):
            hori_array.append(" ")
        hori_array.append("|")
    elif shape == '| ':
        hori_array.append("|")
        for i in range(disp_size):
            hori_array.append(" ")
        hori_array.append(" ")
    elif shape == '||':
        hori_array.append("|")
        for i in range(disp_size):
            hori_array.append(" ")
        hori_array.append("|")
    else:
        hori_array.append(" ")
        for i in range(disp_size):
            hori_array.append(" ")
        hori_array.append(" ")
    return hori_array


def change_num(display_size, num):
    """
    문자로 받은 숫자를 각 모양으로 바꿔서 전달해준다.
    :param display_size: int 모양 크기
    :param num: string 숫자 하나씩
    :return: 2차원 배열로 되돌려준다.
    """
    display_array = []
    if num == '0':
        display_array.append(hori_output(display_size, '-'))
        for j in range(display_size):
            display_array.append(hori_output(display_size, '||'))
        display_array.append(hori_output(display_size, ' '))
        for j in range(display_size):
            display_array.append(hori_output(display_size, '||'))
        display_array.append(hori_output(display_size, '-'))
        return display_array

    elif num == '1':
        display_array.append(hori_output(display_size, ' '))
        for j in range(display_size):
            display_array.append(hori_output(display_size, ' |'))
        display_array.append(hori_output(display_size, ' '))
        for j in range(display_size):
            display_array.append(hori_output(display_size, ' |'))
        display_array.append(hori_output(display_size, ' '))
        return display_array

    elif num == '2':
        display_array.append(hori_output(display_size, '-'))
        for j in range(display_size):
            display_array.append(hori_output(display_size, ' |'))
        display_array.append(hori_output(display_size, '-'))
        for j in range(display_size):
            display_array.append(hori_output(display_size, '| '))
        display_array.append(hori_output(display_size, '-'))
        return display_array

    elif num == '3':
        display_array.append(hori_output(display_size, '-'))
        for j in range(display_size):
            display_array.append(hori_output(display_size, ' |'))
        display_array.append(hori_output(display_size, '-'))
        for j in range(display_size):
            display_array.append(hori_output(display_size, ' |'))
        display_array.append(hori_output(display_size, '-'))
        return display_array

    elif num == '4':
        display_array.append(hori_output(display_size, ' '))
        for j in range(display_size):
            display_array.append(hori_output(display_size, '||'))
        display_array.append(hori_output(display_size, '-'))
        for j in range(display_size):
            display_array.append(hori_output(display_size, ' |'))
        display_array.append(hori_output(display_size, ' '))
        return display_array

    elif num == '5':
        display_array.append(hori_output(display_size, '-'))
        for j in range(display_size):
            display_array.append(hori_output(display_size, '| '))
        display_array.append(hori_output(display_size, '-'))
        for j in range(display_size):
            display_array.append(hori_output(display_size, ' |'))
        display_array.append(hori_output(display_size, '-'))
        return display_array

    elif num == '6':
        display_array.append(hori_output(display_size, '-'))
        for j in range(display_size):
            display_array.append(hori_output(display_size, '| '))
        display_array.append(hori_output(display_size, '-'))
        for j in range(display_size):
            display_array.append(hori_output(display_size, '||'))
        display_array.append(hori_output(display_size, '-'))
        return display_array

    elif num == '7':
        display_array.append(hori_output(display_size, '-'))
        for j in range(display_size):
            display_array.append(hori_output(display_size, ' |'))
        display_array.append(hori_output(display_size, ' '))
        for j in range(display_size):
            display_array.append(hori_output(display_size, ' |'))
        display_array.append(hori_output(display_size, ' '))
        return display_array

    elif num == '8':
        display_array.append(hori_output(display_size, '-'))
        for j in range(display_size):
            display_array.append(hori_output(display_size, '||'))
        display_array.append(hori_output(display_size, '-'))
        for j in range(display_size):
            display_array.append(hori_output(display_size, '||'))
        display_array.append(hori_output(display_size, '-'))
        return display_array

    else:
        display_array.append(hori_output(display_size, '-'))
        for j in range(display_size):
            display_array.append(hori_output(display_size, '||'))
        display_array.append(hori_output(display_size, '-'))
        for j in range(display_size):
            display_array.append(hori_output(display_size, ' |'))
        display_array.append(hori_output(display_size, '-'))
        return display_array


while True:
    # 입력받자마자 바로 리스트로 바꿔준다.
    user_input = input("출력 값을 입력해주세요: ").split()
    user_input[0] = int(user_input[0])
    if user_input[0] == 0:
        break
    row_size = 2*(user_input[0]+1)+1
    display_value = [[] for i in range(row_size)]

    # 받는 숫자를 한 자리씩 떼서 넘긴다.
    for number in range(len(user_input[1])):
        temp_display = change_num(user_input[0], user_input[1][number])
        # 각 행별로 붙여주고, 한 칸씩 띄어준다.
        for i in range(row_size):
            display_value[i].extend(temp_display[i])
            display_value[i].extend([" "])

    # 이중반복으로 출력
    for i in range(len(display_value)):
        for j in range(len(display_value[0])):
            print(display_value[i][j], end="")
        print("")
