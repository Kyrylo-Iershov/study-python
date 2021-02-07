password = input(" Input your password : ")
confirm = input(" Confirm your password : ")
text1 = list(password)
text2 = list(confirm)


def correct_password():
    while True:
        if text1 == text2:
            print(" Correct ! ")
            break
        elif text1 != text2:
            print(" Try again ! ")
            break



correct_password()
