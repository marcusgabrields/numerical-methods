"""

"""
from math import cos, sin, tan, exp

def  estranhaestranh(x):
    return 2**x - x**2



def bissecao(f,a,b,prec):
    """ Método da bisseção para uma função f no intervalo [a,b]. """
    m = (a+b)/2
    # Se já há precisão suficiente, retornamos o ponto médio do intervalo
    if abs(b - a) < prec: return m
    # Se f(m) == 0, achamos uma raiz exata!
    if f(m) == 0: return m

    # Senão, vamos por recorrência
    if f(m)*f(a) < 0: return bissecao(f,a,m,prec)
    else: return bissecao(f,m,b,prec)

def q(x):
    return exp(x) + tan(x)

print('{}: {}'.format('COS', bissecao(cos, -2, 1, 1e-03)))
print('{}: {}'.format('SIN', bissecao(sin, -2, 3, 1e-03)))
print('{}: {}'.format('SIN', bissecao(q, -1, 0, 1e-03)))

# print()
# r = bissecao(sin, -1, 0, 1e-03)
# print(r)
# print(round(r, 4))