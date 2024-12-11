Damage = 0
Start_Health = 0

while True: # 전체 반복문
    Health = input("체력을 입력하세요: ")
    Start_Health = Health
    Armor = input("방어력을 입력하세요: ")
    Magic_resistance = input("마법 저항력을 입력하세요: ")

    Attack_damage = input("공격력을 입력하세요: ")
    KSPmin = input("크라켄 학살자의 최소 대미지를 입력하세요: ")
    KSPmax = input("크라켄 학살자의 최대 대미지를 입력하세요: ")
    G = input("구인수의 격노검 효과를 활성화하시겠습니까?(Y/N , 구인수는 풀스택 기준): ")
    T = input("경계 효과를 활성화하시겠습니까?(Y/N , 경계는 풀스택 기준): ")

    G_A = "O"
    T_A = "O"

    while True: #구인수 활성화 여부
        if G == "Y" or G == "y":
            G_A = "O"
            break
        elif G == "N" or G == "n":
            G_A = "X"
            break
        else:
            print("Y or N만 입력하세요.")
            G = input("구인수의 격노검 효과를 활성화하시겠습니까?(Y/N , 구인수는 풀스택): ")

    while True: #경계 활성화 여부
        if T == "Y" or T == "y":
            T_A = "O"
            break
        elif T == "N" or T == "n":
            T_A = "X"
            break
        else:
            print("Y or N만 입력하세요.")
            T = input("경계 효과를 활성화하시겠습니까?(Y/N , 경계는 풀스택): ")

    while True: #체력 숫자 확인
        if Health.isdigit() == False:
            print("숫자만 입력하세요.")
            Health = input("체력을 입력하세요: ")
            Start_Health = Health
            continue
        else:
            break

    while True: #크라켄 대미지 숫자 확인
        if KSPmin.isdigit() == False:
            print("숫자만 입력하세요.")
            KSPmin = input("크라켄 학살자의 최소 대미지를 입력하세요: ")
            continue
        elif KSPmax.isdigit() == False:
            print("숫자만 입력하세요.")
            KSPmax = input("크라켄 학살자의 최대 대미지를 입력하세요: ")
            continue
        else:
            break

    while True: #재확인
        print(f"적 체력: {Health} / 적 방어력: {Armor} / 적 마법 저항력: {Magic_resistance}")
        print(f"공격력: {Attack_damage} / 구인수 효과 활성화 여부: {G_A} / 경계 효과 활성화 여부: {T_A}")
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

    def Damage_calculation()
        Health = Health - (Attack_damage/(1+Armor*0.01))
    def RK()
        Health = Health - (Health*0.08/(1+Armor*0.01))
    def KS()
        
    def Terminus()
        Armor = Armor - Armor*0.3
    