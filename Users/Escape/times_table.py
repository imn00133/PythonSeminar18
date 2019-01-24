for y in range(1, 10):
    for x in range(2, 10):
        print('{} Ă {} = {:2d}'.format(x, y, x * y), end='  ')
    print()

# # plan b
# for a in [['{} Ă {} = {:2d}'.format(x, y, x * y) for x in range(2, 10)]
#           for y in range(1, 10)]:
#     print('  '.join(a))
