s = input()


def hash_tagGen():
    s1 = s.replace(" ", "")
    s2 = "#" + s1
    return s2


print(hash_tagGen())
