length = int(input(" Input length : "))
width = int(input(" Input width : "))


def area(length, width):
    print(length * width)
    if length == width:
        print("Square")


area(length, width)
