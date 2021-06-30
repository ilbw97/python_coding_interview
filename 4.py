c_list = ['black',
          'brown',
          'red',
          'orange',
          'yellow',
          'green',
          'blue',
          'violet',
          'grey',
          'white']
while True:
    try:
        a = input('')
        b = input('')
        c = input('')
        if a not in c_list:
            raise ValueError
        if b not in c_list:
            raise ValueError
        if c not in c_list:
            raise ValueError
        r = str(c_list.index(a)) + str(c_list.index(b))
        print(int(r) * (10 ** c_list.index(c)))
        break
    except ValueError:
        print("NOT IN LIST. re enter ")



