def bmi(w=float(input('enter weight\n')), h=float(input('enter height\n'))):
    if h > 5:
        h = h/100
    h2 = h ** 2
    bm = round(w/h2, 1)
    p1 = round(18.6 * h2, 1)
    p2 = round(24.9 * h2, 1)
    s = ''
    if bm < 18.6:
        s = 'thin'
    elif bm >= 18.6 and bm < 25:
        s = 'healthy'
    elif bm >= 25 and bm < 30:
        s = 'overweight'
    else:
        s = 'obese'
    
    r = 'bmi = {}: you are {}, your perfect weight should be betwean {} and {}'.format(bm, s, p1, p2)
    return r
