from firebase_admin import db
import discord
from replace import replace_amount


def print_money(ctx, text):
    if len(text) == 0:
        ref = db.reference()
        dic = ref.get()

        user_id = ctx.author.id

        money = dic[str(user_id)]['money']
        nick = dic[str(user_id)]['nickname']
        amount = dic[str(user_id)]['ce']['amount'] + dic[str(user_id)]['go']['amount'] + dic[str(user_id)]['mk']['amount'] + dic[str(user_id)]['nl']['amount'] + dic[str(user_id)]['pd']['amount'] + dic[str(user_id)]['sl']['amount'] + dic[str(user_id)]['sn']['amount'] + dic[str(user_id)]['tc']['amount'] + dic[str(user_id)]['ua']['amount'] + dic[str(user_id)]['pg']['amount']

        embed = discord.Embed(
        color = discord.Color.blue()
        )
        embed.add_field(name=":dollar: 보유 자금", value="**%s**" %replace_amount(money), inline=False)
        embed.add_field(name=":chart_with_upwards_trend: 총 보유 주", value="**%s**" %replace_amount(amount), inline=False)
        embed.set_footer(text='%s님의 정보' %nick)
        return embed

    elif len(text) == 1:
        nick = str(text[0])
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

        money = str()
        amount = str()

        user_ids = list(dic.keys())
        for i in user_ids:
            if nick == dic[str(i)]['nickname']:
                money = dic[str(i)]['money']
                amount = dic[str(i)]['ce']['amount'] + dic[str(i)]['go']['amount'] + dic[str(i)]['mk']['amount'] + dic[str(i)]['nl']['amount'] + dic[str(i)]['pd']['amount'] + dic[str(i)]['sl']['amount'] + dic[str(i)]['sn']['amount'] + dic[str(i)]['tc']['amount'] + dic[str(i)]['ua']['amount'] + dic[str(i)]['pg']['amount']

        if money == '' and amount == '':
            ctx_text = '입력하신 닉네임은 존재하지 않는 유저입니다.'
            return ctx_text
            
        else:
            embed = discord.Embed(
            color = discord.Color.blue()
            )
            embed.add_field(name=":dollar: 보유 자금", value="**%s**" %replace_amount(money), inline=False)
            embed.add_field(name=":chart_with_upwards_trend: 총 보유 주", value="**%s**" %replace_amount(amount), inline=False)
            embed.set_footer(text='%s님의 정보' %nick)
            return embed
