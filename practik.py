#N = int(input("Введи число: "))

#fact = 1

#for i in range(1, N + 1):
 #   fact *= i
#print(f"Факториал числа {N} равен {fact}")

def f(s):
    if s:
        s[0 + f(s[1:])
    else:
        return 0
f([1,2,3,4])
