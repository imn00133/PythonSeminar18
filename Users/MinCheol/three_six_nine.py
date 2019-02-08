criteria = (3, 6, 9)
ent_count = 20

input_num = int(input("어디까지? : "))

for curr_num in range(1, input_num+1):
    three_counter = 0
    exp = 1
    left_num = 1
    while not 0 == left_num:
        if curr_num < 10:
            each_num = curr_num
            for i in criteria:
                if i == each_num:
                    three_counter += 1
            left_num = 0
            break
        each_num = curr_num % (10**exp) - curr_num % (10**exp-1)
        left_num = curr_num // (10**exp)
        #print("left %d" % left_num)
        for i in criteria:
            if i == each_num:
                three_counter += 1
        exp = exp + 1
    #print("threecount %d" % three_counter)
    if three_counter > 0:
        print("짝"*three_counter, end=' ')
    else:
        print("%d" % curr_num, end=' ')
    ent_count -= 1
    if ent_count == 0:
        print("")
        ent_count = 20

