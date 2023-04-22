a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

def add(a,b):
    if b > a:
        a,b = b,a
    if b == 0:
        return a
    return  add(a, b-1) + 1

print(add(a,b))