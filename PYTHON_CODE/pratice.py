print("""오늘의 문제 : 튜플과 딕셔너리로 문자열 길이 출력하기

3개의 문자열이 담긴 튜플을 선언하고, 딕셔너리를 통해 각각의 문자열의 길이를 저장한뒤 출력해보세요.
출력 예시 : {'Hello': 5, 'This is Python': 14, 'Bye': 3}
""")

tuple_lst = ("Hello", "This is python", "Bye")
dict_lst = {}

for i in tuple_lst:
    dict_lst[i] = len(i)

print("정답 : ", dict_lst)
