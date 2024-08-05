while True:
    print('-----sdda------')
    num = int(input())
    if num < 1:
        print('xaaaaaa')
        break
    else:
        coun = 1
        for c in range(0, 10):
            print(f'{num} X {coun} = {num * coun}')
            coun += 1
