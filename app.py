from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/solution')
def solution():
    return render_template('solucao.html')

if __name__ == "__main__":
    app.run()

    
import math
from math import e

def f(x):
    func = "e**x-(2*x)-1"
    func_ajustada = func.replace("x", str(x))
    func_ajustada = func.replace("e", str(e))
    print(func_ajustada)
    return eval(func_ajustada)

def bisseccao():
    a = -30
    b = 30
    e = 0.001
    
    if f(a) * f(b) < 0:
        while(math.fabs(b-a)/2 > e):
            x1 = (a + b)/2
            if f(x1) == 0:
                break
            else:
                if f(a) * f(x1) < 0:
                    b = x1
                else:
                    a = x1
        print("O valor é da raiz ", x1)

    else:
        print("Não possui raiz")


