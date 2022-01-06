import requests
from bs4 import BeautifulSoup

def kospi():
    url = 'https://finance.naver.com/sise/sise_index.naver?code=KOSPI'
    res = requests.get(url)

    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    info = soup.select_one('#time')
    info = str(info)
    info = info.replace('<span id="time">','')
    info = info.replace('</span>','')

    return info

def real_stock():
    item_code = ['005930','005380','035420','120115','003490','035720'] #삼성전자, 현대차, 네이버, 코오롱인더우, 대한항공 순서
    now_prices = []
    yesterday_prices = []
    yesterday_percents = []
    sum_pirces = []
    foreigners = []
    transes = []
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

        graph = str(soup.select_one('#img_chart_area'))[145:232]

        now_prices.append(now_price)
        yesterday_prices.append(yesterday_price)
        yesterday_percents.append(yesterday_percent)
        sum_pirces.append(sum_pirce)
        foreigners.append(foreigner)
        transes.append(trans)
        graphs.append(graph)

    result = [now_prices, yesterday_prices, yesterday_percents, sum_pirces, foreigners, transes, graphs]

    return result
    
