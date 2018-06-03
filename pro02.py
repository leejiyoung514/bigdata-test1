#11
#5개의 숫자를 키보드로 이력받아 평균을 구하는 프로그램을 작성하세요
#숫자는 콤마(,)로 구분하여 입력합니다.

sum=0
num=input("숫자 5개를 , 로 구분하여 입력하세요:")
list=num.split(",")
list=[int(i) for i in list]
for i in range(len(list)):
    sum+=list[i]
average=sum/len(list)
print("평균은", average, " 입니다.")