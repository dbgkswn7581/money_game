import random
import numpy as np

def random_value(value):
    li = ['plus', 'zero', 'minus']
    cho = np.random.choice(li, 1, p=[0.41,0.04,0.55])

    lli = ['vs','s','m','b','vb','sp']

    llii = np.random.choice(lli, 1, p=[0.55,0.35,0.05,0.03,0.015,0.005])
    if llii == 'vs':
        num = random.randrange(1,60)
    elif llii == 's':
        num = random.randrange(61,120)
    elif llii == 'm':
        num = random.randrange(121,180)
    elif llii == 'b':
        num = random.randrange(181,240)
    elif llii == 'vb':
        num = random.randrange(241,300)
    elif llii == 'sp':
        sp = [0.3,0.5,0.7,0.1,1.25,1.5,1.75,2]
        e = random.choice(sp)


    if llii == 'sp':
        return int(value * e)
    else:
        if cho == 'plus':
            return value + num
        elif cho == 'minus':
            if (value-num) <= 0:
                return value
            else:
                return value - num
        elif cho == 'zero':
            return value
