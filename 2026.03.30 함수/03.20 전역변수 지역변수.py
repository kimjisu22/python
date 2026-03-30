num = 10 #전역변수

def fun1():
    global num 
    num = 20
    print('num : ',num)

print('num: ', num)
fun1()
print('num: ', num)

