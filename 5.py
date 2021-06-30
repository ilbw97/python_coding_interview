while True:
    try:
        a = int(input(),8)
        if len(str(a)) > 333334:
            raise ValueError
        print(bin(a)[2:])
        break
    except ValueError:
        print("Value is too long! re enter : ")

