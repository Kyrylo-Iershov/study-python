n = int(input(" Input a number : "))
chz = list(range(1, n))
for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print(" Solo Learn ")
    elif x % 3 == 0:
        print(" Solo ")
    elif x % 5 == 0:
        print(" Learn ")
    else:
        continue
