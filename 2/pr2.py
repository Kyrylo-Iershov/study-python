items = []
while True:
    print(items)
    n = int(input())
    items.append(n)
    if n == 0:
        print(" game over ")
        break
    if sum(items) == 21:
        print("Bingo !")
        break
    if sum(items) > 21:
        print(" again ")
        break
print(" Finished ")
