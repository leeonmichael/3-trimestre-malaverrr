def func46(n):
    a,b = 0,1
    i = 0
    while i<n:
        a,b = b,a+b
        i += 1
    michael_david = a
    return michael_david

def func47(a,b):
    x = a
    y = b
    while y:
        x,y = y,x%y
    david_moreno = x
    return david_moreno

def func48(lst):
    moreno_nieto = []
    for x in lst:
        if x not in moreno_nieto:
            moreno_nieto.append(x)
    return moreno_nieto


