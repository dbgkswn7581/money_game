import psycopg2

def upload(user_id, com, amount, now_value, date, clock):
    conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
    c = conn.cursor()
    data = c.execute('SELECT * FROM "user" WHERE id=%s', (str(user_id),))
    data = data.fetchone()
    c.close()
    conn.close()
    money = data[2]
    stock = data[4]
    stock = stock.split('&')
    total = int(amount) * int(now_value)
    after_money = int(money) - total
    ans = [com, now_value, amount, date, clock]
    ans = str(ans)

    for i in range(10):
        j = stock[i]
        if j == '0':
            stock[i] = ans
            break
    res = ''
    for i in range(10):
        j = stock[i]

        res = res + '&' + j
    res = res[1:]
    conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
    c = conn.cursor()
    c.execute('UPDATE "user" SET money=%s WHERE id=%s', (after_money, str(user_id)))
    c.execute('UPDATE "user" SET stock=%s WHERE id=%s', (res, str(user_id)))
    conn.commit()
    c.close()
    conn.close()
    

