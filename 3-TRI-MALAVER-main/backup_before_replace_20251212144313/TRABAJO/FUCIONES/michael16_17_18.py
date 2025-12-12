def func16(n):
    a,b = 0,1
    i = 0
    while i<n:
        a,b = b,a+b
        i += 1
    moreno = a
    return moreno

def func17(a,b):
    x = a
    y = b
    while y:
        x,y = y,x%y
    nieto = x
    return nieto

def func18(lst):
    michael_david = []
    for x in lst:
        if x not in michael_david:
            michael_david.append(x)
    return michael_david


