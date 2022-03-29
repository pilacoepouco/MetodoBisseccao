from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

    
import math

def f(x):
    func = "x**2-5"
    func_ajustada = func.replace("x", str(x))
    return eval(func_ajustada)

def bisseccao():
    a = -30
    b = 30
    e = 0.001
    
    if f(a) * f(b) < 0:
        while(math.fabs(b-a)/2 > e):
            x1 = (a + b)/2
            if f(x1) == 0:
                # print("O valor é da raiz ", x1)
                break
            else:
                if f(a) * f(x1) < 0:
                    b = x1
                else:
                    a = x1
        print("O valor é da raiz ", x1)

    else:
        print("Não possui raiz")


