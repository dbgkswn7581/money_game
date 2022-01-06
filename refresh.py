import psycopg2
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

  conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
  c = conn.cursor()
  c.execute('UPDATE {} SET value=? WHERE num=%s'.format(name), (int(value), num))
  c.execute('UPDATE {} SET date=? WHERE num=%s'.format(name), (date, num))
  c.execute('UPDATE {} SET clock=? WHERE num=%s'.format(name), (clock, num))
  conn.commit()
  c.close()
  conn.close()

  conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
  c = conn.cursor()
  c.execute('UPDATE stock SET value=%s WHERE company=%s', (int(value), name))
  c.execute('UPDATE stock SET before=%s WHERE company=%s', (before_value, name))
  c.execute('UPDATE stock SET date=%s WHERE company=%s', (date, name))
  c.execute('UPDATE stock SET clock=%s WHERE company=%s', (clock, name))
  c.execute('UPDATE stock SET num=%s WHERE company=%s', (num, name))
  conn.commit()
  c.close()
  conn.close()

      


def refresh():
    conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
    c = conn.cursor()
    c.execute('SELECT * FROM stock WHERE company=%s', ('meta',))
    meta = c.fetchone()
    c.execute('SELECT * FROM stock WHERE company=%s', ('didim',))
    didim = c.fetchone()
    c.execute('SELECT * FROM stock WHERE company=%s', ('gonglyoug',))
    gonglyoug = c.fetchone()
    c.execute('SELECT * FROM stock WHERE company=%s', ('nuli',))
    nuli = c.fetchone()
    c.execute('SELECT * FROM stock WHERE company=%s', ('hangil',))
    hangil = c.fetchone()
    c.execute('SELECT * FROM stock WHERE company=%s', ('singom',))
    singom = c.fetchone()

    c.close()
    conn.close()

    time = get_time()

    update_stock(meta, time)
    update_stock(didim, time)
    update_stock(gonglyoug, time)
    update_stock(nuli, time)
    update_stock(hangil, time)
    update_stock(singom, time)



    
