from matplotlib import pyplot as plt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from main import find_now_num


def save_graph(com):
    if com == 'all':
        ref = db.reference()
        dic = ref.get()

        ce = dic['ce']
        go = dic['go']
        mk = dic['mk']
        nl = dic['nl']
        pd = dic['pd']
        pg = dic['pg']
        sl = dic['sl']
        sn = dic['sn']
        tc = dic['tc']
        ua = dic['ua']

        companys = [ce, go, mk, nl, pd, pg, sl, sn, tc, ua]
        
        x_companys = []
        y_companys = []
        x_values = []
        y_values = []
        for i in companys:
            for j in range(0, 10):
                now = find_now_num(i)
                s = now + j
                if s > 10:
                    s = s - 10
                x_values.append(i[s]['time'])
                y_values.append(i[s]['value'])
            x_companys.append(x_values)
            y_companys.append(y_values)
            x_values = []
            y_values = []

        plt.figure(figsize=(10,10))

        plt.plot(x_companys[0],y_companys[0],marker='o',linewidth=2,color='BurlyWood',label='Core')
        plt.plot(x_companys[1],y_companys[1],marker='o',linewidth=2,color='BlueViolet', label='Gaon')
        plt.plot(x_companys[2],y_companys[2],marker='o',linewidth=2,color='Crimson', label='Mako')
        plt.plot(x_companys[3],y_companys[3],marker='o',linewidth=2,color='DarkOrange', label='Nyalung')
        plt.plot(x_companys[4],y_companys[4],marker='o',linewidth=2,color='Gold', label='Panda')
        plt.plot(x_companys[5],y_companys[5],marker='o',linewidth=2,color='ForestGreen', label='Penguin')
        plt.plot(x_companys[6],y_companys[6],marker='o',linewidth=2,color='MidnightBlue', label='Silu')
        plt.plot(x_companys[7],y_companys[7],marker='o',linewidth=2,color='Moccasin', label='Sine')
        plt.plot(x_companys[8],y_companys[8],marker='o',linewidth=2,color='Peru', label='TiChib')
        plt.plot(x_companys[9],y_companys[9],marker='o',linewidth=2,color='DarkCyan', label='Yuna')
        plt.legend()
        plt.xlabel('time')
        plt.ylabel('value')
        
        # plt.show()
        plt.savefig('all.png')



    else:
        ref = db.reference()
        dic = ref.get()

        com_dic = dic[com]

        now = find_now_num(com_dic)
        now = now + 1
        x_values = []
        y_values = []

        for i in range(0,10):
            s = now + i
            if s > 10:
                s = s - 10

            x_values.append(com_dic[s]['time'])
            y_values.append(com_dic[s]['value'])
        
        if com == 'ce':
            plt_color = 'BurlyWood'
        elif com == 'go':
            plt_color = 'BlueViolet'
        elif com == 'mk':
            plt_color = 'Crimson'
        elif com == 'nl':
            plt_color = 'DarkOrange'
        elif com == 'pd':
            plt_color = 'Gold'    
        elif com == 'pg':
            plt_color = 'ForestGreen'
        elif com == 'sl':
            plt_color = 'MidnightBlue'
        elif com == 'sn':
            plt_color = 'Moccasin'
        elif com == 'tc':
            plt_color = 'Peru'
        elif com == 'ua':
            plt_color = 'DarkCyan'

        plt.figure(figsize=(10,5))
        plt.plot(x_values,y_values,marker='o',linewidth=2,color=plt_color)
        plt.xlabel('time')
        plt.ylabel('value')

        
        plt.savefig('%s.png' %com)

save_graph('all')

