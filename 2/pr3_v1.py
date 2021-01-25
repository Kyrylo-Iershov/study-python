items = [23, 555, 666, 123, 128, 4242, 990]
while True:
    print(items)
    n = int(input())
    if items[n] % 2 > 0:
        print("Free!")
    else:
        print(" Price is " + str(items[n]))
