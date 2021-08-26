class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first+self.second
        return result

    def sub(self):
        result = self.first-self.second
        return result

    def mul(self):
        result = self.first*self.second
        return result

    def dev(self):
        result = self.first/self.second
        return result


class PerfectCal(Calculator):
    def modulo(self):
        result = self.first % self.second
        return result

    def devide_int(self):
        result = self.first//self.second
        return result


a = float(input("숫자를 입력하시오.: "))
b = float(input("숫자를 입력하시오,: "))

n = PerfectCal(a, b)
print("덧셈결과: " + str(n.add()))
print("뺄셈결과: " + str(n.sub()))
print("곱셈결과: " + str(n.mul()))
print("나눗셈결과: " + str(n.dev()))

print("나눗셈 결과(정수): ", {n.devide_int()}, "입니다.")
print("나머지: ", {n.modulo()}, "입니다.")
