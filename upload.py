import sqlite3

def upload(user_id, com, amount, now_value, date, clock):
    conn = sqlite3.connect('user.db', isolation_level=None)
    c = conn.cursor()
    data = c.execute('SELECT * FROM user WHERE id=?', (str(user_id),))
    data = data.fetchone()
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
    conn = sqlite3.connect('user.db', isolation_level=None)
    c = conn.cursor()
    c.execute('UPDATE user SET money=? WHERE id=?', (after_money, str(user_id)))
    c.execute('UPDATE user SET stock=? WHERE id=?', (res, str(user_id)))
    

