def bisection(f, interval, precision):

    if f(interval[0]) * f(interval[1]) > 0:
        return 'f(a) x f(b) são maior que 0'
    
    interval.sort()

    e = [precision]

    i = 1

    r = sum(interval) / 2
    e.append(interval[1] - interval[0])

    print( '- --------------------------------------- -')
    print( '- Interação        Raiz          Precisão -')
    print( '- ---------     -----------      -------- -')
    while e[i] > e[0] or f(r) == 0:
        if f(r) < 0:
            interval[0] = r
        
        else:
            interval[1] = r
        
        print('  {:>5}    {:>12}   {:>14}'.format(i, round(r, 4), round(e[i], 4)))

        r = sum(interval) / 2
        e.append(interval[1] - interval[0])

        i += 1
    
    
    return r