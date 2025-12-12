def func76(n):
    a,b = 0,1
    i = 0
    while i<n:
        a,b = b,a+b
        i += 1
    moreno_nieto = a
    return moreno_nieto

def func77(a,b):
    x = a
    y = b
    while y:
        x,y = y,x%y
    michael = x
    return michael

def func78(lst):
    david = []
    for x in lst:
        if x not in david:
            david.append(x)
    return david


