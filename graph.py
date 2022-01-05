from matplotlib import pyplot as plt
import sqlite3

def save_graph(com):
    conn = sqlite3.connect('stock.db', isolation_level=None)
    c = conn.cursor()
    c = c.execute('SELECT * FROM stock WHERE company=?', (com, ))
    com = c.fetchone()
    name = com[0]
    now = int(com[5])

    x_values = []
    y_values = []
    db = name + '.db'

    conn = sqlite3.connect(db, isolation_level=None)
    c = conn.cursor()

    for i in range(1,271):
        num = now + i if not (now+i) > 270 else now + i - 270
        
        d = c.execute('SELECT * FROM stock WHERE num=?', (num, ))
        d = d.fetchone()

        time = str(d[2]) + ' ' + str(d[3])

        x_values.append(time)
        y_values.append(int(d[1]))
    
    if name == 'meta':
        plt_color = 'BurlyWood'
    elif name == 'didim':
        plt_color = 'BlueViolet'
    elif name == 'gonglyoug':
        plt_color = 'Crimson'
    elif name == 'nuli':
        plt_color = 'DarkOrange'
    elif name == 'hangil':
        plt_color = 'Gold'    
    elif name == 'singom':
        plt_color = 'ForestGreen'


    plt.figure(figsize=(10,5))
    plt.plot(x_values,y_values,linewidth=2,color=plt_color)
    # plt.plot(x_values,y_values,marker='o',linewidth=2,color=plt_color)
    plt.xlabel('time')
    plt.ylabel('value')

    
    plt.savefig('%s.png' %name)

