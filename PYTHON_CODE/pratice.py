# 오늘의 문제 : 계산기 클래스 만들기
class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first+self.second
        return result

    def minus(self):
        result = self.first-self.second
        return result

    def mul(self):
        result = self.first*self.second
        return result

    def div(self):
        result = self.first/self.second
        return result


a = float(input("첫 번째 숫자를 입력해주세요 : "))
b = float(input("두 번째 숫자를 입력해주세요 : "))
cal = Calculator(a, b)
print("덧셈 : ", cal.add(), "뺄셈 : ", cal.minus())
print("곱셈 : ", cal.mul(), "나눗셈 : ", cal.div())
