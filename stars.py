length = 10
for i in range(0, 2*length):
    if i >= length:
        stars = 2*length -i
    else:
        stars = i+1
    for j in range(0, stars):
        print('*', end='')
    print()
