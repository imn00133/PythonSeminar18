for second_num in range(1, 10):
    for first_num in range(2, 10):
        print("%d * %d = %2d" % (first_num, second_num,
                                 first_num*second_num), end='  ')
    print("")
