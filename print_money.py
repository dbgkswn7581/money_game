import psycopg2
import discord
from replace import replace_amount


def print_money(ctx, text):
    user_id = ctx.author.id

    if len(text) == 0:
        conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
        c = conn.cursor()
        c.execute('SELECT * FROM "user" WHERE id=%s',(str(user_id),))
        data = c.fetchone()

        c.close()
        conn.close()

        money = int(data[2])
        nick = data[1]
        stock = data[4]
        stock = stock.split('&')
        many = 0

        for i in range(10):
            j = stock[i]
            if not j == '0':
                it = j.replace('[','').replace(']','').split(',')
                company = it[0]
                company = company.replace("'",'')
                amount = int(it[2])

                if company == 'meta' or company == 'didim' or company == 'gonglyoug' or company == 'nuli' or company == 'hangil' or company == 'singom':
                    conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                    c = conn.cursor()
                    c.execute('SELECT * FROM stock WHERE company=%s', (company, ))
                    d = c.fetchone()

                    c.close()
                    conn.close()

                    value = d[1]
                    value = int(value)

                elif company == 'samsung' or company == 'hyundai' or company == 'naver' or company == 'kolon' or company == 'korean' or company == 'kakao':
                    conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                    c = conn.cursor()
                    c.execute('SELECT * FROM restock WHERE company=%s', (company, ))
                    d = c.fetchone()

                    c.close()
                    conn.close()

                    value = d[1]
                    value = int(value.replace(',',''))

                money = money + (value * amount)
                many = many + amount


        embed = discord.Embed(
        color = discord.Color.blue()
        )
        embed.add_field(name=":dollar: 총 자산", value="**%s**" %replace_amount(money), inline=False)
        embed.add_field(name=":chart_with_upwards_trend: 총 보유 주", value="**%s**" %replace_amount(many), inline=False)
        embed.set_footer(text='%s님의 정보' %nick)

        return embed

    elif len(text) == 1:
        nick = str(text[0])
        
        conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
        c = conn.cursor()
        c.execute('SELECT id,nickname FROM "user"')
        user_s = c.fetchall()

        c.close()
        conn.close()

        user_nicks = []

        for i in user_s:
            user_nicks.append(i[1])


        if nick not in user_nicks:
            ctx_text = '입력하신 닉네임은 존재하지 않는 유저입니다.'
            return ctx_text
            
        else:
            conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
            c = conn.cursor()
            c.execute('SELECT * FROM "user" WHERE nickname=%s', (nick,))
            data = c.fetchone()

            c.close()
            conn.close()

            money = int(data[2])
            nick = data[1]
            stock = data[4]
            stock = stock.split('&')
            many = 0

            for i in range(10):
                j = stock[i]
                if not j == '0':
                    it = j.replace('[','').replace(']','').split(',')
                    company = it[0]
                    company = company.replace("'",'')
                    
                    if company == 'meta' or company == 'didim' or company == 'gonglyoug' or company == 'nuli' or company == 'hangil' or company == 'singom':
                        conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                        c = conn.cursor()
                        c.execute('SELECT * FROM stock WHERE company=%s', (company, ))
                        d = c.fetchone()
                        c.close()
                        conn.close()
                        value = d[1]
                        value = int(value)

                    elif company == 'samsung' or company == 'hyundai' or company == 'naver' or company == 'kolon' or company == 'korean' or company == 'kakao':
                        conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
                        c = conn.cursor()
                        c.execute('SELECT * FROM restock WHERE company=%s', (company, ))
                        d = c.fetchone()
                        c.close()
                        conn.close()
                        value = d[1]
                        value = int(value.replace(',',''))

                    amount = int(it[2])
                    money = money + (value * amount)
                    many = many + amount


            embed = discord.Embed(
            color = discord.Color.blue()
            )
            embed.add_field(name=":dollar: 총 자산", value="**%s**" %replace_amount(money), inline=False)
            embed.add_field(name=":chart_with_upwards_trend: 총 보유 주", value="**%s**" %replace_amount(many), inline=False)
            embed.set_footer(text='%s님의 정보' %nick)
            return embed
