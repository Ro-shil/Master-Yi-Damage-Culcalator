import math

Damage = 0 #입힌 대미지값
Start_EH = 0 #체력 비율 계산을 위한 초기 체력

while True: #전체 반복문
    Level = int(input("마스터 이의 레벨을 입력하세요: "))
    while True: #레벨 숫자 여부 확인 및 1~18 사이 값만 입력
        if str(Level).isdigit() == False:
            print("숫자만 입력하세요.")
            Level = input("마스터 이의 레벨을 입력하세요: ")
            continue
        elif Level < 1 or Level > 18:
            print("1~18 사이의 값을 입력하세요.")
            Level = input("마스터 이의 레벨을 입력하세요: ")
            continue
        else:
            break

    AD = 65 + 2.5*Level
    round(AD)

    EH = input("적의 체력을 입력하세요: ")
    while True: #체력 숫자 여부 확인
        if EH.isdigit() == False:
            print("숫자만 입력하세요.")
            EH = input("적의 체력을 입력하세요: ")
            continue
        else:
            break
    Start_EH = EH
    EA = input("적의 방어력을 입력하세요: ")
    while True: #방어력 숫자 여부 확인
        if EA.isdigit() == False:
            print("숫자만 입력하세요.")
            EA = input("적의 방어력을 입력하세요: ")
            continue
        else:
            break
    EMR = input("적의 마법 저항력을 입력하세요: ")
    while True: #마멉저항력 숫자 여부 확인
        if EMR.isdigit() == False:
            print("숫자만 입력하세요.")
            EMR = input("적의 마법 저항력을 입력하세요: ")
            continue
        else:
            break

    #크라켄 학살자 대미지 구간
    KL = Level-8
    if KL<0:
        KL = 0
    KSPmin = 150 + 5*KL
    KSPmax = 225 + 7.5*KL
    round(KSPmax)

    #구인수 활성화 여부
    G = input("구인수의 격노검 효과를 활성화하시겠습니까?(Y/N): ")
    G_A = "O"
    while True:
        if G == "Y" or G == "y":
            G_A = "O"
            break
        elif G == "N" or G == "n":
            G_A = "X"
            break
        else:
            print("Y or N만 입력하세요.")
            G = input("구인수의 격노검 효과를 활성화하시겠습니까?(Y/N , 구인수는 풀스택): ")

    #경계 활성화 여부
    T = input("경계 효과를 활성화하시겠습니까?(Y/N): ")
    T_A = "O"
    while True:
        if T == "Y" or T == "y":
            T_A = "O"
            break
        elif T == "N" or T == "n":
            T_A = "X"
            break
        else:
            print("Y or N만 입력하세요.")
            T = input("경계 효과를 활성화하시겠습니까?(Y/N , 경계는 풀스택): ")

    #재확인
    while True:
        print(f"적 체력: [{EH}] / 적 방어력: [{EA}] / 적 마법 저항력: [{EMR}]")
        print(f"레벨: [{Level}] / 공격력: [{AD}] / 크라켄 학살자의 최소 대미지: [{KSPmin}] / 크라켄 학살자의 최대 대미지 [{KSPmax}]")
        Decision = input("결정하시겠습니까? (Y/N): ")

        while True:
            if Decision == "Y" or Decision == "y":
                break  
            elif Decision == "N" or Decision == "n":
                break
            else:
                print("Y or N만 입력하세요.")
                continue
        
        break

    if Decision == "Y" or Decision == "y":
        break
    elif Decision == "N" and Decision == "N":
        continue