import numpy as np

def get_gacha_list(worth):
    worth = int(worth)
    incre = [0,0.5,2,4,10,50,100]
    value = []
    for i in incre:
        value.append(int(round(worth*i)))
    
    return value


def gacha(times):
    # times = 뽑기 횟수
    # worth = 상자 가격
    incre = [0,0.5,2,4,10,50,100]
    result = [0,0,0,0,0,0,0,0,0,0]

    for i in range(times):
        coin = np.random.choice(incre, 1, p=[0.4494,0.105,0.4,0.04,0.005,0.0005,0.0001])
        where = incre.index(coin)
        result[where] += 1
    
    return result



