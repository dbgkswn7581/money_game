import discord
import psycopg2

def reg(ctx, text):
    user_keys = []
    txt = text[0]
    nickname = txt
    user_id = ctx.author.id
    
    conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
    c = conn.cursor()
    
    c.execute('SELECT id,nickname FROM "user"')
    user_s = c.fetchall()
    user_keys = []
    for i in user_s:
        user_keys.append(i[0])

    if str(user_id) in user_keys:
        c.execute('SELECT * FROM "user" WHERE id=%s', (str(user_id),))
        data = c.fetchone()
        c.close()
        conn.close()
        nick = data[1]
        money = data[2]
        embed = discord.Embed(title ="회원가입 실패",
        description = 'Money Game', color = discord.Color.red()
        )
        embed.add_field(name = '이미 가입된 유저입니다.', value='가입된 닉네임 : %s\n보유 자금 : %s' %(str(nick), str(money)), inline=False)

        return embed
    
    elif str(user_id) not in user_keys:

        nicks = []

        for i in user_s:
            nicks.append(i[1])
        
        if nickname in nicks:
            c.close()
            conn.close()
            embed = discord.Embed(title ="회원가입 실패",
            description = 'Money Game', color = discord.Color.red()
            )
            embed.add_field(name = '중복된 닉네임입니다.', value='다른 닉네임으로 다시 시도해주십시오.', inline=False)
        else:
            c.execute('INSERT INTO "user"(id, nickname, money, choose, stock) \
            VALUES(%s, %s, %s, %s, %s)', \
                (str(user_id), txt, 1000000, 1,'0&0&0&0&0&0&0&0&0&0'))
            
            conn.commit()
            c.close()
            conn.close()

            embed = discord.Embed(title = "%s님 반갑습니다!" %txt,
            description = "Money Game", color = discord.Color.green()
            )
            embed.add_field(name='보유 자금', value='1,000,000', inline=True)
            embed.add_field(name="`$도움말`을 통해 사용 가능한 명령어를 확인해보세요" , value='접두사 : `$`', inline=True)

        
        

        return embed

def unreg(ctx):
    user_keys = []
    user_id = ctx.author.id

    conn = psycopg2.connect(host='ec2-3-209-234-80.compute-1.amazonaws.com',dbname='d8sv37cbum5a7k',user='kyshvxsusgztbc',password='938df8636f301f7656f277c4e2684ff5fbaba1fa68822cd73785e33c7bea62f2',port=5432)
    c = conn.cursor()

    c.execute('SELECT id,nickname FROM "user"')
    user_s = c.fetchall()
    user_keys = []
    for i in user_s:
        user_keys.append(i[0])

    if str(user_id) in user_keys:
        c.execute('SELECT * FROM "user" WHERE id=%s', (str(user_id),))
        data = c.fetchone()
        nick = data[1]
        money = data[2]

        c.execute('DELETE FROM "user" WHERE id=%s', (str(user_id),))
        conn.commit()
        c.close()
        conn.close()


        embed = discord.Embed(title ="Money Game 탈퇴",
        description = 'Money Game', color = discord.Color.dark_green()
        )
        embed.add_field(name = '성공적으로 탈퇴되었습니다.', value='가입된 닉네임 : %s\n보유 자금 : %s' %(str(nick), str(money)), inline=False)

        return embed
    
    elif str(user_id) not in user_keys:
        c.close()
        conn.close()
        embed = discord.Embed(title ="Money Game 탈퇴",
        description = 'Money Game', color = discord.Color.red()
        )
        embed.add_field(name = '가입하지 않은 계정입니다.', value='`$가입 (닉네임)`\n으로 가입을 진행해주십시오.', inline=False)


        return embed
