from firebase_admin import db
import discord

def reg(ctx, text):
    user_keys = []
    txt = text[0]
    nickname = txt
    user_id = ctx.author.id
    
    ref = db.reference()
    dic = ref.get()
    del dic['ce']
    del dic['go']
    del dic['mk']
    del dic['nl']
    del dic['pd']
    del dic['pg']
    del dic['sl']
    del dic['sn']
    del dic['tc']
    del dic['ua']
    
    for key in dic.keys():
        user_keys.append(key)

    if str(user_id) in user_keys:
        ref = db.reference()
        data = ref.child(str(user_id)).get()
        nick = data['nickname']
        money = data['money']
        embed = discord.Embed(title ="회원가입 실패",
        description = 'Money Game', color = discord.Color.red()
        )
        embed.add_field(name = '이미 가입된 유저입니다.', value='가입된 닉네임 : %s\n보유 자금 : %s' %(str(nick), str(money)), inline=False)

        return embed
    
    elif str(user_id) not in user_keys:
        ref= db.reference()
        dic = ref.get()
        del dic['ce']
        del dic['go']
        del dic['mk']
        del dic['nl']
        del dic['pd']
        del dic['pg']
        del dic['sl']
        del dic['sn']
        del dic['tc']
        del dic['ua']
        nicks = []

        for i in user_keys:
            nicks.append(dic[str(i)]['nickname'])
        
        if nickname in nicks:
            embed = discord.Embed(title ="회원가입 실패",
            description = 'Money Game', color = discord.Color.red()
            )
            embed.add_field(name = '중복된 닉네임입니다.', value='다른 닉네임으로 다시 시도해주십시오.', inline=False)
        else:
            embed = discord.Embed(title = "%s님 반갑습니다!" %txt,
            description = "Money Game", color = discord.Color.green()
            )
            embed.add_field(name='보유 자금', value='5000', inline=True)
            embed.add_field(name="`$도움말`을 통해 사용 가능한 명령어를 확인해보세요" , value='접두사 : `$`', inline=True)
            # embed.set_thumbnail(url="https://cravatar.eu/helmhead/%s/68.png" %txt)

        ref = db.reference()
        ref.update({'%s'%user_id:{
            'nickname':nickname, 
            'money':5000, 
            'box':{'get' : 0, 'time' : 0, 'lost' : 0},
            'pg':{'amount' : 0, 'value' : 0}, 
            'sn':{'amount' : 0, 'value' : 0},
            'mk':{'amount' : 0, 'value' : 0},
            'ua':{'amount' : 0, 'value' : 0},
            'nl':{'amount' : 0, 'value' : 0},
            'pd':{'amount' : 0, 'value' : 0},
            'go':{'amount' : 0, 'value' : 0},
            'tc':{'amount' : 0, 'value' : 0},
            'sl':{'amount' : 0, 'value' : 0},
            'ce':{'amount' : 0, 'value' : 0}}})
        
        return embed

def unreg(ctx):
    user_keys = []
    user_id = ctx.author.id

    ref = db.reference()
    dic = ref.get()
    del dic['ce']
    del dic['go']
    del dic['mk']
    del dic['nl']
    del dic['pd']
    del dic['pg']
    del dic['sl']
    del dic['sn']
    del dic['tc']
    del dic['ua']

    for key in dic.keys():
        user_keys.append(key)

    if str(user_id) in user_keys:
        ref = db.reference()
        data = ref.child(str(user_id)).get()
        nick = data['nickname']
        money = data['money']

        ref = db.reference()
        ref.child(str(user_id)).delete()

        embed = discord.Embed(title ="Money Game 탈퇴",
        description = 'Money Game', color = discord.Color.dark_green()
        )
        embed.add_field(name = '성공적으로 탈퇴되었습니다.', value='가입된 닉네임 : %s\n보유 자금 : %s' %(str(nick), str(money)), inline=False)

        return embed
    
    elif str(user_id) not in user_keys:
        embed = discord.Embed(title ="Money Game 탈퇴",
        description = 'Money Game', color = discord.Color.red()
        )
        embed.add_field(name = '가입하지 않은 계정입니다.', value='`$가입 (닉네임)`\n으로 가입을 진행해주십시오.', inline=False)


        return embed
