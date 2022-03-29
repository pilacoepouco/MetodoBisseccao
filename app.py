import math

a = 2
b = 5
e = 0.001
func = "x^2-5"


def f(x):
    func_ajustada = func.replace("x", x)
    return eval(func_ajustada)


def bisseccao():
    if f(a) * f(b) < 0:
        while(math.fabs(a)-math.fabs(b)/2 < e):
            x1 = (a + b)/2
            if x1 == 0:
                break
            else:
                if f(a) * f(x1) < 0:
                    b = x1
                else:
                    a = x1
        print("O valor é da raiz ", x1)
    else:
        print("Não possui raiz")

