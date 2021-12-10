from firebase_admin import db
import discord
from replace import replace_amount
from gacha import gacha

def replace_box(step):
  if step == '1':
    return 1000
  elif step == '2':
    return 10000
  elif step == '3':
    return 100000
  elif step == '4':
    return 1000000
  elif step == '5':
    return 10000000
  elif step == '6':
    return 100000000
  elif step == '7':
    return 1000000000
  elif step == '8':
    return 10000000000


def draw(ctx,text):
    if len(text) == 0:
        ctx_text = '`$뽑기 상점` : 뽑기 상자 목록과 가격을 확인합니다.\n`$뽑기 나` : 본인의 상자 보유 여부를 확인합니다.\n`$뽑기 구매 (단계) (수량)` : 뽑기 상자를 (수량)만큼 구매합니다.\n`$뽑기 판매 (단계) (수량)` : 뽑기 상자를 (수량)만큼 판매합니다.\n`$뽑기 오픈 (단계) (수량)` : (수량)만큼 상자를 오픈합니다.\n`$뽑기 확률 (단계)` : 해당 단계의 상자의 확률과 당첨되는 보상을 확인합니다.\n\n```diff\n+ 3단계 상자인 경우 (단계)부분에 숫자 3만 입력하십시오.```'
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

        user_ids = list(dic.keys())
        user_nicks = []
        for i in user_ids:
            user_nicks.append(dic[str(i)]['nickname'])

        order = text[0]

        if order == '상점' or order == 'tw' or order == 'ㅅㅈ' or order == 'store' or order == 'shop':
            embed = discord.Embed(
                title = ':shopping_cart: 뽑기 상점',
                color = 0x009FFF
            )

            embed.add_field(
                name = ':coin: 1단계 상자 :coin:',
                value = '```diff\n+ 가격 : 1,000 코인\n+ 뽑기 시 0 ~ 10만 코인이 확률적으로 나옵니다.\n--- 확률 : $뽑기 확률 1단계 ---```',
                inline='False'
            )

            embed.add_field(
                name = ':dollar: 2단계 상자 :dollar:',
                value = '```diff\n+ 가격 : 1만 코인\n+ 뽑기 시 0 ~ 100만 코인 또는 1단계 상자 5 ~ 50 개가 확률적으로 나옵니다.\n--- 확률 : $뽑기 확률 2단계 ---```',
                inline='False'
            )

            embed.add_field(
                name = ':yen: 3단계 상자 :yen:',
                value = '```diff\n+ 가격 : 10만 코인\n+ 뽑기 시 0 ~ 1000만 코인 또는 2단계 상자 5 ~ 50 개가 확률적으로 나옵니다.\n--- 확률 : $뽑기 확률 3단계 ---```',
                inline='False'
            )

            embed.add_field(
                name = ':euro: 4단계 상자 :euro:',
                value = '```diff\n+ 가격 : 100만 코인\n+ 뽑기 시 0 ~ 1억 코인 또는 3단계 상자 5 ~ 50 개가 확률적으로 나옵니다.\n--- 확률 : $뽑기 확률 4단계 ---```',
                inline='False'
            )

            embed.add_field(
                name = ':pound: 5단계 상자 :pound:',
                value = '```diff\n+ 가격 : 1000만 코인\n+ 뽑기 시 0 ~ 10억 코인 또는 4단계 상자 5 ~ 50 개가 확률적으로 나옵니다.\n--- 확률 : $뽑기 확률 5단계 ---```',
                inline='False'
            )

            embed.add_field(
                name = ':moneybag: 6단계 상자 :moneybag:',
                value = '```diff\n+ 가격 : 1억 코인\n+ 뽑기 시 0 ~ 100억 코인 또는 5단계 상자 5 ~ 50 개가 확률적으로 나옵니다.\n--- 확률 : $뽑기 확률 6단계 ---```',
                inline='False'
            )

            embed.add_field(
                name = ':gem: 7단계 상자 :gem:',
                value = '```diff\n+ 가격 : 10억 코인\n+ 뽑기 시 0 ~ 1000억 코인 또는 6단계 상자 5 ~ 50 개가 확률적으로 나옵니다.\n--- 확률 : $뽑기 확률 7단계 ---```',
                inline='False'
            )

            embed.add_field(
                name = ':credit_card: 8단계 상자 :credit_card:',
                value = '```diff\n+ 가격 : 100억 코인\n+ 뽑기 시 0 ~ 1조 코인 또는 7단계 상자 5 ~ 50 개가 확률적으로 나옵니다.\n--- 확률 : $뽑기 확률 8단계 ---```',
                inline='False'
            )

            embed.set_footer(text = '뽑기 관련 명령어 : `$뽑기`')

            return embed
            

        elif order == '나' or order == 'ㄴ' or order == 's' or order == 'my' or order == 'me':
            user_id = ctx.author.id
            ref = db.reference()
            dic = ref.get()
            data = dic[str(user_id)]
            user_boxes = data['box']
            user_nickname = data['nickname']

            embed = discord.Embed(
                title = '%s님의 보유 상자' %(user_nickname),
                color = 0xef8e38
            )

            embed.add_field(
                name = ':coin: 1단계 상자 :coin:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[1]),
                inline = True
            )
            embed.add_field(
                name = ':dollar: 2단계 상자 :dollar:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[2]),
                inline = True
            )
            embed.add_field(
                name = ':yen: 3단계 상자 :yen:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[3]),
                inline = True
            )
            embed.add_field(
                name = ':euro: 4단계 상자 :euro:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[4]),
                inline = True
            )
            embed.add_field(
                name = ':pound: 5단계 상자 :pound:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[5]),
                inline = True
            )
            embed.add_field(
                name = ':moneybag: 6단계 상자 :moneybag:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[6]),
                inline = True
            )
            embed.add_field(
                name = ':gem: 7단계 상자 :gem:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[7]),
                inline = True
            )
            embed.add_field(
                name = ':credit_card: 8단계 상자 :credit_card:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[8]),
                inline = True
            )

            return embed
            
        
        elif text[0] in user_nicks:
            user_id = user_ids[user_nicks.index(text[0])]
            ref = db.reference()
            dic = ref.get()
            data = dic[str(user_id)]
            user_boxes = data['box']
            user_nickname = data['nickname']

            embed = discord.Embed(
                title = '%s님의 보유 상자' %(user_nickname),
                color = 0xef8e38
            )

            embed.add_field(
                name = ':coin: 1단계 상자 :coin:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[1]),
                inline = True
            )
            embed.add_field(
                name = ':dollar: 2단계 상자 :dollar:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[2]),
                inline = True
            )
            embed.add_field(
                name = ':yen: 3단계 상자 :yen:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[3]),
                inline = True
            )
            embed.add_field(
                name = ':euro: 4단계 상자 :euro:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[4]),
                inline = True
            )
            embed.add_field(
                name = ':pound: 5단계 상자 :pound:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[5]),
                inline = True
            )
            embed.add_field(
                name = ':moneybag: 6단계 상자 :moneybag:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[6]),
                inline = True
            )
            embed.add_field(
                name = ':gem: 7단계 상자 :gem:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[7]),
                inline = True
            )
            embed.add_field(
                name = ':credit_card: 8단계 상자 :credit_card:',
                value = '```md\n# %s 개```' %replace_amount(user_boxes[8]),
                inline = True
            )

            return embed
            

        else:
            ctx_text = '잘못된 명령어입니다.'
            return ctx_text

    elif len(text) == 2:
        order = text[0]
        step = text[1]
        if order == '확률' or order == 'ㅎㄹ' or order == 'gf':
            if step == '1' or step == '1단계' or step == '1er' or step == '1ㄷㄱ':
                re = 1
                result = {'0 코인' : 0, '500 코인' : 0, '2000 코인' : 0, '2200 코인' : 0, '2400 코인' : 0, '2600 코인' : 0, '2800 코인' : 0, '3000 코인' : 0, '10000 코인' : 0, '50000 코인' : 0, '100000 코인' : 0}
            elif step == '2' or step == '2단계' or step == '2er' or step == '2ㄷㄱ':
                re = 2
                result = {'0 코인' : 0, '5000 코인' : 0, '15000 코인' : 0, '20000 코인' : 0, '30000 코인' : 0, '100000 코인' : 0, '500000 코인' : 0, '1000000 코인' : 0, '5 상자' : 0, '10 상자' : 0, '25 상자' : 0, '50 상자' : 0}
            elif step == '3' or step == '3단계' or step == '3er' or step == '3ㄷㄱ':
                re = 3
                result = {'0 코인' : 0, '50000 코인' : 0, '150000 코인' : 0, '200000 코인' : 0, '300000 코인' : 0, '1000000 코인' : 0, '5000000 코인' : 0, '10000000 코인' : 0, '5 상자' : 0, '10 상자' : 0, '25 상자' : 0, '50 상자' : 0}
            elif step == '4' or step == '4단계' or step == '4er' or step == '4ㄷㄱ':
                re = 4
                result = {'0 코인' : 0, '500000 코인' : 0, '1500000 코인' : 0, '2000000 코인' : 0, '3000000 코인' : 0, '10000000 코인' : 0, '50000000 코인' : 0, '100000000 코인' : 0, '5 상자' : 0, '10 상자' : 0, '25 상자' : 0, '50 상자' : 0}
            elif step == '5' or step == '5단계' or step == '5er' or step == '5ㄷㄱ':
                re = 5
                result = {'0 코인' : 0, '5000000 코인' : 0, '15000000 코인' : 0, '20000000 코인' : 0, '30000000 코인' : 0, '100000000 코인' : 0, '500000000 코인' : 0, '1000000000 코인' : 0, '5 상자' : 0, '10 상자' : 0, '25 상자' : 0, '50 상자' : 0}
            elif step == '6' or step == '6단계' or step == '6er' or step == '6ㄷㄱ':
                re = 6
                result = {'0 코인' : 0, '50000000 코인' : 0, '150000000 코인' : 0, '200000000 코인' : 0, '300000000 코인' : 0, '1000000000 코인' : 0, '5000000000 코인' : 0, '10000000000 코인' : 0, '5 상자' : 0, '10 상자' : 0, '25 상자' : 0, '50 상자' : 0}
            elif step == '7' or step == '7단계' or step == '7er' or step == '7ㄷㄱ':
                re = 7
                result = {'0 코인' : 0, '500000000 코인' : 0, '1500000000 코인' : 0, '2000000000 코인' : 0, '3000000000 코인' : 0, '10000000000 코인' : 0, '50000000000 코인' : 0, '100000000000 코인' : 0, '5 상자' : 0, '10 상자' : 0, '25 상자' : 0, '50 상자' : 0}
            elif step == '8' or step == '8단계' or step == '8er' or step == '8ㄷㄱ':
                re = 8
                result = {'0 코인' : 0, '5000000000 코인' : 0, '15000000000 코인' : 0, '20000000000 코인' : 0, '30000000000 코인' : 0, '100000000000 코인' : 0, '500000000000 코인' : 0, '1000000000000 코인' : 0, '5 상자' : 0, '10 상자' : 0, '25 상자' : 0, '50 상자' : 0}

            result = list(result.keys())

            embed = discord.Embed(
                title = '%d단계 상자의 확률입니다.' %re,
                color = 0xFF007F
            )

            p_1 = [0.1,0.1877,0.14,0.14,0.14,0.14,0.14,0.01,0.002,0.0002,0.0001]
            p = [0.10,0.2716,0.30,0.30,0.01,0.002,0.0002,0.0001,0.01,0.005,0.001,0.0001]

            if re == 1:
                for i in result:
                    te = i.split(' ')
                
                embed.add_field(
                    name = '%s' %(replace_amount(te[0]) + ' ' +  te[1]), 
                    value = '```scss\n[%s]```' %(str(p_1[result.index(i)])+'%'),
                    inline = True
                )


            else:
                for i in result:
                    te = i.split(' ')

                embed.add_field(
                    name = '%s' %(replace_amount(te[0]) + ' ' +  te[1]), 
                    value = '```scss\n[%s]```' %(str((p[result.index(i)])*100)+'%'),
                    inline = True
                )
                embed.set_footer(text = '여기서 나오는 상자는 %d단계의 상자입니다.' %(re-1))
            
            return embed

    elif len(text) == 3:
        order = text[0]
        step = text[1]
        amount = text[2]

        if order == '구매' or order == 'ㄱㅁ' or order == 'ra' or order == 'buy':
            user_id = ctx.author.id
            ref = db.reference()
            dic = ref.get()
            data = dic[str(user_id)]
            user_money = data['money']
            user_boxes = data['box']

            try:
                if amount == '다' or amount == 'ㄷ' or amount == 'e' or amount == 'all':
                    if user_money < replace_box(step):
                        ctx_text = '보유 금액이 부족합니다.'
                        return ctx_text
                    else:
                        before = user_boxes[int(step)]
                        amount = int(user_money / replace_box(step))

                        ref.child(str(user_id)).child('box').child(step).set(before+int(amount))
                        ref.child(str(user_id)).child('money').set(user_money-(int(amount)*replace_box(step)))

                        ctx_text = '상자를 구매했어요.\n`+ %s 상자 : %s개`\n`- %s 코인`'%((step+'단계'),replace_amount(int(amount)),replace_amount(int(amount)*replace_box(step)))
                        return ctx_text

                elif amount == '반' or amount == 'ㅂ' or amount == 'q' or amount == '하프' or amount == 'ㅎㅍ' or amount == 'gv' or amount == 'half':
                    if int(user_money / 2) < replace_box(step):
                        ctx_text = '보유 금액이 부족합니다.'
                        return ctx_text
                    else:
                        before = user_boxes[int(step)]
                        amount = int(int(user_money/2) / replace_box(step))

                        ref.child(str(user_id)).child('box').child(step).set(before+int(amount))
                        ref.child(str(user_id)).child('money').set(user_money-(int(amount)*replace_box(step)))

                        ctx_text = '상자를 구매했어요.\n`+ %s 상자 : %s개`\n`- %s 코인`'%((step+'단계'),replace_amount(int(amount)),replace_amount(int(amount)*replace_box(step)))
                        return ctx_text

                else:
                    before = user_boxes[int(step)]

                    if int(amount)*replace_box(step) > user_money:
                        ctx_text = '보유 금액이 부족합니다.'
                        return ctx_text

                    else:
                        ref.child(str(user_id)).child('box').child(step).set(before+int(amount))
                        ref.child(str(user_id)).child('money').set(user_money-(int(amount)*replace_box(step)))

                        ctx_text = '상자를 구매했어요.\n`+ %s 상자 : %s개`\n`- %s 코인`'%((step+'단계'),replace_amount(int(amount)),replace_amount(int(amount)*replace_box(step)))
                        return ctx_text
            except:
                ctx_text = '잘못된 명령어입니다. 예시 : `$뽑기 구매 5 10`'
                return ctx_text
        
        elif order == '판매' or order == 'ㅍㅁ' or order == 'va' or order == 'sell':
            user_id = ctx.author.id
            ref = db.reference()
            dic = ref.get()
            data = dic[str(user_id)]
            user_money = data['money']
            user_boxes = data['box']

            try:
                before = user_boxes[int(step)]

                if amount == '다' or amount == 'ㄷ' or amount == 'e' or amount == 'all':
                    if before == 0:
                        ctx_text = '판매할 상자가 없습니다.'
                        return ctx_text
                    else:
                        ref.child(str(user_id)).child('box').child(step).set(0)
                        ref.child(str(user_id)).child('money').set(user_money+(int(before)*replace_box(step)))

                        ctx_text = '상자를 판매했어요.\n`- %s 상자 : %s개`\n`+ %s 코인`'%((step+'단계'),replace_amount(int(before)),replace_amount(int(before)*replace_box(step)))
                        return ctx_text

                elif amount == '반' or amount == 'ㅂ' or amount == 'q' or amount == '하프' or amount == 'ㅎㅍ' or amount == 'gv' or amount == 'half':
                    if before < 2:
                        ctx_text = '보유한 상자가 2개 이상일 때 `하프` 명령어를 사용할 수 있습니다.'
                        return ctx_text
                    else:
                        ref.child(str(user_id)).child('box').child(step).set(int(before/2)+1)
                        ref.child(str(user_id)).child('money').set(user_money+(int(before/2)*replace_box(step)))

                        ctx_text = '상자를 판매했어요.\n`- %s 상자 : %s개`\n`+ %s 코인`'%((step+'단계'),replace_amount(int(before/2)+1),replace_amount(int(before/2)*replace_box(step)))
                        return ctx_text

                else:
                    before = user_boxes[int(step)]

                    if before < int(amount):
                        ctx_text = '보유 상자 개수가 부족합니다.'
                        return ctx_text
                    else:
                        ref.child(str(user_id)).child('box').child(step).set(before-int(amount))
                        ref.child(str(user_id)).child('money').set(user_money+(int(amount)*replace_box(step)))

                        ctx_text = '상자를 판매했어요.\n`- %s 상자 : %d개`\n`+ %s 코인`'%((step+'단계'),int(amount),replace_amount(int(amount)*replace_box(step)))
                        return ctx_text


            except:
                ctx_text = '잘못된 명령어입니다. 예시 : `$뽑기 판매 5 10`'
                return ctx_text

        elif order == '오픈' or order == 'ㅇㅍ' or order == 'dv' or order == 'open':
            user_id = ctx.author.id
            ref = db.reference()
            dic = ref.get()
            data = dic[str(user_id)]
            user_money = data['money']
            user_boxes = data['box']
            user_nickname = data['nickname']

        try:
            before = user_boxes[int(step)]

            if before < int(amount):
                ctx_text = '보유 상자 개수가 부족합니다.'
                return ctx_text
            else:
                if int(amount) > 10000:
                    ctx_text = '한 번에 1만 개를 초과하여 상자를 열 수 없습니다.'
                    return ctx_text
                else:
                    result = gacha(int(step), int(amount))
                    keys = list(result.keys())
                    values = list(result.values())
                    
                    if int(step) == 1:
                        emoji = ':coin:'
                    elif int(step) == 2:
                        emoji = ':dollar:'
                    elif int(step) == 3:
                        emoji = ':yen:'
                    elif int(step) == 4:
                        emoji = ':euro:'
                    elif int(step) == 5:
                        emoji = ':pound:'
                    elif int(step) == 6:
                        emoji = ':moneybag:'
                    elif int(step) == 7:
                        emoji = ':gem:'
                    elif int(step) == 8:
                        emoji = ':credit_card:'

                    embed = discord.Embed(
                        title = '%s %d단계 상자 %s \n%d개 오픈 결과 (%s 님의 뽑기)' %(emoji, int(step), emoji, int(amount), user_nickname),
                        color = 0xE8CBC0
                        )

                    re_money = 0
                    re_box = 0

                    if int(step) == 1:
                        for i in range(0,11):
                            slid = keys[i].split(' ')
                            re_money += (int(slid[0]) * int(values[i]))
                            slid[0] = replace_amount(int(slid[0]))

                            embed.add_field(
                            name = '**%s**' %(slid[0]+' '+slid[1]),
                            value = '```md\n[%d][번]```'%values[i],
                            inline = True
                            )
                        
                        embed.set_footer(text='총 %s 코인 획득' %replace_amount(re_money))
                        ref.child(str(user_id)).child('box').child(str(step)).set(before-int(amount))
                        ref.child(str(user_id)).child('money').set(user_money+re_money)
                    

                    else:
                        for i in range(0,12):
                            slid = keys[i].split(' ')
                            if i >= 0 and i <= 7:
                                re_money += (int(slid[0]) * int(values[i]))
                            else:
                                re_box += (int(slid[0]) * int(values[i]))

                            slid[0] = replace_amount(int(slid[0]))
                            
                            embed.add_field(
                            name = '**%s**' %(slid[0]+' '+slid[1]),
                            value = '```md\n[%d][번]```'%values[i],
                            inline = True
                            )
                        embed.set_footer(text='총 %s 코인과 %d단계 상자 %d개 획득' %(replace_amount(re_money), (int(step)-1), re_box))
                        ref.child(str(user_id)).child('box').child(str(step)).set(before-int(amount))
                        ref.child(str(user_id)).child('money').set(user_money+re_money)

                        before = user_boxes[int(step)-1]
                        ref.child(str(user_id)).child('box').child(str(int(step)-1)).set(before+re_box)
                        
                        return embed

        except:
            ctx_text = '잘못된 명령어입니다. 예시 : `$뽑기 오픈 5 10`'
            return ctx_text