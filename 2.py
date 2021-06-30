while True:
    try:
        x, y, w, h = map(int, input().split())
        if (-1 <= w <= 1000 and -1 <= h <= 1000) == False:
            raise ValueError
        elif (-1 <= x <= w-1 and -1 <= y <= h-1) == False:
            raise ValueError
        else:
            print(min(abs(x), abs(y), abs(w-x), abs(h-y)))
            break
    except ValueError:
       print('Value Error. re enter : ')



