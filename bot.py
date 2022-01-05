#-*- coding:utf-8 -*-

import os
import discord
from discord.colour import Color
from discord.ext import commands, tasks
from datetime import datetime
import time
from discord.ext.commands import bot

client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    game = discord.Game("Money Game")
    await client.change_presence(status = discord.Status.online, activity = game)


@client.command(name="가입")
async def signup(ctx, *text):
  from reg import reg
  embed = reg(ctx, text)
  await ctx.send(embed=embed)

@client.command(name="rd")
async def signup(ctx, *text):
  from reg import reg

  embed = reg(ctx, text)

  await ctx.send(embed=embed)

@client.command(name="ㄱㅇ")
async def signup(ctx, *text):
  from reg import reg

  embed = reg(ctx, text)

  await ctx.send(embed=embed)

##############################################################################################

@client.command(name="탈퇴")
async def signout(ctx):
  from reg import unreg
  embed = unreg(ctx)
  await ctx.send(embed=embed)

@client.command(name="xx")
async def signout(ctx):
  from reg import unreg
  embed = unreg(ctx)
  await ctx.send(embed=embed)

@client.command(name="ㅌㅌ")
async def signout(ctx):
  from reg import unreg
  embed = unreg(ctx)
  await ctx.send(embed=embed)



##############################################################################################################################
@client.command(name="주식")
async def reg(ctx, *text):
  from stock import stock
  ctx_text = stock(ctx, text)
  if type(ctx_text) == list:
    await ctx.send(file=ctx_text[0])
    

  elif type(ctx_text) == str:
    await ctx.send(ctx_text)

  elif type(ctx_text) == dict:
    await ctx.send(embed = ctx_text['one'])
    await ctx.send(embed = ctx_text['two'])
  else:
    await ctx.send(embed=ctx_text)

@client.command(name="wt")
async def reg(ctx, *text):
  from stock import stock
  ctx_text = stock(ctx, text)
  if type(ctx_text) == list:
    await ctx.send(file=ctx_text[0])

  elif type(ctx_text) == str:
    await ctx.send(ctx_text)

  elif type(ctx_text) == dict:
    await ctx.send(embed = ctx_text['one'])
    await ctx.send(embed = ctx_text['two'])
  else:
    await ctx.send(embed=ctx_text)

@client.command(name="ㅈㅅ")
async def reg(ctx, *text):
  from stock import stock
  ctx_text = stock(ctx, text)
  if type(ctx_text) == list:
    await ctx.send(file=ctx_text[0])

  elif type(ctx_text) == str:
    await ctx.send(ctx_text)

  elif type(ctx_text) == dict:
    await ctx.send(embed = ctx_text['one'])
    await ctx.send(embed = ctx_text['two'])
  else:
    await ctx.send(embed=ctx_text)



################################################################################################################################################

@client.command(name='도움말')
async def help(ctx):
  await ctx.send('`$가입 (닉네임)`  : 시스템에 가입합니다.\n`$탈퇴` : 시스템에서 탈퇴합니다.\n\n`$주식` : 현재 주식 현황을 확인합니다.\n`$주식 구매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 구매합니다.\n`$주식 판매 (번호) (수량)` : 해당 번호의 주식을 수량만큼 판매합니다.\n`$주식 나` : 현재 본인이 보유중인 주식을 확인할 수 있습니다.\n`$주식 그래프 (회사명)` : 해당 회사의 주식 변동 그래프를 확인할 수 있습니다.\n\n`$돈` : 본인 정보를 확인할 수 있습니다.\n`$순위` : 순위 관련 명령어를 확인할 수 있습니다.\n`$설정` : 설정 관련 명령어를 확인할 수 있습니다.\n```diff\n+ 위 명령어는 자음 또는 영어로 입력할 수 있습니다.```')

@client.command(name='명령어')
async def help(ctx):
  await ctx.send('`$가입 (닉네임)`  : 시스템에 가입합니다.\n`$탈퇴` : 시스템에서 탈퇴합니다.\n\n`$주식` : 현재 주식 현황을 확인합니다.\n`$주식 구매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 구매합니다.\n`$주식 판매 (번호) (수량)` : 해당 번호의 주식을 수량만큼 판매합니다.\n`$주식 나` : 현재 본인이 보유중인 주식을 확인할 수 있습니다.\n`$주식 그래프 (회사명)` : 해당 회사의 주식 변동 그래프를 확인할 수 있습니다.\n\n`$돈` : 본인 정보를 확인할 수 있습니다.\n`$순위` : 순위 관련 명령어를 확인할 수 있습니다.\n`$설정` : 설정 관련 명령어를 확인할 수 있습니다.\n```diff\n+ 위 명령어는 자음 또는 영어로 입력할 수 있습니다.```')

@client.command(name='?')
async def help(ctx):
  await ctx.send('`$가입 (닉네임)`  : 시스템에 가입합니다.\n`$탈퇴` : 시스템에서 탈퇴합니다.\n\n`$주식` : 현재 주식 현황을 확인합니다.\n`$주식 구매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 구매합니다.\n`$주식 판매 (번호) (수량)` : 해당 번호의 주식을 수량만큼 판매합니다.\n`$주식 나` : 현재 본인이 보유중인 주식을 확인할 수 있습니다.\n`$주식 그래프 (회사명)` : 해당 회사의 주식 변동 그래프를 확인할 수 있습니다.\n\n`$돈` : 본인 정보를 확인할 수 있습니다.\n`$순위` : 순위 관련 명령어를 확인할 수 있습니다.\n`$설정` : 설정 관련 명령어를 확인할 수 있습니다.\n```diff\n+ 위 명령어는 자음 또는 영어로 입력할 수 있습니다.```')

@client.command(name='command')
async def help(ctx):
  await ctx.send('`$가입 (닉네임)`  : 시스템에 가입합니다.\n`$탈퇴` : 시스템에서 탈퇴합니다.\n\n`$주식` : 현재 주식 현황을 확인합니다.\n`$주식 구매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 구매합니다.\n`$주식 판매 (번호) (수량)` : 해당 번호의 주식을 수량만큼 판매합니다.\n`$주식 나` : 현재 본인이 보유중인 주식을 확인할 수 있습니다.\n`$주식 그래프 (회사명)` : 해당 회사의 주식 변동 그래프를 확인할 수 있습니다.\n\n`$돈` : 본인 정보를 확인할 수 있습니다.\n`$순위` : 순위 관련 명령어를 확인할 수 있습니다.\n`$설정` : 설정 관련 명령어를 확인할 수 있습니다.\n```diff\n+ 위 명령어는 자음 또는 영어로 입력할 수 있습니다.```')

##############################################################################################################################

@client.command(name='돈')
async def myself(ctx, *text):
  from print_money import print_money
  embed = print_money(ctx,text)
  if type(embed) == str:
    await ctx.send(embed)
  else:
    await ctx.send(embed=embed)

@client.command(name='ㄷ')
async def myself(ctx, *text):
  from print_money import print_money
  embed = print_money(ctx,text)
  if type(embed) == str:
    await ctx.send(embed)
  else:
    await ctx.send(embed=embed)

@client.command(name='e')
async def myself(ctx, *text):
  from print_money import print_money
  embed = print_money(ctx,text)
  if type(embed) == str:
    await ctx.send(embed)
  else:
    await ctx.send(embed=embed)

##############################################################################################################################

# def replace_box(step):
#   if step == '1':
#     return 1000
#   elif step == '2':
#     return 10000
#   elif step == '3':
#     return 100000
#   elif step == '4':
#     return 1000000
#   elif step == '5':
#     return 10000000
#   elif step == '6':
#     return 100000000
#   elif step == '7':
#     return 1000000000
#   elif step == '8':
#     return 10000000000

# @client.command(name='뽑기')
# async def draw(ctx, *text):
#   from draw import draw
#   embed = draw(ctx, text)
#   if type(embed) == str:
#     await ctx.send(embed)
#   else:
#     await ctx.send(embed=embed)

# @client.command(name='Qr')
# async def draw(ctx, *text):
#   from draw import draw
#   embed = draw(ctx, text)
#   if type(embed) == str:
#     await ctx.send(embed)
#   else:
#     await ctx.send(embed=embed)

# @client.command(name='ㅃㄱ')
# async def draw(ctx, *text):
#   from draw import draw
#   embed = draw(ctx, text)
#   if type(embed) == str:
#     await ctx.send(embed)
#   else:
#     await ctx.send(embed=embed)

# @client.command(name='ㅂㄱ')
# async def draw(ctx, *text):
#   from draw import draw
#   embed = draw(ctx, text)
#   if type(embed) == str:
#     await ctx.send(embed)
#   else:
#     await ctx.send(embed=embed)

# @client.command(name='qr')
# async def draw(ctx, *text):
#   from draw import draw
#   embed = draw(ctx, text)
#   if type(embed) == str:
#     await ctx.send(embed)
#   else:
#     await ctx.send(embed=embed)


##############################################################################################################################

@client.command(name='순위')
async def rank(ctx, *text):
  from rank import rank
  embed = rank(ctx, text)
  if type(embed) == str:
    await ctx.send(embed)
  else:
    await ctx.send(embed=embed)

@client.command(name='ㅅㅇ')
async def rank(ctx, *text):
  from rank import rank
  embed = rank(ctx, text)
  if type(embed) == str:
    await ctx.send(embed)
  else:
    await ctx.send(embed=embed)

@client.command(name='td')
async def rank(ctx, *text):
  from rank import rank
  embed = rank(ctx, text)
  if type(embed) == str:
    await ctx.send(embed)
  else:
    await ctx.send(embed=embed)


################################################################################################################################################

@client.command(name='설정')
async def reg(ctx, *text):
  from setting import setting

  ctx_text = setting(ctx, text)

  await ctx.send(ctx_text)
  
@client.command(name='tw')
async def reg(ctx, *text):
  from setting import setting

  ctx_text = setting(ctx, text)

  await ctx.send(ctx_text)

@client.command(name='ㅅㅈ')
async def reg(ctx, *text):
  from setting import setting

  ctx_text = setting(ctx, text)

  await ctx.send(ctx_text)

@client.command(name='setting')
async def reg(ctx, *text):
  from setting import setting

  ctx_text = setting(ctx, text)

  await ctx.send(ctx_text)
  

@tasks.loop(seconds=240)
async def refresh():
    from refresh import refresh
    from restock import restock

    for i in range(20):
        if not i == 19:
            restock()
            time.sleep(12)
        elif i == 19:
            restock()
            refresh()



@client.command(name='start')
async def start(ctx, *text):
    if len(text) == 2:
        order = text[0]
        pw = text [1]

        if str(pw) == "6213" and order == 'refresh':
            refresh.start()
            print("start process - refresh")
            embed = discord.Embed(title = "Sussess Start",
            description = "Start Loop - `ReFresh`" , color = discord.Color.dark_gold()
            )

            await ctx.send(embed=embed)
        

        else:
            embed = discord.Embed(title = "Wrong PassWord",
            description = "Start Loop" , color = discord.Color.dark_red()
            )

            await ctx.send(embed=embed)

    elif len(text) == 1:
        await ctx.send('Input Password!')

@client.command(name='stop')
async def stop(ctx, *text):
    if len(text) == 2:
        order = text[0]
        pw = text [1]

        if str(pw) == "6213" and order == 'refresh':
            refresh.stop()
            print("stop process - refresh")
            embed = discord.Embed(title = "Sussess Stop",
            description = "Stop Loop - `ReFresh`" , color = discord.Color.dark_gold()
            )

            await ctx.send(embed=embed)
        

        else:
            embed = discord.Embed(title = "Wrong PassWord",
            description = "Stop Loop" , color = discord.Color.dark_red()
            )

            await ctx.send(embed=embed)
            
    elif len(text) == 1:
        await ctx.send('Input Password!')

    
    
    
##############################################################################################################################

# @client.event
# async def on_command_error(ctx, error):
#     print('ctx : {}, error : {}'.format(ctx, error))
        

client.run(os.environ['token'])
