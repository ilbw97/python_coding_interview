while True:
    try:
        X = int(input())
        n = 1
        if (1 <= X <= 10000000) == False:
            raise ValueError
        while n < X:
            X -= n
            n += 1

        if n % 2 == 0:
            top=X
            bottom = n - X + 1
        else:
            top = n - X + 1
            bottom = X
        print("%d/%d" % (top, bottom))
        break
    except ValueError:
        print('Wrong Value. re enter : ')
