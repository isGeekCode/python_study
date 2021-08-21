n = int(input("정수를 입력하세요 : "))


def getSum(n):
    a = 0
    for i in range(n+1):    # 0부터 n까지 나열
        a += i  # i 만큼 a에 더해진다    ex)a +=1  1만큼 더해진다
    return a				# a 값을 내보내는 함수


result = getSum(n)  # result = a
print(result)
