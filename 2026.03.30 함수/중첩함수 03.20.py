def divFunc(n1,n2):

    def divOper(num1, num2):
        return num1 / num2

    if n2 != 0:
        result = divOper(n1,n2)

    elif n2 == 0:
        result = '0으로 나눌 수 없습니다'

    return result

print(divFunc(10,0))
print(divFunc(10,2))
