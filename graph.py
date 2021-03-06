from matplotlib import pyplot as plt
import psycopg2

def save_graph(com):
    conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
    c = conn.cursor()
    c.execute('SELECT * FROM stock WHERE company=%s', (com, ))
    com = c.fetchone()
    name = com[0]
    now = int(com[5])

    x_values = []
    y_values = []


    conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
    c = conn.cursor()

    for i in range(1,271):
        num = now + i if not (now+i) > 270 else now + i - 270
        
        c.execute('SELECT * FROM {} WHERE num=%s'.format(name), (num, ))
        d = c.fetchone()

        

        time = str(d[2]) + ' ' + str(d[3])

        x_values.append(time)
        y_values.append(int(d[1]))
        
    c.close()
    conn.close()

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

