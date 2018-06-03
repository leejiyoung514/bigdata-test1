import random
#13
#set을 사용하여 1~45까지의 숫자 중 임의의 6개의 숫자를 콤마(,)로 구분하여 출력하세요


num=set(random.sample(range(1,46),6))
print(num)