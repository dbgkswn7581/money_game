import sqlite3
from randoms import random_value
from get_time import get_time

def update_stock(company, time):
  date = time['date']
  clock = time['clock']

  name = company[0]
  before_value = int(company[1])
  value = random_value(before_value)
  before_num = int(company[5])
  num = before_num + 1 if not before_num == 270 else 1

  conn = sqlite3.connect('{}.db'.format(name), isolation_level=None)
  c = conn.cursor()
  c.execute('UPDATE stock SET value=? WHERE num=?', (int(value), num))
  c.execute('UPDATE stock SET date=? WHERE num=?', (date, num))
  c.execute('UPDATE stock SET clock=? WHERE num=?', (clock, num))

  conn = sqlite3.connect('stock.db', isolation_level=None)
  c = conn.cursor()
  c.execute('UPDATE stock SET value=? WHERE company=?', (int(value), name))
  c.execute('UPDATE stock SET before=? WHERE company=?', (before_value, name))
  c.execute('UPDATE stock SET date=? WHERE company=?', (date, name))
  c.execute('UPDATE stock SET clock=? WHERE company=?', (clock, name))
  c.execute('UPDATE stock SET num=? WHERE company=?', (num, name))

      


def refresh():
    conn = sqlite3.connect('stock.db', isolation_level=None)
    c = conn.cursor()
    meta = c.execute('SELECT * FROM stock WHERE company=?', ('meta',))
    meta = meta.fetchone()
    didim = c.execute('SELECT * FROM stock WHERE company=?', ('didim',))
    didim = didim.fetchone()
    gonglyoug = c.execute('SELECT * FROM stock WHERE company=?', ('gonglyoug',))
    gonglyoug = gonglyoug.fetchone()
    nuli = c.execute('SELECT * FROM stock WHERE company=?', ('nuli',))
    nuli = nuli.fetchone()
    hangil = c.execute('SELECT * FROM stock WHERE company=?', ('hangil',))
    hangil = hangil.fetchone()
    singom = c.execute('SELECT * FROM stock WHERE company=?', ('singom',))
    singom = singom.fetchone()

    time = get_time()

    update_stock(meta, time)
    update_stock(didim, time)
    update_stock(gonglyoug, time)
    update_stock(nuli, time)
    update_stock(hangil, time)
    update_stock(singom, time)



    
