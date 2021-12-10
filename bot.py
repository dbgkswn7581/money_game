#-*- coding:utf-8 -*-

import os
import discord
from discord.colour import Color
from discord.ext import commands, tasks
from datetime import datetime
import time
from discord.ext.commands import bot
from discord.flags import Intents
from firebase_admin import credentials
from firebase_admin import db
from randoms import random_value


intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="$", intents=intents)

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

##############################################################################################

@tasks.loop(seconds=240)
async def refresh():
  from refresh import refresh

  refresh()


##############################################################################################################################

@client.command(name="주식")
async def reg(ctx, *text):
  from stock import stock
  ctx_text = stock(ctx, text)

  if type(ctx_text) == list:
    await ctx.send(file=ctx_text[0])

  else:
    await ctx.send(ctx_text)

@client.command(name="wt")
async def reg(ctx, *text):
  from stock import stock
  ctx_text = stock(ctx, text)

  if type(ctx_text) == list:
    await ctx.send(file=ctx_text[0])

  else:
    await ctx.send(ctx_text)

@client.command(name="ㅈㅅ")
async def reg(ctx, *text):
  from stock import stock
  ctx_text = stock(ctx, text)

  if type(ctx_text) == list:
    await ctx.send(file=ctx_text[0])

  else:
    await ctx.send(ctx_text)


################################################################################################################################################

@client.command(name='도움말')
async def help(ctx):
  await ctx.send('`$가입 (닉네임)`  : 시스템에 가입합니다.\n`$탈퇴` : 시스템에서 탈퇴합니다.\n\n`$주식` : 현재 주식 현황을 확인합니다.\n`$주식 구매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 구매합니다.\n`$주식 판매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 판매합니다.\n`$주식 나` : 현재 본인이 보유중인 주식을 확인할 수 있습니다.\n`$주식 그래프 (회사명)` : 해당 회사의 주식 변동 그래프를 확인할 수 있습니다.\n\n`$돈` : 본인 정보를 확인할 수 있습니다.\n`$순위` : 순위 관련 명령어를 확인할 수 있습니다.\n`$뽑기` : 뽑기 관련 명령어를 확인할 수 있습니다.\n```diff\n+ 위 명령어는 자음 또는 영어로 입력할 수 있습니다.```')

@client.command(name='명령어')
async def help(ctx):
  await ctx.send('`$가입 (닉네임)`  : 시스템에 가입합니다.\n`$탈퇴` : 시스템에서 탈퇴합니다.\n\n`$주식` : 현재 주식 현황을 확인합니다.\n`$주식 구매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 구매합니다.\n`$주식 판매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 판매합니다.\n`$주식 나` : 현재 본인이 보유중인 주식을 확인할 수 있습니다.\n`$주식 그래프 (회사명)` : 해당 회사의 주식 변동 그래프를 확인할 수 있습니다.\n\n`$돈` : 본인 정보를 확인할 수 있습니다.\n`$순위` : 순위 관련 명령어를 확인할 수 있습니다.\n`$뽑기` : 뽑기 관련 명령어를 확인할 수 있습니다.\n```diff\n+ 위 명령어는 자음 또는 영어로 입력할 수 있습니다.```')

@client.command(name='?')
async def help(ctx):
  await ctx.send('`$가입 (닉네임)`  : 시스템에 가입합니다.\n`$탈퇴` : 시스템에서 탈퇴합니다.\n\n`$주식` : 현재 주식 현황을 확인합니다.\n`$주식 구매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 구매합니다.\n`$주식 판매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 판매합니다.\n`$주식 나` : 현재 본인이 보유중인 주식을 확인할 수 있습니다.\n`$주식 그래프 (회사명)` : 해당 회사의 주식 변동 그래프를 확인할 수 있습니다.\n\n`$돈` : 본인 정보를 확인할 수 있습니다.\n`$순위` : 순위 관련 명령어를 확인할 수 있습니다.\n`$뽑기` : 뽑기 관련 명령어를 확인할 수 있습니다.\n```diff\n+ 위 명령어는 자음 또는 영어로 입력할 수 있습니다.```')

@client.command(name='command')
async def help(ctx):
  await ctx.send('`$가입 (닉네임)`  : 시스템에 가입합니다.\n`$탈퇴` : 시스템에서 탈퇴합니다.\n\n`$주식` : 현재 주식 현황을 확인합니다.\n`$주식 구매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 구매합니다.\n`$주식 판매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 판매합니다.\n`$주식 나` : 현재 본인이 보유중인 주식을 확인할 수 있습니다.\n`$주식 그래프 (회사명)` : 해당 회사의 주식 변동 그래프를 확인할 수 있습니다.\n\n`$돈` : 본인 정보를 확인할 수 있습니다.\n`$순위` : 순위 관련 명령어를 확인할 수 있습니다.\n`$뽑기` : 뽑기 관련 명령어를 확인할 수 있습니다.\n```diff\n+ 위 명령어는 자음 또는 영어로 입력할 수 있습니다.```')

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

@client.command(name='뽑기')
async def draw(ctx, *text):
  from draw import draw
  embed = draw(ctx, text)
  if type(embed) == str:
    await ctx.send(embed)
  else:
    await ctx.send(embed=embed)

@client.command(name='Qr')
async def draw(ctx, *text):
  from draw import draw
  embed = draw(ctx, text)
  if type(embed) == str:
    await ctx.send(embed)
  else:
    await ctx.send(embed=embed)

@client.command(name='ㅃㄱ')
async def draw(ctx, *text):
  from draw import draw
  embed = draw(ctx, text)
  if type(embed) == str:
    await ctx.send(embed)
  else:
    await ctx.send(embed=embed)

@client.command(name='ㅂㄱ')
async def draw(ctx, *text):
  from draw import draw
  embed = draw(ctx, text)
  if type(embed) == str:
    await ctx.send(embed)
  else:
    await ctx.send(embed=embed)

@client.command(name='qr')
async def draw(ctx, *text):
  from draw import draw
  embed = draw(ctx, text)
  if type(embed) == str:
    await ctx.send(embed)
  else:
    await ctx.send(embed=embed)


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



##############################################################################################################################

@client.command(name='start')
async def start(ctx, *text):
    pw = text[0]
    
    if str(pw) == "6213":
        refresh.start()
        print("start process")
        embed = discord.Embed(title = "Sussess Start",
        description = "Start Loop" , color = discord.Color.dark_gold()
        )

        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title = "Wrong PassWord",
        description = "Start Loop" , color = discord.Color.dark_red()
        )

        await ctx.send(embed=embed)

@client.command(name='restart')
async def restart(ctx, *text):
    pw = text[0]

    if str(pw) == "6213":
        refresh.stop()
        time.sleep(0.3)
        refresh.restart()
        print("restart process")
        embed = discord.Embed(title = "Sussess Restart",
        description = "ReStart Loop" , color = discord.Color.dark_gold()
        )

        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title = "Wrong PassWord",
        description = "ReStart Loop" , color = discord.Color.dark_red()
        )

        await ctx.send(embed=embed)

@client.command(name='stop')
async def stop(ctx, *text):
    pw = text[0]
    
    if str(pw) == "6213":
        refresh.stop()
        print("stop process")

        embed = discord.Embed(title = "Sussess Stop",
        description = "Stop Loop" , color = discord.Color.dark_gold()
        )

        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title = "Wrong PassWord",
        description = "Stop Loop" , color = discord.Color.dark_red()
        )

        await ctx.send(embed=embed)


client.run(os.environ['token'])
