from firebase_admin import db
import discord
from replace import replace_amount

def rank(ctx, text):
    if len(text) == 0:
        ctx_text = '사용법 : `$순위 <자신/전체>`'
        return ctx_text
    elif len(text) == 1:
        user_id = ctx.author.id
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

        moneys = {}
        user_ids = list(dic.keys())
        user_nicks = []
        for i in user_ids:
            user_nicks.append(dic[str(i)]['nickname'])

        for i in user_ids:
            money = dic[str(i)]['money']
            moneys[str(i)] = money
        
        import operator

        rank = dict(sorted(moneys.items(), key=operator.itemgetter(1), reverse=True))
        moneys = list(rank.values())
        moneys.sort()
        moneys.reverse()

        if text[0] == '자신' or text[0] == '나' or text[0] == 'ㄴ' or text[0] == 'me' or text[0] == 'ㅈㅅ' or text[0] == 'wt':
            user_money = rank[str(user_id)]
            user_nickname = dic[str(user_id)]['nickname']

            embed = discord.Embed(
                title = '%s 님의 순위'%user_nickname,
                color = 0xf64f59
            )

            user_rank = moneys.index(user_money) + 1
            percent = (user_rank / len(moneys)) * 100

            embed.add_field(
                name=":trophy: **전체 순위**", value="**{}/{}** (상위 {}%)" .format(user_rank, len(moneys), percent), inline=True
                )

            embed.add_field(
                name=':dollar: **현재 보유 금액**', value='%s' %replace_amount(user_money), inline=False
            )

            return embed

        elif text[0] in user_nicks:
            user_id = user_ids[user_nicks.index(text[0])]
            user_money = rank[str(user_id)]
            user_nickname = dic[str(user_id)]['nickname']

            embed = discord.Embed(
                title = '%s 님의 순위'%user_nickname,
                color = 0xf64f59
            )

            user_rank = moneys.index(user_money) + 1
            percent = (user_rank / len(moneys)) * 100

            embed.add_field(
                name=":trophy: **전체 순위**", value="**{}/{}** (상위 {}%)" .format(user_rank, len(moneys), percent), inline=True
                )

            embed.add_field(
                name=':dollar: **현재 보유 금액**', value='%s' %replace_amount(user_money), inline=False
            )

            return embed

        elif text[0] == '전체' or text[0] == 'all' or text[0] == 'ㅈㅊ' or text[0] == 'wc':
            embed = discord.Embed(
                color = 0x654ea3
            )

            #rank -> dict() -> 유저의 보유 금액을 내림차순으로 정렬

            count_users = len(list(rank.keys()))
            replace_format = format(count_users, ',d')
            import math
            count_pages = math.ceil((count_users/10))
            value = str()

            if count_users < 10:
                for i in range(0, (count_users)):
                    user_id = list(rank.keys())[i]
                    user_money = list(rank.values())[i]
                    user_nickname = dic[str(user_id)]['nickname']

                    value = value + '**%d.** '%(i+1) + '%s '%(user_nickname) + '`%s`' %replace_amount(user_money) + '\n'

                embed.add_field(
                    name='글로벌 순위\n-------------' ,value=value, inline=False
                    )
                
                
                embed.set_footer(text='페이지 1/%d, 총 %s명' %(count_pages, replace_format))

                return embed
        
            else:
                for i in range(0, 10):
                    user_id = list(rank.keys())[i]
                    user_money = list(rank.values())[i]
                    user_nickname = dic[str(user_id)]['nickname']

                    value = value + '**%d.** '%(i+1) + '%s '%(user_nickname) + '`%s`' %replace_amount(user_money) + '\n'
                
                embed.add_field(
                    name='글로벌 순위\n-------------' ,value=value, inline=False
                    )
                
                
                embed.set_footer(text='페이지 1/%d, 총 %s명' %(count_pages, replace_format))

                return embed
        

    elif len(text) == 2:
        try:
            page = int(text[1])

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

            moneys = {}
            user_ids = list(dic.keys())

            for i in user_ids:
                money = dic[str(i)]['money']
                moneys[str(i)] = money
            
            import operator

            rank = dict(sorted(moneys.items(), key=operator.itemgetter(1), reverse=True))
            moneys = list(rank.values())
            moneys.sort()
            moneys.reverse()

            embed = discord.Embed(
                color = 0x654ea3
            )

            #rank -> dict() -> 유저의 보유 금액을 내림차순으로 정렬

            end_page = page*10 
            start_page = page*10 - 10

            count_users = len(list(rank.keys()))
            replace_format = format(count_users, ',d')
            import math
            count_pages = math.ceil((count_users/10))

            if page > count_pages:
                ctx_text = '존재하지 않는 페이지입니다.'
                return ctx_text
            
            else:
                value = str()
                
                if end_page > count_users:
                    end_page = count_users


                    for i in range(start_page, end_page):
                        user_id = list(rank.keys())[i]
                        user_money = list(rank.values())[i]
                        user_nickname = dic[str(user_id)]['nickname']

                        value = value + '**%d.** '%(i+1) + '%s '%(user_nickname) + '`%s`' %replace_amount(user_money) + '\n'
                    
                    embed.add_field(
                        name='글로벌 순위\n-------------' ,value=value, inline=False
                    )
                    
                    count_users = len(list(rank.keys()))
                    replace_format = format(count_users, ',d')
                    import math
                    count_pages = math.ceil((count_users/10))
                    embed.set_footer(text='페이지 %d/%d, 총 %s명' %(page, count_pages, replace_format))

                    return embed

                else:
                    for i in range(start_page, end_page):
                        user_id = list(rank.keys())[i]
                        user_money = list(rank.values())[i]
                        user_nickname = dic[str(user_id)]['nickname']

                        value = value + '**%d.** '%(i+1) + '%s '%(user_nickname) + '`%s`' %replace_amount(user_money) + '\n'
                    
                    embed.add_field(
                        name='글로벌 순위\n-------------' ,value=value, inline=False
                    )
                    
                    count_users = len(list(rank.keys()))
                    replace_format = format(count_users, ',d')
                    import math
                    count_pages = math.ceil((count_users/10))
                    embed.set_footer(text='페이지 %d/%d, 총 %s명' %(page, count_pages, replace_format))

                    return embed

        except:
            ctx_text = '페이지는 자연수만 입력할 수 있습니다.'
            return ctx_text