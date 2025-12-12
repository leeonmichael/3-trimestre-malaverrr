def func97(a,b):
    x = a
    y = b
    while y:
        x,y = y,x%y
    moreno_nieto = x
    return moreno_nieto

def func98(lst):
    michael = []
    for x in lst:
        if x not in michael:
            michael.append(x)
    return michael

def func99(s):
    david = ''.join(ch for ch in s if ch.isalpha())
    return david


