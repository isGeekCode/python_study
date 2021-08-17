# 변수 count를 0으로 선언
count = 0

# if로 반복문 사용
for i in range(1, 101):
    # i가 증가하면서 짝수, 동시에 7의 배수가 아닌 값
    if (i % 2 == 0) and (i % 7 != 0):
        count += 1
print("1부터 100까지의 수 중에서 짝수이면서 7의 배수가 아닌 수의 개수는 "+str(count) + "개 입니다")
