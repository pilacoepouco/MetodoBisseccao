import math

from math import e

def f(x):
    func = "e**x-(2*x)-1"
    func_ajustada = func.replace("x", str(x))
    func_ajustada = func_ajustada.replace("e", str(e))
    return eval(func_ajustada)

def bisseccao():
    a = 1
    b = 2
    e = 0.001

    if f(a) * f(b) < 0:
        while(math.fabs(b-a)/2 > e):
            x1 = (a + b)/2
            print("INTERVALOS",x1)
            if f(x1) == 0:
                break
            else:
                if f(a) * f(x1) < 0:
                    b = x1
                else:
                    a = x1
        print("O valor é da raiz ", x1)
        # print(f(x1))
    else:
        print("Não possui raiz")


bisseccao()