with open('a.dat', 'w') as a:
    a.writelines(['%d\n' % x for x in range(1, 80)])
