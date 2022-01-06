import psycopg2
from matplotlib.colors import is_color_like
from matplotlib.pyplot import title
from get_time import get_time
from replace import replace_amount
from graph import save_graph
import discord
from real_stock import real_stock, kospi
from upload import upload



def re_time():
  time = get_time()

  conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
  c = conn.cursor()
  c.execute('SELECT * FROM stock WHERE company=%s', ('meta',))
  d = c.fetchone()
  c.close()
  conn.close()
  before_time = d[4]
  time_gap = int(time['clock'][3:5]) - int(before_time[3:5])
    
  if time_gap == 0:
    second_gap = int(time['clock'][6:]) - int(before_time[6:])
    re = {'gap' : second_gap, 'type' : 'sec'}
    return re
  else:
    re = {'gap' : time_gap, 'type' : 'min'}
    return re

def get_stock(tuple):
  pm = '+' if (tuple[1]-tuple[2]) >= 0 else '-'
  value = tuple[1]
  value = format(value, ',')

  gap = str(((tuple[2]-tuple[1])*(-1)) if (tuple[2]-tuple[1]) < 0 else (tuple[2]-tuple[1]))
  gap = format(int(gap), ',')

  
  if tuple[2]-tuple[1] == 0:
    gap = '-'
  elif pm == '+':
    gap = '▲' + gap
  elif pm == '-':
    gap = '▼' + gap

  list = [pm, value, gap]

  return list

def get_restock(tuple):
  pm = '+' if tuple[2][0] == '+' else '-'
  value = tuple[1]
  gap = tuple[2][1:]
  
  if tuple[2][0] == '+':
    gap = '▲' + gap
  elif tuple[2][0] == '-':
    gap = '▼' + gap

  list = [pm, value, gap]

  return list

def find_company(input):
  if input == '메타증권' or input == '메타' or input == 'ax' or input == 'axwr' or input == 'ㅁㅌ' or input == 'ㅁㅌㅈㄱ':
    return 'meta'
  elif input == '디딤건설' or input == '디딤' or input == 'ee' or input == 'eert' or input == 'ㄷㄷ' or input == 'ㄷㄷㄳ' or input == 'ㄷㄷㄱㅅ':
    return 'didim'
  elif input == '공룡제약' or input == '공룡' or input == 'rf' or input == 'rfwd' or input == 'ㄱㄹ' or input == 'ㄱㄹㅈㅇ':
    return 'gonglyoug'
  elif input == '누리마켓' or input == '누리' or input == 'sf' or input == 'sfaz' or input == 'ㄴㄹ' or input == 'ㄴㄻㅋ' or input == 'ㄴㄹㅁㅋ':
    return 'nuli'
  elif input == '한길그룹' or input == '한길' or input == 'gr' or input == 'grrf' or input == 'ㅎㄱ' or input == 'ㅎㄱㄱㄹ':
    return 'hangil'
  elif input == '신곰화학' or input == '신곰' or input == 'tr' or input == 'trgg' or input == 'ㅅㄱ' or input == 'ㅅㄱㅎㅎ':
    return 'singom'
  elif input == '삼성전자' or input == '삼전' or input == '삼성' or input == 'ㅅㅅㅈㅈ' or input == 'ㅅㅈ' or input == 'ㅅㅅ' or input == 'ttww' or input == 'tw' or input == 'tt' or input == 'samsung':
    return 'samsung'
  elif input == '현대차' or input == '현대' or input == 'ㅎㄷ' or input == 'ㅎㄷㅊ' or input == 'hyundai' or input == 'ge' or input == 'gec' or input == 'hyundaicar' or input == 'hyundai_car':
    return 'hyundai'
  elif input == '네이버' or input == 'ㄴㅇㅂ' or input == 'naver' or input == 'sdq' or input == 'NAVER':
    return 'naver'
  elif input == '코오롱인더우' or input == '코오롱' or input == 'ㅋㅇㄹㅇㄷㅇ' or input == 'ㅋㅇㄹ' or input == 'kolon' or input == 'kolon_ina' or input == 'zdfded' or input == 'zdf':
    return 'kolon'
  elif input == '대한항공' or input == '대한' or input == 'ㄷㅎㅎㄱ' or input == 'ㄷㅎ' or input == 'korean_air' or input == 'korean' or input == 'korea' or input == 'eg' or input == 'eggr':
    return 'korean'
  elif input == '카카오' or input == 'ㅋㅋㅇ' or input == 'kakao' or input == 'zzd' or input == 'KAKAO':
    return 'kakao'

def return_TF_company(company):
  companys = ['meta','didim','gonglyoug','nuli','hangil','singom','samsung','hyundai','naver','kolon','korean','kakao']
  if company in companys:
    return 'T'
  else:
    return 'F'

def kr_company(com):
  if com =='meta':
    return '메타증권'
  elif com == 'didim':
    return '디딤건설'
  elif com == 'gonglyoug':
    return '공룡제약'
  elif com == 'nuli':
    return '누리마켓'
  elif com == 'hangil':
    return '한길그룹'
  elif com == 'singom':
    return '신곰화학'
  elif com =='samsung':
    return '삼성전자'
  elif com == 'hyundai':
    return '현대차'
  elif com == 'naver':
    return 'NAVER'
  elif com == 'kolon':
    return '코오롱인더우'
  elif com == 'korean':
    return '대한항공'
  elif com == 'kakao':
    return '카카오'

def get_diff(company, value, amount):
  
  
  if company == 'meta' or company == 'didim' or company == 'gonglyoug' or company == 'nuli' or company == 'hangil' or company == 'singom':
    conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
    c = conn.cursor()
    c.execute('SELECT * FROM stock WHERE company=%s', (company,))
    d = c.fetchone()
    c.close()
    conn.close()
    now = d[1]
    diff = int(value) - int(now)

    if diff < 0:
      diff = diff * (-1)
      res = '-' + replace_amount(diff * int(amount))
    else:
      res = '+' + replace_amount(diff * int(amount))
    
    return res

  elif company == 'samsung' or company == 'hyundai' or company == 'naver' or company == 'kolon' or company == 'korean' or company == 'kakao':
    conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
    c = conn.cursor()
    c.execute('SELECT * FROM restock WHERE company=%s', (company,))
    d = c.fetchone()
    c.close()
    conn.close()
    now = d[1]
    now = now.replace(',','')

    diff = int(value) - int(now)
    
    if diff < 0:
      diff = diff * (-1)
      res = '-' + replace_amount(diff * int(amount))
    else:
      res = '+' + replace_amount(diff * int(amount))
    
    return res

def stock(ctx, text):
    user_id = ctx.author.id
    user_keys = []
    if text == ():
        conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
        c = conn.cursor()
        c.execute('SELECT * FROM "user" WHERE id=%s', (str(user_id),))
        data = c.fetchone()
        c.close()
        conn.close()
        choose = data[3]

        conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
        c = conn.cursor()

        c.execute('SELECT * FROM stock WHERE company=%s', ('meta',))
        mt = c.fetchone()
        mt = get_stock(mt)
        c.execute('SELECT * FROM stock WHERE company=%s', ('didim',))
        dd = c.fetchone()
        dd = get_stock(dd)
        c.execute('SELECT * FROM stock WHERE company=%s', ('gonglyoug',))
        gl = c.fetchone()
        gl = get_stock(gl)
        c.execute('SELECT * FROM stock WHERE company=%s', ('nuli',))
        nl = c.fetchone()
        nl = get_stock(nl)
        c.execute('SELECT * FROM stock WHERE company=%s', ('hangil',))
        hg = c.fetchone()
        hg = get_stock(hg)
        c.execute('SELECT * FROM stock WHERE company=%s', ('singom',))
        sg = c.fetchone()
        sg = get_stock(sg)
        c.close()
        conn.close()

        conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
        c = conn.cursor()
        c.execute('SELECT * FROM restock WHERE company=%s', ('samsung',))
        samsung = c.fetchone()
        samsung = get_restock(samsung)
        c.execute('SELECT * FROM restock WHERE company=%s', ('hyundai',))
        hyundai = c.fetchone()
        hyundai = get_restock(hyundai)
        c.execute('SELECT * FROM restock WHERE company=%s', ('naver',))
        naver = c.fetchone()
        naver = get_restock(naver)
        c.execute('SELECT * FROM restock WHERE company=%s', ('kolon',))
        kolon = c.fetchone()
        kolon = get_restock(kolon)
        c.execute('SELECT * FROM restock WHERE company=%s', ('korean',))
        korean = c.fetchone()
        korean = get_restock(korean)
        c.execute('SELECT * FROM restock WHERE company=%s', ('kakao',))
        kakao = c.fetchone()
        kakao = get_restock(kakao)

        c.close()
        conn.close()

        time_gap = re_time() # time_gap = {'gap' : time_gap, 'type' : 'min'}
        now_time = get_time()
        now_time = now_time['clock']

        
        if time_gap['type'] == 'min':
            if time_gap['gap'] < 0:
                time_gap['gap'] = time_gap['gap'] * (-1)
                time_gap['gap'] = 60 - time_gap['gap']
            
            embed1 = discord.Embed(
              title = '**NNSTG**',
              description = '주식 정보는 %d분 전 변동됐어요.\n현재 시간 : `%s`' %(time_gap['gap'], now_time),
              color = 0x00b09b)
            embed1.add_field(
              name = '메타증권',
              value = '```diff\n%s %s  (%s)```'%(mt[0], mt[1], mt[2]),
              inline=True)
            embed1.add_field(
              name = '디딤건설',
              value = '```diff\n%s %s  (%s)```'%(dd[0], dd[1], dd[2]),
              inline=True)
            embed1.add_field(
              name = '공룡제약',
              value = '```diff\n%s %s  (%s)```'%(gl[0], gl[1], gl[2]),
              inline=True)
            embed1.add_field(
              name = '누리마켓',
              value = '```diff\n%s %s  (%s)```'%(nl[0], nl[1], nl[2]),
              inline=True)
            embed1.add_field(
              name = '한길그룹',
              value = '```diff\n%s %s  (%s)```'%(hg[0], hg[1], hg[2]),
              inline=True)
            embed1.add_field(
              name = '신곰화학',
              value = '```diff\n%s %s  (%s)```'%(sg[0], sg[1], sg[2]),
              inline=True)

            embed2 = discord.Embed(
              title = '**KOSPI**',
              description = '`%s`' %(kospi()),
              color = 0xb00015)

            embed2.add_field(
              name = '삼성전자',
              value = '```diff\n%s %s  (%s)```'%(samsung[0], samsung[1], samsung[2]),
              inline=True)
            embed2.add_field(
              name = '현대차',
              value = '```diff\n%s %s  (%s)```'%(hyundai[0], hyundai[1], hyundai[2]),
              inline=True)
            embed2.add_field(
              name = 'NAVER',
              value = '```diff\n%s %s  (%s)```'%(naver[0], naver[1], naver[2]),
              inline=True)
            embed2.add_field(
              name = '코오롱인더우',
              value = '```diff\n%s %s  (%s)```'%(kolon[0], kolon[1], kolon[2]),
              inline=True)
            embed2.add_field(
              name = '대한항공',
              value = '```diff\n%s %s  (%s)```'%(korean[0], korean[1], korean[2]),
              inline=True)
            embed2.add_field(
              name = '카카오',
              value = '```diff\n%s %s  (%s)```'%(kakao[0], kakao[1], kakao[2]),
              inline=True)
            
        elif time_gap['type'] == 'sec':
            embed1 = discord.Embed(
              title = '**NNSTG**',
              description = '주식 정보는 %d분 전 변동됐어요.\n현재 시간 : `%s`' %(time_gap['gap'], now_time),
              color = 0x00b09b)

            embed1.add_field(
              name = '메타증권',
              value = '```diff\n%s %s  (%s)```'%(mt[0], mt[1], mt[2]),
              inline=True)
            embed1.add_field(
              name = '디딤건설',
              value = '```diff\n%s %s  (%s)```'%(dd[0], dd[1], dd[2]),
              inline=True)
            embed1.add_field(
              name = '공룡제약',
              value = '```diff\n%s %s  (%s)```'%(gl[0], gl[1], gl[2]),
              inline=True)
            embed1.add_field(
              name = '누리마켓',
              value = '```diff\n%s %s  (%s)```'%(nl[0], nl[1], nl[2]),
              inline=True)
            embed1.add_field(
              name = '한길그룹',
              value = '```diff\n%s %s  (%s)```'%(hg[0], hg[1], hg[2]),
              inline=True)
            embed1.add_field(
              name = '신곰화학',
              value = '```diff\n%s %s  (%s)```'%(sg[0], sg[1], sg[2]),
              inline=True)
            
            embed2 = discord.Embed(
              title = '**KOSPI**',
              description = '`%s`' %(kospi()),
              color = 0xb00015)

            embed2.add_field(
              name = '삼성전자',
              value = '```diff\n%s %s  (%s)```'%(samsung[0], samsung[1], samsung[2]),
              inline=True)
            embed2.add_field(
              name = '현대차',
              value = '```diff\n%s %s  (%s)```'%(hyundai[0], hyundai[1], hyundai[2]),
              inline=True)
            embed2.add_field(
              name = 'NAVER',
              value = '```diff\n%s %s  (%s)```'%(naver[0], naver[1], naver[2]),
              inline=True)
            embed2.add_field(
              name = '코오롱인더우',
              value = '```diff\n%s %s  (%s)```'%(kolon[0], kolon[1], kolon[2]),
              inline=True)
            embed2.add_field(
              name = '대한항공',
              value = '```diff\n%s %s  (%s)```'%(korean[0], korean[1], korean[2]),
              inline=True)
            embed2.add_field(
              name = '카카오',
              value = '```diff\n%s %s  (%s)```'%(kakao[0], kakao[1], kakao[2]),
              inline=True)
            
        if choose == 1:
          return {'one' : embed1, 'two' : embed2}

        elif choose == 2:
          return embed1
        
        elif choose == 2:
          return embed2
        

    else:
        order = text[0]
        user_id = ctx.author.id

        if order == '나' or order == 'ㄴ' or order=='s':
            conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
            c = conn.cursor()

            c.execute('SELECT id,nickname FROM "user"')
            user_s = c.fetchall()
            c.close()
            conn.close()
            user_keys = []
            for i in user_s:
                user_keys.append(i[0])

            if str(user_id) not in user_keys:
              ctx_text = "`$가입 (닉네임)`을 통해 시스템에 가입 후 이용바랍니다."
              return ctx_text

            else:
              

              conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
              c = conn.cursor()

              c.execute('SELECT * FROM "user" WHERE id=%s', (str(user_id),))
              data = c.fetchone()
              c.close()
              conn.close()

              have_stock = data[4].split('&')
              nickname = data[1]

              send = '{} 님의 보유 주식 정보입니다.\n```scss\n'.format(nickname)

              for i in range(10):
                j = have_stock[i]

                if not j == '0':
                  com_stock = j.replace('[','').replace(']','').split(',')
                  company = com_stock[0]
                  if "'" in company:
                    company = company.replace("'",'')
                  kor_com = kr_company(company)

                  value = com_stock[1]
                  amount = com_stock[2]

                  if ' ' in value:
                    value = value.replace(' ', '')
                  if "'" in value:
                    value = value.replace("'",'')
                  if ' ' in amount:
                    amount = amount.replace(' ', '')
                  if "'" in amount:
                    amount = amount.replace("'",'')

                  diff = get_diff(company, value, amount) # -> str() / ex) diff = '+199조 1억 2993'
                  send = send + "#{} [{}] : '{}주'; //{} {}\n손익 → {} {}\n".format(i+1, kor_com, replace_amount(int(com_stock[2])), com_stock[3], com_stock[4], diff[0], diff[1:])

              send = send+'```'

              if send == '```scss\n```':
                send = '보유하신 주식이 없습니다. `$주식`을 통해 주식 정보를 확인해보세요'
                return send
              else:
                return send


                

        elif order == '구매' or order == 'ㄱㅁ' or order == 'ra' or order == '구입' or order == 'ㄱㅇ' or order == 'rd' or order == 'buy' or order == '매수' or order == 'ㅁㅅ' or order == 'at':
            conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
            c = conn.cursor()

            c.execute('SELECT id,nickname FROM "user"')
            user_s = c.fetchall()
            c.close()
            conn.close()
            user_keys = []
            for i in user_s:
                user_keys.append(i[0])

            if str(user_id) not in user_keys:
                ctx_text = "`$가입 (닉네임)`을 통해 시스템에 가입 후 이용바랍니다."
                return ctx_text
                
            else:
                conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                c = conn.cursor()
                data = c.execute('SELECT * FROM "user" WHERE id=%s', (str(user_id),))
                data = data.fetchone()
                c.close()
                conn.close()
                money = int(data[2])
                stock = data[4].split('&')
                ch = ''

                for i in stock:
                  if not i == '0':
                    ch = ch+'a'

                if ch=='aaaaaaaaaa':
                  ctx_text = '보유하신 주식을 판매 후 주식을 구매해주시기 바랍니다.\n`$주식 나`을 통해 보유 주식을 확인하십시오'
                  return ctx_text

                else:
                  if len(text) != 3:
                      ctx_text = '잘못된 명령어입니다.\n예시 : `$주식 구매 펭귄증권 100`'
                      return ctx_text
                      
                  else:
                      company = text[1]
                      amount = text[2]
                      if type(company) != str:
                          ctx_text = '잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오'
                          return ctx_text
                      else:
                          com = find_company(company)
                          re_company = return_TF_company(com)
                          
                          if re_company == 'F':
                              ctx_text = '잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오'
                              return ctx_text
                              
                          else:
                              if amount == '다' or amount == 'ㄷ' or amount == 'all' or amount == 'e':
                                  com = find_company(company)
                                  kr_com = kr_company(com)

                                  if com == 'meta' or com == 'didim' or com == 'gonglyoug' or com == 'nuli' or com == 'hangil' or com == 'singom':
                                    conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                                    c = conn.cursor()
                                    c.execute('SELECT * FROM stock WHERE company=%s', (com,))
                                    d = c.fetchone()
                                    c.close()
                                    conn.close()
                                    now_value = d[1]


                                  elif com == 'samsung' or com == 'hyundai' or com == 'naver' or com == 'kolon' or com == 'korean' or com == 'kakao':
                                    conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                                    c = conn.cursor()
                                    c.execute('SELECT * FROM restock WHERE company=%s', (com,))
                                    d = c.fetchone()
                                    c.close()
                                    conn.close()
                                    now = d[1]
                                    now_value = now.replace(',','')
                                    now_value = int(now_value)


                                  conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                                  c = conn.cursor()
                                  c.execute('SELECT * FROM "user" WHERE id=%s', (str(user_id),))
                                  data = c.fetchone()

                                  c.close()
                                  conn.close()

                                  amount = int(money / now_value)

                                  if (amount * now_value) > money:
                                      ctx_text = '보유 금액이 부족합니다.'
                                      return ctx_text
                                      
                                  else:
                                      time = get_time()
                                      date = time['date']
                                      clock = time['clock']

                                      upload(user_id, com, amount, now_value, date, clock)
                                      
                                      ctx_text = '주식을 구매했어요.\n`- %s 코인`\n`+ %s %s 주`'%(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                                      return ctx_text

                              else:
                                  # try:
                                    amount = int(amount)
                                    if amount <= 0:
                                        ctx_text = '수량 부분에 자연수만 입력해주십시오.'
                                        return ctx_text
                                    else:
                                        com = find_company(company)
                                        kr_com = kr_company(com)


                                        if com == 'meta' or com == 'didim' or com == 'gonglyoug' or com == 'nuli' or com == 'hangil' or com == 'singom':
                                          conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                                          c = conn.cursor()
                                          c.execute('SELECT * FROM stock WHERE company=%s', (com,))
                                          d = c.fetchone()
                                          c.close()
                                          conn.close()
                                          now_value = d[1]
                                          now_value = int(now_value)


                                        elif com == 'samsung' or com == 'hyundai' or com == 'naver' or com == 'kolon' or com == 'korean' or com == 'kakao':
                                          conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                                          c = conn.cursor()
                                          c.execute('SELECT * FROM restock WHERE company=%s', (com,))
                                          d = c.fetchone()
                                          c.close()
                                          conn.close()
                                          now = d[1]
                                          now_value = now.replace(',','')
                                          now_value = int(now_value)
                                        

                                        if (amount * now_value) > money:
                                            ctx_text = '보유 금액이 부족합니다.'
                                            return ctx_text
                                            
                                        else:
                                            time = get_time()
                                            date = time['date']
                                            clock = time['clock']
                                            
                                            upload(user_id, com, amount, now_value, date, clock)

                                            ctx_text = '주식을 구매했어요.\n`- %s 코인`\n`+ %s %s 주`'%(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                                            return ctx_text
                                                
                                  # except:
                                  #     ctx_text = '수량 부분이 자연수가 아니거나 오류가 발생했습니다.\n```diff\n+++ 오류 발생 시 개발자에게 문의 바랍니다.```'
                                  #     return ctx_text
                                    
        elif order == '판매' or order == 'ㅍㅁ' or order == 'va' or order == '매도' or order == 'ㅁㄷ' or order == 'ae' or order == 'sell':
            conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
            c = conn.cursor()

            c = c.execute('SELECT id,nickname FROM "user"')
            user_s = c.fetchall()
            c.close()
            conn.close()
            user_keys = []

            for i in user_s:
                user_keys.append(i[0])

            if str(user_id) not in user_keys:
                ctx_text = "`$가입 (닉네임)`을 통해 시스템에 가입 후 이용바랍니다."
                return ctx_text
        
            else:
                if len(text) != 3:
                    ctx_text = '잘못된 명령어입니다.\n예시 : `$주식 판매 2 100`'
                    return ctx_text
                else:
                  # try:
                    number = int(text[1])
                    amount = text[2]

                    if amount == '다' or amount == 'ㄷ' or amount == 'all' or amount == 'e':
                      conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                      c = conn.cursor()
                      c.execute('SELECT * FROM "user" WHERE id=%s', (str(user_id), ))
                      data = c.fetchone()
                      c.close()
                      conn.close()

                      have_stock = data[4].split('&')
                      user_money = int(data[2])
                      numbers = []
                      for i in range(10):
                        j = have_stock[i]
                        if not j == '0':
                          numbers.append(i)
                      
                      if (number-1) not in numbers:
                        ctx_text = '입력하신 번호에 해당하는 주식을 보유하지 않고 있습니다. `$주식 나`를 통해 확인해주십시오.'
                        return ctx_text

                      else:
                        select_stock = have_stock[number-1]
                        select_stock = select_stock.replace('[','').replace(']','').split(',')
                        select_company = select_stock[0]

                        if "'" in select_company:
                          select_company = select_company.replace("'",'')
                        if ' ' in select_company:
                          select_company = select_company.replace(" ", "")

                        user_amount = select_stock[2]

                        if "'" in user_amount:
                          user_amount = user_amount.replace("'",'')
                        if " " in user_amount:
                          user_amount = user_amount.replace(" ", '')
                        
                        user_amount = int(user_amount)

                        if select_company == 'meta' or select_company == 'didim' or select_company == 'gonglyoug' or select_company == 'nuli' or select_company == 'hangil' or select_company == 'singom':
                          conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                          c = conn.cursor()
                          c.execute('SELECT * FROM stock WHERE company=%s', (select_company, ))

                          com_data = c.fetchone()
                          c.close()
                          conn.close()
                          now_value = int(com_data[1])

                          total = (user_amount * now_value) + user_money

                          
                          have_stock[number-1] = '0'
                          
                          
                          res = ''
                          for i in range(10):
                            j = have_stock[i]
                            if i == 9:
                              res = res + j
                            else:
                              res = res + j + '&'

                          conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                          c = conn.cursor()
                          c.execute('UPDATE "user" SET money=%s WHERE id=%s', (str(total), str(user_id)))
                          c.execute('UPDATE "user" SET stock=%s WHERE id=%s', (res, str(user_id)))
                          conn.commit()
                          c.close()
                          conn.close()

                          ctx_text = '주식을 판매했어요.\n`+ {} 코인`\n`- {} {}주`'.format(replace_amount(user_amount * now_value), kr_company(select_company), replace_amount(user_amount))
                          return ctx_text

                          
                          
                        elif select_company == 'samsung' or select_company == 'hyundai' or select_company == 'naver' or select_company == 'kolon' or select_company == 'korean' or select_company == 'kakao':
                          conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                          c = conn.cursor()
                          c.execute('SELECT * FROM restock WHERE company=%s', (select_company, ))
                          com_data = c.fetchone()
                          c.close()
                          conn.close()
                          now_value = int(com_data[1].replace(',',''))

                          total = (user_amount * now_value) + user_money

                          have_stock[number-1] = '0'

                          res = ''
                          for i in range(10):
                            j = have_stock[i]
                            if i == 9:
                              res = res + j
                            else:
                              res = res + j + '&'

                          conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                          c = conn.cursor()
                          c.execute('UPDATE "user" SET money=%s WHERE id=%s', (total, str(user_id)))
                          c.execute('UPDATE "user" SET stock=%s WHERE id=%s', (res, str(user_id)))
                          conn.commit()
                          c.close()
                          conn.close()

                          ctx_text = '주식을 판매했어요.\n`+ {} 코인`\n`- {} {}주`'.format(replace_amount(user_amount * now_value), kr_company(select_company), replace_amount(user_amount))
                          return ctx_text

                    else:
                        # try:
                          amount = int(amount)
                          if amount <= 0:
                              ctx_text = '수량 부분에 자연수만 입력해주십시오.'
                              return ctx_text
                          else:
                            conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                            c = conn.cursor()
                            c.execute('SELECT * FROM "user" WHERE id=%s', (str(user_id), ))
                            data = c.fetchone()
                            c.close()
                            conn.close()

                            have_stock = data[4].split('&')
                            user_money = int(data[2])
                            numbers = []
                            for i in range(10):
                              j = have_stock[i]
                              if not j == '0':
                                numbers.append(i)
                            
                            if (number-1) not in numbers:
                              ctx_text = '입력하신 번호에 해당하는 주식을 보유하지 않고 있습니다. `$주식 나`를 통해 확인해주십시오.'
                              return ctx_text 
                            
                            else:
                              select_stock = have_stock[number-1]
                              select_stock = select_stock.replace('[','').replace(']','').split(',')
                              select_company = select_stock[0].replace("'",'')
                              user_amount = int(select_stock[2].replace(" ",''))

                              if user_amount < amount:
                                ctx_text = '보유하신 개수보다 많이 입력하였습니다. `$주식 나`를 통해 확인해주십시오.'
                                return ctx_text
                              
                              else:
                                if select_company == 'meta' or select_company == 'didim' or select_company == 'gonglyoug' or select_company == 'nuli' or select_company == 'hangil' or select_company == 'singom':
                                  conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                                  c = conn.cursor()
                                  c = c.execute('SELECT * FROM stock WHERE company=%s', (select_company, ))
                                  com_data = c.fetchone()
                                  now_value = int(com_data[1])
                                  c.close()
                                  conn.close()

                                  total = (amount * now_value) + user_money
                                  
                                  if user_amount-amount == 0:
                                    have_stock[number-1] = '0'
                                  else:
                                    select_stock[2] = user_amount-amount
                                    have_stock[number-1] = str(select_stock)
                                  
                                  res = ''
                                  for i in range(10):
                                    j = have_stock[i]
                                    if i == 9:
                                      res = res + j
                                    else:
                                      res = res + j + '&'

                                  conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                                  c = conn.cursor()
                                  c.execute('UPDATE "user" SET money=%s WHERE id=%s', (str(total), str(user_id)))
                                  c.execute('UPDATE "user" SET stock=%s WHERE id=%s', (res, str(user_id)))
                                  conn.commit()
                                  c.close()
                                  conn.close()

                                  ctx_text = '주식을 판매했어요.\n`+ {} 코인`\n`- {} {}주`'.format(replace_amount(amount * now_value), kr_company(select_company), replace_amount(amount))
                                  return ctx_text
                                  
                                elif select_company == 'samsung' or select_company == 'hyundai' or select_company == 'naver' or select_company == 'kolon' or select_company == 'korean' or select_company == 'kakao':
                                  conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                                  c = conn.cursor()
                                  c.execute('SELECT * FROM restock WHERE company=%s', (select_company, ))
                                  com_data = c.fetchone()
                                  now_value = int(com_data[1].replace(',',''))
                                  c.close()
                                  conn.close()

                                  total = (amount * now_value) + user_money
                                  
                                  if user_amount-amount == 0:
                                    have_stock[number-1] = '0'
                                  else:
                                    select_stock[2] = user_amount-amount
                                    have_stock[number-1] = str(select_stock)

                                  res = ''
                                  for i in range(10):
                                    j = have_stock[i]
                                    if i == 9:
                                      res = res + j
                                    else:
                                      res = res + j + '&'

                                  conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                                  c = conn.cursor()
                                  c.execute('UPDATE "user" SET money=%s WHERE id=%s', (total, str(user_id)))
                                  c.execute('UPDATE "user" SET stock=%s WHERE id=%s', (res, str(user_id)))
                                  c.close()
                                  conn.close()

                                  ctx_text = '주식을 판매했어요.\n`+ {} 코인`\n`- {} {}주`'.format(replace_amount(amount * now_value), kr_company(select_company), replace_amount(amount))
                                  return ctx_text

                                
                  # except:
                  #   ctx_text = '`$주식 나`를 통해 팔고자 하는 주식의 번호를 확인해주십시오'
                  #   return ctx_text

                                # except:
                                #     ctx_text = '수량 부분이 자연수가 아니거나 오류가 발생했습니다.\n```diff\n+++ 오류 발생 시 개발자에게 문의 바랍니다.```'
                                #     return ctx_text

        elif order == '그래프' or order == 'ㄱㄿ' or order == 'ㄱㄹㅍ' or order == 'rfv' or order == 'graph':
            if len(text) > 2:
                ctx_text = '잘못된 명령어입니다.\n예시 : `$주식 그래프 펭귄증권`'
                return ctx_text
            else:
                if len(text) == 1:
                    ctx_text = '그래프를 보고 싶은 회사명을 입력해 주십시오.'
                    return ctx_text

                else:
                    company = text[1]
                    if type(company) != str:
                        ctx_text = '잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오'
                        return ctx_text
                    else:
                        com = find_company(company)
                        re_company = return_TF_company(com)
                        
                        if re_company == 'F':
                            ctx_text = '잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오'
                            return ctx_text
                        
                        else:
                          if com == 'meta' or com == 'didim' or com == 'gonglyoug' or com == 'nuli' or com == 'hangil' or com == 'singom':
                              save_graph(com)
                              
                              with open('%s.png'%com, 'rb') as f:
                                  picture = discord.File(f)
                                  ctx_text = [picture,'file']
                                  return ctx_text
                          else:
                            conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                            c = conn.cursor()
                            c = c.execute('SELECT * FROM restock WHERE company=%s', (com, ))
                            c = c.fetchone()
                            c.close()
                            conn.close()
                            com_name = kr_company(com)
                            link = c[9]
                            date = c[7]
                            clock  = c[8]
                            time = date + ' ' + clock
                            embed = discord.Embed(
                              title = '{} / {}'.format(com_name, time)
                            )
                            embed.set_image(url=link)

                            return embed

        elif len(text) == 1:
            nick = order
            conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
            c = conn.cursor()

            c.execute('SELECT * FROM "user"')
            nicks = []
            for i in c.fetchall():
                nickname = i[1]
                nicks.append(nickname)
            c.close()
            conn.close()

            if nick not in nicks:
              ctx_text = '입력하신 닉네임은 존재하지 않는 유저입니다.'
              return ctx_text

            else:
                conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                c = conn.cursor()

                c.execute('SELECT * FROM user WHERE nickname=?', (str(nick),))
                data = c.fetchone()
                c.close()
                conn.close()
                have_stock = data[4].split('&')
                nickname = data[1]

                send = '{} 님의 보유 주식 정보입니다.\n```scss\n'.format(nickname)

                for i in range(10):
                  j = have_stock[i]

                  if not j == '0':
                    com_stock = j.replace('[','').replace(']','').split(',')
                    company = com_stock[0]
                    if "'" in company:
                      company = company.replace("'",'')
                    kor_com = kr_company(company)

                    value = com_stock[1]
                    amount = com_stock[2]

                    if ' ' in value:
                      value = value.replace(' ', '')
                    if "'" in value:
                      value = value.replace("'",'')
                    if ' ' in amount:
                      amount = amount.replace(' ', '')
                    if "'" in amount:
                      amount = amount.replace("'",'')

                    diff = get_diff(company, value, amount) # -> str() / ex) diff = '+199조 1억 2993'
                    send = send + "#{} [{}] : '{}주'; //{} {}\n손익 → {} {}\n".format(i+1, kor_com, replace_amount(int(com_stock[2])), com_stock[3], com_stock[4], diff[0], diff[1:])

                send = send+'```'

                if send == '```scss\n```':
                  send = '보유하신 주식이 없습니다. `$주식`을 통해 주식 정보를 확인해보세요'
                  return send
                else:
                  return send

