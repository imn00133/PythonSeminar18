def gugucon(index):
    for dan in range(1, 10):
        print("%d * %d = %2d" % (index, dan, index * dan), end="  ")
    print("")


for gugu in range(1, 10):
    gugucon(gugu)
