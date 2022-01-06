import requests
from bs4 import BeautifulSoup
from get_time import get_time
import psycopg2


def restock():
    item_code = ['005930','005380','035420','120115','003490','035720'] #삼성전자, 현대차, 네이버, 코오롱인더우, 대한항공, 카카오 순서
    company = ['samsung', 'hyundai', 'naver', 'kolon', 'korean', 'kakao']

    now_prices = []
    yesterday_prices = []
    yesterday_percents = []
    sum_pirces = []
    foreigners = []
    transes = []
    times = []
    graphs = []

    for i in item_code:
        url = 'https://finance.naver.com/item/main.naver?code=' + i
        res = requests.get(url)

        html = res.text
        soup = BeautifulSoup(html, 'html.parser')

        price_info = soup.select_one('#middle > dl > dd:nth-child(5)')
        price_info = str(price_info).split(' ')
        
        now_price = price_info[1] #현재가
        if price_info[3] == '상승': 
            yesterday_price = '+' + str(price_info[4]) #전일비
            yesterday_percent = '+' + str(price_info[6]) #등락률
        elif price_info[3] == '하락':
            yesterday_price = '-' + str(price_info[4]) #전일비
            yesterday_percent = '-' + str(price_info[6]) #등락률
        elif price_info[3] == '보합':
            yesterday_price = '+' + str(price_info[4]) #전일비
            yesterday_percent = '+' + str(price_info[6]) #등락률

        sum_pirce = str(soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(4) > td:nth-child(2)')) #시가총액
        sum_pirce = sum_pirce.replace('<td>','')
        sum_pirce = sum_pirce.replace('</td>','')

        foreigner = str(soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(5) > td:nth-child(2)')) #외국인비율
        foreigner = foreigner.replace('<td>','')
        foreigner = foreigner.replace('</td>','')

        trans = (str(soup.select_one('#middle > dl > dd:nth-child(12)')).split(' '))[1] #거래량
        trans = trans.replace('<dd>','')
        trans = trans.replace('</dd>','')


        time = str(soup.select_one('#time > em'))
        time = time.replace('<em class="date">','')
        time = time[:17]
        times.append(time)

        graph = str(soup.select_one('#img_chart_area'))[145:232]

        now_prices.append(now_price)
        yesterday_prices.append(yesterday_price)
        yesterday_percents.append(yesterday_percent)
        sum_pirces.append(sum_pirce)
        foreigners.append(foreigner)
        transes.append(trans)
        graphs.append(graph)

    conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
    c = conn.cursor()

    time = get_time()

    for i in company:
        c.execute('UPDATE restock SET value=%s WHERE company=%s', (now_prices[company.index(i)], i))
        c.execute('UPDATE restock SET yes_price=%s WHERE company=%s', (yesterday_prices[company.index(i)], i))
        c.execute('UPDATE restock SET yes_percent=%s WHERE company=%s', (yesterday_percents[company.index(i)], i))
        c.execute('UPDATE restock SET sum_price=%s WHERE company=%s', (sum_pirces[company.index(i)], i))
        c.execute('UPDATE restock SET foreigner=%s WHERE company=%s', (foreigners[company.index(i)], i))
        c.execute('UPDATE restock SET trans=%s WHERE company=%s', (transes[company.index(i)], i))
        c.execute('UPDATE restock SET date=%s WHERE company=%s', (time['date'], i))
        c.execute('UPDATE restock SET clock=%s WHERE company=%s', (time['clock'], i))
        c.execute('UPDATE restock SET graph=%s WHERE company=%s', (graphs[company.index(i)], i))

        # c.execute('INSERT INTO restock VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (i, now_prices[company.index(i)], yesterday_prices[company.index(i)], yesterday_percents[company.index(i)],sum_pirces[company.index(i)], foreigners[company.index(i)], transes[company.index(i)], time['date'], time['clock'], graphs[company.index(i)]))

    conn.commit()
    c.close()
    conn.close()
    
