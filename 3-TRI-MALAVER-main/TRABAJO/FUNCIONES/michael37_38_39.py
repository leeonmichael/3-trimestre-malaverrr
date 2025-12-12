# Ejercicio 1
def func37(a,b):
    x = a
    y = b
    while y:
        x,y = y,x%y
    moreno = x
    return moreno

# Ejercicio 2
def func38(lst):
    nieto = []
    for x in lst:
        if x not in nieto:
            nieto.append(x)
    return nieto

# Ejercicio 3
def func39(s):
    michael_david = ''.join(ch for ch in s if ch.isalpha())
    return michael_david


