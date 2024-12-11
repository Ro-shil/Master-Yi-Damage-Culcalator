import math

Damage = 0 #입힌 대미지값
Start_EH = 0 #체력 비율 계산을 위한 초기 체력

while True: #전체 반복문
    Level = int(input("마스터 이의 레벨을 입력하세요: "))
    while True: #레벨 숫자 여부 확인 및 1~18 사이 값만 입력
        if str(Level).isdigit() == False:
            print("숫자만 입력하세요.")
            int(Level = input("마스터 이의 레벨을 입력하세요: "))
            continue
        elif Level < 1 or Level > 18:
            print("1~18 사이의 값을 입력하세요.")
            int(Level = input("마스터 이의 레벨을 입력하세요: "))
            continue
        else:
            break

    AD = 65 + 2.5*Level
    round(AD)

    EH = int(input("적의 체력을 입력하세요: "))
    while True: #체력 숫자 여부 확인
        if str(EH).isdigit() == False:
            print("숫자만 입력하세요.")
            int(EH = input("적의 체력을 입력하세요: "))
            continue
        else:
            break
    Start_EH = EH
    EA = int(input("적의 방어력을 입력하세요: "))
    while True: #방어력 숫자 여부 확인
        if str(EA).isdigit() == False:
            print("숫자만 입력하세요.")
            EA = int(input("적의 방어력을 입력하세요: "))
            continue
        else:
            break
    EMR = int(input("적의 마법 저항력을 입력하세요: "))
    while True: #마멉저항력 숫자 여부 확인
        if str(EMR).isdigit() == False:
            print("숫자만 입력하세요.")
            EMR = int(input("적의 마법 저항력을 입력하세요: "))
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

        if Decision == "Y" or Decision == "y":
            break

    if Decision == "Y" or Decision == "y":
            break


HP = EH/Start_EH #체력비율
AC = 0 #공격횟수
KAC = 0 #크라켄 공격횟수
GAC = 0 #구인수 공격횟수
KSD = 0 #크라켄 대미지
PKSD = 0 #이전 크라켄 대미지


#기본공격
def AA():
    global EH
    global AC
    EH = EH - (AD/1+(EA*0.01))
    AC = AC + 1

#마스터이 패시브
def PAA():
    global EH
    global AC
    EH = EH - ((AD/2)/1+(EA*0.01))
    AC = AC + 1


#몰락한 왕의 검 대미지
def RK():
    global EH
    EH = EH - (EH*0.08/1+(EA*0.01))

#크라켄 학살자 대미지
def KS():
    global HP
    global EH
    global AC
    global KSD
    global PKSD
    HP = EH/Start_EH
    KSD = KSPmin + (100-HP) * ((KSPmax - KSPmin)/100)
    PKSD = KSD
    EH = EH - (KSD/1+(EA*0.01))

#크라켄 대미지 0
def KS0():
    global HP
    global EH
    global AC
    global KSD
    global PKSD
    EH = EH + PKSD

#패시브 크라켄 학살자 대미지
def PKS():
    global HP
    global EH
    global AC
    global KSD
    HP = EH/Start_EH
    KSD = KSPmin + (100-HP) * ((KSPmax - KSPmin)/100)
    EH = EH - ((KSD/2)/1+(EA*0.01))

def KGA(): #크라켄 구인수 발동
    global AC
    global KAC
    AC = AC + 1
    KAC = KAC + 1

def RGA(): #몰왕검 구인수 발동
    global AC
    AC = AC + 1

'''
#경계 활성화
TEA = EA - EA*0.3
'''

#크라켄 대미지
while True:
    if G_A == "X": #구인수 비활
        if T_A == "X": #구인수 비활 / 경계 비활
            AA()
            KAC = KAC + 1
            if AC % 4 == 0:
                PAA()
            if KAC % 3 == 0:
                KS()
                KAC = KAC + 1
                if AC % 5 == 0 and KAC % 3 == 0:
                    PAA()
                    KS0()
                    PKS()
            if EH <= 0:
                break
            '''
        elif T_A == "O": #구인수 비활 / 경계 활성화
            Terminus()
            AA()
            KAC = KAC + 1
            if KAC % 3 == 0:
                KS()
            if AC % 4 == 0:
                PAA()
                KAC = KAC + 1
                if AC % 5 == 0 and KAC % 3 == 0:
                    PAA()
                    KS0()
                    PKS()
            if EH <= 0:
                break
                '''

    if G_A == "O": #구인수 활성화
        if T_A == "X": #구인수 활성화 / 경계 비활
            AA()
            KAC = KAC + 1
            if AC % 4 == 0:
                PAA()
            if AC % 6 == 0:
                KGA()
            if KAC % 3 == 0:
                KS()
                KAC = KAC + 1
                if AC % 5 == 0 and KAC % 3 == 0:
                    PAA()
                    KS0()
                    PKS()
    
    if EH <= 0:
        break


print(f"계산 결과: 기본 공격 [{AC}]회")
