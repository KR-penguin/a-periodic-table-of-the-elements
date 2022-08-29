# 원소주기율표 외우기 게임
# made by kopeng
# 플래이 해주셔서 감사합니다!


import time
import random

element = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe"]
right_element = ["수소", "헬륨", "리튬", "베릴륨", "붕소", "탄소", "질소", "산소", "플루오린", "네온", "나트륨", "마그네슘", "알루미늄", "규소", "인", "황", "염소", "아르곤", "칼륨", "칼슘", "스칸듐", "타이타늄", "바나듐", "크로뮴", "망가니즈", "철"]
right_answer = "TEXT"
qusetion = "TEXT"
chance = 0
answer = "0"
gaming = False
level = 0
score = 0
temp = 0

def ready_game():
    global level
    global chance
    global answer
    
    print("\n\n\n원소주기율표 게임에 오신 것을 환영합니다")
    input("")
    answer = input("난이도는 몇으로 하시겠습니까? ( 1 ~ 4 )  :  ")

    level = int(answer) 

    if level == 1:
        chance = 15
    if level == 2:
        chance = 10
    if level == 3:
        chance = 5
    if level == 4:
        chance = 1



def game():
    global element
    global right_answer
    global answer
    global gaming
    global level
    global chance
    global score
    global temp
    global qusetion

    while chance > 0:
        
        if score == 600:


            print("\n\nGame Clear! 축하합니다!")
            print("누적 점수 : ", score)
            input("")

        else:
            start = time.time()

            temp = random.randint(1, 26)
            qusetion = element[temp]
            right_answer = right_element[temp]
            print("\n")
            print(qusetion)
            answer = input("")

            if answer == right_answer:
                print("\n정답입니다!\n")
                score = score + 30
                chance = chance - 0
                print("현재 점수 : ", score)
                print("현재 기회 : ", chance)
                end = time.time()
                et = end - start
                et = format(et, ".2f")
                print("\n속도 : ", et, "초")
                continue
            else:
                print("\n오답입니다..\n")
                score = score - 30
                chance = chance - 1
                print("현재 점수 : ", score)
                print("현재 기회 : ", chance)
                end = time.time()
                et = end - start
                et = format(et, ".2f")
                print("\n속도 : ", et, "초")
                continue
        
    print("\n\nGame Over...")
    print("누적 점수 : ", score)
    input("")


ready_game()
game() 