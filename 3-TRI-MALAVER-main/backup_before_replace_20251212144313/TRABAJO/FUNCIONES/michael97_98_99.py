# Ejercicio 1
def func97(a,b):
    x = a
    y = b
    while y:
        x,y = y,x%y
    moreno_nieto = x
    return moreno_nieto

# Ejercicio 2
def func98(lst):
    michael = []
    for x in lst:
        if x not in michael:
            michael.append(x)
    return michael

# Ejercicio 3
def func99(s):
    david = ''.join(ch for ch in s if ch.isalpha())
    return david


