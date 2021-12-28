from firebase_admin import db
import discord
from replace import replace_amount
from gacha import gacha, get_gacha_list

def draw(ctx,text):
    if len(text) == 0:
        ctx_text = '`$뽑기 나` : 본인의 뽑기 정보를 확인합니다..\n`$뽑기 오픈 (금액) (개수)` : (금액)만큼의 뽑기 상자를 (개수)만큼 오픈합니다.\n`$뽑기 확률` : 뽑기 상자의 확률과 당첨되는 보상을 확인합니다.\n\n```diff\n+ 상자를 3개 열고자 할 경우 (개수)부분에 숫자 3만 입력하십시오.```'
        return ctx_text
        
    elif len(text) == 1:
        ref = db.reference()
        dic = ref.get()
        del dic['pg']
        del dic['sn']
        del dic['mk']
        del dic['ua']
        del dic['nl']
        del dic['pd']
        del dic['go']
        del dic['tc']
        del dic['sl']
        del dic['ce']
        del dic['admin']
        del dic['samsung']
        del dic['kakao']
        del dic['naver']
        del dic['korean']
        del dic['kolon']
        del dic['hyundai']

        user_ids = list(dic.keys())
        user_nicks = []
        for i in user_ids:
            user_nicks.append(dic[str(i)]['nickname'])

        order = text[0]


        if order == '나' or order == 'ㄴ' or order == 's' or order == 'my' or order == 'me':
            user_id = ctx.author.id
            ref = db.reference()
            dic = ref.get()
            data = dic[str(user_id)]
            user_boxes = data['box']
            user_get = user_boxes['get']
            user_lost = user_boxes['lost']
            user_time = user_boxes['time']
            user_nickname = data['nickname']

            embed = discord.Embed(
                title = '%s님의 뽑기 정보' %(user_nickname),
                color = 0xef8e38
            )

            
            embed.add_field(
                name = '오픈한 상자 개수',
                value = '```md\n# %s 개```' %replace_amount(user_time),
                inline = True
            )

            embed.add_field(
                name = '뽑기에 사용한 코인',
                value = '```md\n# %s 코인```' %replace_amount(user_lost),
                inline = True
            )
            
            embed.add_field(
                name = '뽑기로 얻은 코인',
                value = '```md\n# %s 코인```' %replace_amount(user_get),
                inline = True
            )

            return embed
            
        if order == '확률' or order == 'ㅎㄹ' or order == 'gf':
            gacha_list = ['0배', '2배', '4배', '10배', '50배', '100배']

            embed = discord.Embed(
                title = '확률표',
                color = 0xFF007F
            )

            p = [0.7794,0.175, 0.04, 0.005,  0.0005, 0.0001]

            for i in gacha_list:
                per = '%.2f'%(p[gacha_list.index(i)]*100)
                per = per + '%'
                embed.add_field(
                    name = '%s' %(i), 
                    value = '```scss\n[%s]```' %(per),
                    inline = True
                )            
            return embed
        

        else:
            ctx_text = '잘못된 명령어입니다.'
            return ctx_text

    elif len(text) == 3:
        order = text[0]
        worth = text[1]
        amount = text[2]
    
        if order == '오픈' or order == 'ㅇㅍ' or order == 'dv' or order == 'open' or order == '열기' or order == '구매' or order == 'ㄱㅁ' or order == 'ra' or order == 'buy' or order == 'ㅇㄱ' or order == 'dr':
            user_id = ctx.author.id
            ref = db.reference()
            dic = ref.get()
            data = dic[str(user_id)]
            user_money = data['money']
            user_boxes = data['box']
            user_nickname = data['nickname']
            user_get = user_boxes['get'] #뽑기로 번 돈
            user_time = user_boxes['time'] #구매한 뽑기 상자 개수
            user_lost = user_boxes['lost'] #뽑기에 사용한 돈

            # try:
            if int(amount) > 10000:
                ctx_text = '한 번에 1만 개를 초과하여 상자를 열 수 없습니다.'
                return ctx_text

            else:
                result = gacha(int(amount))
                gacha_list = get_gacha_list(worth)
                emoji = ':moneybag:'


                embed = discord.Embed(
                    title = '%s %s 코인 상자 %s \n%d개 오픈 결과 (%s 님의 뽑기)' %(emoji, replace_amount(int(worth)), emoji, int(amount), user_nickname),
                    color = 0xE8CBC0
                    )

                re_money = 0

                for i in range(0,6):
                    earn = result[i] * gacha_list[i]
                    re_money += earn
                    
                    embed.add_field(
                        name = '**%s**' %(replace_amount(gacha_list[i]) + ' 코인'),
                        value = '```md\n[%d][번]```'%result[i],
                        inline = True
                        )

                embed.set_footer(text='총 %s 코인 획득' %(replace_amount(re_money)))
                ref.child(str(user_id)).child('money').set(user_money-int(int(worth)*int(amount)))
                ref = db.reference()
                data = ref.child(str(user_id)).get()
                user_money = data['money']
                ref.child(str(user_id)).child('box').child('get').set(user_get+re_money)
                ref.child(str(user_id)).child('box').child('time').set(user_time+int(amount))
                ref.child(str(user_id)).child('box').child('lost').set(user_lost+int(int(worth)*int(amount)))
                ref.child(str(user_id)).child('money').set(user_money+re_money)

                return embed

            # except:
            #     ctx_text = '잘못된 명령어입니다. 예시 : `$뽑기 오픈 20000 3`'
            #     return ctx_text
        else:
            ctx_text = '잘못된 명령어입니다. `$뽑기`를 통해 명령어를 확인하십시오.'
            return ctx_text
