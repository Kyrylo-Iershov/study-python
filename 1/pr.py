name = input(" Enter your name : ")
sem_1_score = int(input(" 1 semester score : "))
sem_2_score = int(input(" 2 semester score : "))
if (sem_1_score + sem_2_score)/2 > 90 < 100:
    print(" Your discount 50%, Congratulation ! ")
elif (sem_1_score + sem_2_score)/2 > 80 < 89:
    print(" Your discount 30%, Congratulation ! ")
elif (sem_1_score + sem_2_score)/2 > 70 < 79:
    print(" Your discount 10%, Congratulation ! ")
elif (sem_1_score + sem_2_score)/2 > 60 < 69:
    print(" Your discount 5%, Congratulation ! ")
elif (sem_1_score + sem_2_score)/2 > 50 < 59:
    print(" Your discount 0%. ")
else:
    print(" Disqualification ! ")
