#아래와 같이 은행 프로그램을 작성하세요

deposit = 0
withdraw = 0
balance = 0
while True:

    print("-----------------------------------")
    print(" 1.예금 | 2.출금 | 3.잔고 | 4.종료 ")
    print("-----------------------------------")
    num=int(input("선택>"))

    if num==1:
        deposit = int(input("예금액> "))
        balance+=deposit
        print(balance)
        continue
    elif num==2:
        withdraw = int(input("출금액> "))
        print(balance)
        balance-=withdraw
        print(balance)
        continue
    elif num==3:
        print("잔고액>",balance)
        continue
    elif num==4:
        print("프로그램 종료")
        break
    else:
        print("다시 입력해 주세요")
        continue
