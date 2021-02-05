password = input(" Input yuor password : ")
confirm = input(" Confirm your password : ")
text1 = list(password)
text2 = list(confirm)
def correct_password():
    if text1 == text2:
        print("Correct ! ")
    elif text1 != text2:
        print(" Incorrect, try again !")
correct_password()