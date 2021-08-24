print("7개의 수를 입력받고 그 수들의 평균을 구하는 프로그램을 작성해보세요.")

lst = []

for i in range(7):
    lst.append(int(input("정수를 입력하세요 :")))

average = sum(lst)/len(lst)
print("평균 :", average)
