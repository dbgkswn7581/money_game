import sqlite3
import discord
from replace import replace_amount


def print_money(ctx, text):
    user_id = ctx.author.id

    if len(text) == 0:
        conn = sqlite3.connect('user.db',isolation_level=None)
        c = conn.cursor()
        data = c.execute('SELECT * FROM user WHERE id=?',(str(user_id),))
        data = data.fetchone()

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
                    conn = sqlite3.connect('stock.db', isolation_level=None)
                    c = conn.cursor()
                    c.execute('SELECT * FROM stock WHERE company=?', (company, ))
                    d = c.fetchone()
                    value = d[1]
                    value = int(value)

                elif company == 'samsung' or company == 'hyundai' or company == 'naver' or company == 'kolon' or company == 'korean' or company == 'kakao':
                    conn = sqlite3.connect('restock.db', isolation_level=None)
                    c = conn.cursor()
                    c.execute('SELECT * FROM restock WHERE company=?', (company, ))
                    d = c.fetchone()
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
        
        conn = sqlite3.connect('user.db',isolation_level=None)
        c = conn.cursor()
        c = c.execute('SELECT id,nickname FROM user')
        user_s = c.fetchall()
        user_nicks = []

        for i in user_s:
            user_nicks.append(i[1])


        if nick not in user_nicks:
            ctx_text = '입력하신 닉네임은 존재하지 않는 유저입니다.'
            return ctx_text
            
        else:
            conn = sqlite3.connect('user.db',isolation_level=None)
            c = conn.cursor()
            c = c.execute('SELECT * FROM user WHERE nickname=?', (nick,))
            data = c.fetchone()

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
                        conn = sqlite3.connect('stock.db', isolation_level=None)
                        c = conn.cursor()
                        c.execute('SELECT * FROM stock WHERE company=?', (company, ))
                        d = c.fetchone()
                        value = d[1]
                        value = int(value)

                    elif company == 'samsung' or company == 'hyundai' or company == 'naver' or company == 'kolon' or company == 'korean' or company == 'kakao':
                        conn = sqlite3.connect('restock.db', isolation_level=None)
                        c = conn.cursor()
                        c.execute('SELECT * FROM restock WHERE company=?', (company, ))
                        d = c.fetchone()
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
