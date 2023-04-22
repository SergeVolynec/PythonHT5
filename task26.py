a = int(input("Введите число: "))
b = int(input("Введите степень: "))

def ext(a, b):
    if b == 1:
        return a
    return a*ext(a, b-1)


print (ext(a, b))
