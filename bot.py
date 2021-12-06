#-*- coding:utf-8 -*-

import os
import discord
from discord.ext import commands, tasks
from datetime import datetime
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from get_time import get_time
from randoms import random_value
from replace import replace_amount
from graph import save_graph

client = commands.Bot(command_prefix='$')
@client.event
async def on_ready():
    game = discord.Game("Money Game")
    await client.change_presence(status = discord.Status.online, activity = game)


@client.command(name="가입")
async def signup(ctx, *text):
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

    await ctx.send(embed=embed)
  
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
      embed = discord.Embed(title = "회원가입 성공",
      description = "Money Game", color = discord.Color.green()
      )
      embed.add_field(name="%s님 반갑습니다!" %txt, value='Welcome', inline=True)
      embed.add_field(name='보유 자금', value='5000', inline=True)
      # embed.set_thumbnail(url="https://cravatar.eu/helmhead/%s/68.png" %txt)

      ref = db.reference()
      ref.update({'%s'%user_id:{
      'nickname':nickname, 
      'money':5000, 
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

    await ctx.send(embed=embed)

@client.command(name="rd")
async def signup(ctx, *text):
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

    await ctx.send(embed=embed)
  
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
      embed = discord.Embed(title = "회원가입 성공",
      description = "Money Game", color = discord.Color.green()
      )
      embed.add_field(name="%s님 반갑습니다!" %txt, value='Welcome', inline=True)
      embed.add_field(name='보유 자금', value='5000', inline=True)
      # embed.set_thumbnail(url="https://cravatar.eu/helmhead/%s/68.png" %txt)

      ref = db.reference()
      ref.update({'%s'%user_id:{
      'nickname':nickname, 
      'money':5000, 
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

    await ctx.send(embed=embed)

@client.command(name="ㄱㅇ")
async def signup(ctx, *text):
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

    await ctx.send(embed=embed)
  
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
      embed = discord.Embed(title = "회원가입 성공",
      description = "Money Game", color = discord.Color.green()
      )
      embed.add_field(name="%s님 반갑습니다!" %txt, value='Welcome', inline=True)
      embed.add_field(name='보유 자금', value='5000', inline=True)
      # embed.set_thumbnail(url="https://cravatar.eu/helmhead/%s/68.png" %txt)

      ref = db.reference()
      ref.update({'%s'%user_id:{
      'nickname':nickname, 
      'money':5000, 
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

    await ctx.send(embed=embed)

##############################################################################################

@client.command(name="탈퇴")
async def signout(ctx):
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

    await ctx.send(embed=embed)
  
  elif str(user_id) not in user_keys:
    embed = discord.Embed(title ="Money Game 탈퇴",
    description = 'Money Game', color = discord.Color.red()
    )
    embed.add_field(name = '가입하지 않은 계정입니다.', value='`$가입 (닉네임)`\n으로 가입을 진행해주십시오.', inline=False)


    await ctx.send(embed=embed)

@client.command(name="xx")
async def signout(ctx):
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

    await ctx.send(embed=embed)
  
  elif str(user_id) not in user_keys:
    embed = discord.Embed(title ="Money Game 탈퇴",
    description = 'Money Game', color = discord.Color.red()
    )
    embed.add_field(name = '가입하지 않은 계정입니다.', value='`$가입 (닉네임)`\n으로 가입을 진행해주십시오.', inline=False)


    await ctx.send(embed=embed)

@client.command(name="ㅌㅌ")
async def signout(ctx):
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

    await ctx.send(embed=embed)
  
  elif str(user_id) not in user_keys:
    embed = discord.Embed(title ="Money Game 탈퇴",
    description = 'Money Game', color = discord.Color.red()
    )
    embed.add_field(name = '가입하지 않은 계정입니다.', value='`$가입 (닉네임)`\n으로 가입을 진행해주십시오.', inline=False)


    await ctx.send(embed=embed)

##############################################################################################

def dic_in_now(dic, com, time):
  for i in range(1, 11):
    now = dic[i]['now']
    if now == 1:
      value = dic[i]['value']
      rvalue = random_value(value)
      if i == 10:
        i = str(i)
        ref = db.reference()
        ref.child(com).child(i).child('now').set(0)
        ref.child(com).child('1').child('time').set(time['clock'])
        ref.child(com).child('1').child('value').set(rvalue)
        ref.child(com).child('1').child('now').set(1)

      elif i >= 1 and i < 10:
        j = i + 1
        i = str(i)
        j = str(j)
        ref = db.reference()
        ref.child(com).child(i).child('now').set(0)
        ref.child(com).child(j).child('time').set(time['clock'])
        ref.child(com).child(j).child('value').set(rvalue)
        ref.child(com).child(j).child('now').set(1)

def re_time():
  time = get_time()
  ref = db.reference()
  dic = ref.get()
  for i in range(1,11):
    now = dic['ce'][i]['now']
    if now == 1:
      before_time = dic['ce'][i]['time']
      time_gap = int(time['clock'][3:5]) - int(before_time[3:5])
        
      if time_gap == 0:
        second_gap = int(time['clock'][6:]) - int(before_time[6:])
        re = {'gap' : second_gap, 'type' : 'sec'}
        return re
      else:
        re = {'gap' : time_gap, 'type' : 'min'}
        return re


@tasks.loop(seconds=240)
async def refresh():
  ref = db.reference()
  dic = ref.get()
  펭귄 = dic['pg'] # 펭귄 = {1 : {'time':'12:02', 'value' : 1500, 'now' = 0 or 1}, 2 : {...}, ...}
  시네 = dic['sn']
  마코 = dic['mk']
  윤아 = dic['ua']
  냐룽 = dic['nl']
  판다 = dic['pd']
  가온 = dic['go']
  티칩 = dic['tc']
  시루 = dic['sl']
  코어 = dic['ce']

  time = get_time()

  dic_in_now(펭귄, 'pg', time)
  dic_in_now(시네, 'sn', time)
  dic_in_now(마코, 'mk', time)
  dic_in_now(윤아, 'ua', time)
  dic_in_now(냐룽, 'nl', time)
  dic_in_now(판다, 'pd', time)
  dic_in_now(가온, 'go', time)
  dic_in_now(티칩, 'tc', time)
  dic_in_now(시루, 'sl', time)
  dic_in_now(코어, 'ce', time)



##############################################################################################################################

def get_value(dic):
  for i in range(1,11):
    now = dic[i]['now']
    if now == 1:
      if i > 1 and i <= 10:
        j = i-1
        before_value = dic[j]['value']
        now_value = dic[i]['value']
        value_gap = now_value - before_value

        if now_value >= 1000:
          now_value = str(now_value)
          now_value = now_value[0:1] + ',' + now_value[1:]
        else:
          now_value = str(now_value)

        if value_gap > 0 :
          re = {'value' : now_value, 'pm' : '+', 'gap' : '▲'+str(value_gap)}
          return re
        elif value_gap == 0 :
          re = {'value' : now_value, 'pm' : '+', 'gap' : '-'}
          return re
        elif value_gap < 0 :
          value_gap = str(value_gap)
          re = {'value' : now_value, 'pm' : '-', 'gap' : '▼'+value_gap[1:]}
          return re

      elif i == 1:
        j = 10
        before_value = dic[j]['value']
        now_value = dic[i]['value']
        value_gap = now_value - before_value

        if now_value >= 1000:
          now_value = str(now_value)
          now_value = now_value[0:1] + ',' + now_value[1:]
        else:
          now_value = str(now_value)

        if value_gap > 0 :
          re = {'value' : now_value, 'pm' : '+', 'gap' : '▲'+str(value_gap)}
          return re
        elif value_gap == 0 :
          re = {'value' : now_value, 'pm' : '+', 'gap' : '-'}
          return re
        elif value_gap < 0 :
          value_gap = str(value_gap)
          re = {'value' : now_value, 'pm' : '-', 'gap' : '▼'+value_gap[1:]}
          return re

def find_company(input):
  if input == '펭귄증권' or input == '펭귄' or input == 'vr' or input == 'vrwr' or input == 'ㅍㄱ' or input == 'ㅍㄱㅈㄱ':
    return 'pg'
  elif input == '시네제약' or input == '시네' or input == 'ts' or input == 'tswd' or input == 'ㅅㄴ' or input == 'ㅅㄵㅇ' or input == 'ㅅㄴㅈㅇ':
    return 'sn'
  elif input == '마코분식' or input == '마코' or input == 'az' or input == 'azqt' or input == 'ㅁㅋ' or input == 'ㅁㅋㅄ' or input == 'ㅁㅋㅂㅅ':
    return 'mk'
  elif input == '윤아마켓' or input == '윤아' or input == 'dd' or input == 'ddaz' or input == 'ㅇㅇ' or input == 'ㅇㅇㅁㅋ':
    return 'ua'
  elif input == '냐룽제과' or input == '냐룽' or input == 'sf' or input == 'sfwr' or input == 'ㄴㄹ' or input == 'ㄴㄹㅈㄱ':
    return 'nl'
  elif input == '판다은행' or input == '판다' or input == 've' or input == 'vedg' or input == 'ㅍㄷ' or input == 'ㅍㄷㅇㅇ':
    return 'pd'
  elif input == '가온그룹' or input == '가온' or input == 'rd' or input == 'rdrf' or input == 'ㄱㅇ' or input == 'ㄱㅇㄱㄹ':
    return 'go'
  elif input == '티칩화학' or input == '티칩' or input == 'xc' or input == 'xcgg' or input == 'ㅌㅊ' or input == 'ㅌㅊㅎㅎ':
    return 'tc'
  elif input == '시루전자' or input == '시루' or input == 'tf' or input == 'tfww' or input == 'ㅅㄹ' or input == 'ㅅㄹㅈㅈ':
    return 'sl'
  elif input == '코어건설' or input == '코어' or input == 'zd' or input == 'zdrt' or input == 'ㅋㅇ' or input == 'ㅋㅇㄳ' or input == 'ㅋㅇㄱㅅ':
    return 'ce'

def kr_company(com):
  if com =='pg':
    return '펭귄증권'
  elif com == 'sn':
    return '시네제약'
  elif com == 'mk':
    return '마코분식'
  elif com == 'ua':
    return '윤아마켓'
  elif com == 'nl':
    return '냐룽제과'
  elif com == 'pd':
    return '판다은행'
  elif com == 'go':
    return '가온그룹'
  elif com == 'tc':
    return '티칩화학'
  elif com == 'sl':
    return '시루전자'
  elif com == 'ce':
    return '코어건설'

def return_TF_company(company):
  companys = ['pg', 'sn', 'mk', 'ua', 'nl', 'pd', 'go', 'tc', 'sl' ,'ce']
  if company in companys:
    return 'T'
  else:
    return 'F'

def find_now_num(dic):
  for i in range(1, 11):
    now = dic[i]['now']
    if now == 1:
      return i

def find_now_value(dic):
  now = find_now_num(dic)

  return dic[now]['value']

def find_plus_or_minus(before, now, amount):
  if amount == 0:
    return '+0'
  else:
    if now - before > 0:
      return '+%s' %replace_amount((now-before)*amount)
    elif now == before:
      return '+0' 
    elif now - before < 0:
      return '-%s' %replace_amount((before-now)*amount)

@client.command(name="주식")
async def reg(ctx, *text):
  user_keys = []
  if text == ():
    ref = db.reference()
    dic = ref.get()
    펭귄 = dic['pg'] # 펭귄 = {1 : {'time':'12:02', 'value' : 1500, 'now' = 0 or 1}, 2 : {...}, ...}
    시네 = dic['sn']
    마코 = dic['mk']
    윤아 = dic['ua']
    냐룽 = dic['nl']
    판다 = dic['pd']
    가온 = dic['go']
    티칩 = dic['tc']
    시루 = dic['sl']
    코어 = dic['ce']
    pg = get_value(펭귄) # pg = {'value' : now_value, 'pm' : '+', 'gap' : '▲'+str(value_gap)}
    sn = get_value(시네)
    mk = get_value(마코)
    ua = get_value(윤아)
    nl = get_value(냐룽)
    pd = get_value(판다)
    go = get_value(가온)
    tc = get_value(티칩)
    sl = get_value(시루)
    ce = get_value(코어)


    time_gap = re_time() # time_gap = {'gap' : time_gap, 'type' : 'min'}
    now_time = get_time()
    now_time = now_time['clock']
    
    if time_gap['type'] == 'min':
      await ctx.send('주식 정보는 %d분 전 변동됐어요. `%s`\n```diff\n+++ <회사명>  <현재 가치>  <변동량>\n\n%s   펭귄증권     %s    (%s)\n%s   시네제약     %s    (%s)\n%s   마코분식     %s    (%s)\n%s   윤아마켓     %s    (%s)\n%s   냐룽제과     %s    (%s)\n%s   판다은행     %s    (%s)\n%s   가온그룹     %s    (%s)\n%s   티칩화학     %s    (%s)\n%s   시루전자     %s    (%s)\n%s   코어건설     %s    (%s)```\n다음 변동: `%d분 후`'
      %(time_gap['gap'], now_time, pg['pm'], pg['value'], pg['gap'], sn['pm'], sn['value'], sn['gap'], mk['pm'], mk['value'], mk['gap'], ua['pm'], ua['value'], ua['gap'], nl['pm'], nl['value'], nl['gap'], pd['pm'], pd['value'], pd['gap'], go['pm'], go['value'], go['gap'], tc['pm'], tc['value'], tc['gap'], sl['pm'], sl['value'], sl['gap'], ce['pm'], ce['value'], ce['gap'], 4-time_gap['gap']))

    elif time_gap['type'] == 'sec':
      await ctx.send('주식 정보는 %d초 전 변동됐어요. `%s`\n```diff\n+++ <회사명>  <현재 가치>  <변동량>\n\n%s   펭귄증권     %s    (%s)\n%s   시네제약     %s    (%s)\n%s   마코분식     %s    (%s)\n%s   윤아마켓     %s    (%s)\n%s   냐룽제과     %s    (%s)\n%s   판다은행     %s    (%s)\n%s   가온그룹     %s    (%s)\n%s   티칩화학     %s    (%s)\n%s   시루전자     %s    (%s)\n%s   코어건설     %s    (%s)```\n다음 변동: `%d분 후`'
      %(time_gap['gap'], now_time, pg['pm'], pg['value'], pg['gap'], sn['pm'], sn['value'], sn['gap'], mk['pm'], mk['value'], mk['gap'], ua['pm'], ua['value'], ua['gap'], nl['pm'], nl['value'], nl['gap'], pd['pm'], pd['value'], pd['gap'], go['pm'], go['value'], go['gap'], tc['pm'], tc['value'], tc['gap'], sl['pm'], sl['value'], sl['gap'], ce['pm'], ce['value'], ce['gap'], 4))

  else:
    order = text[0]
    user_id = ctx.author.id
    user_name = ctx.author.name

    if order == '나' or order == 'ㄴ' or order=='s':
      ref = db.reference()
      dic = ref.get()

      for i in dic.keys():
        user_keys.append(i)

      if str(user_id) not in user_keys:
        await ctx.send("`$가입 (닉네임)`을 통해 시스템에 가입 후 이용바랍니다.")
      
      else:
        data = dic[str(user_id)]
        nickname = data['nickname']

        펭귄 = [data['pg']['amount'], data['pg']['value']]
        시네 = [data['sn']['amount'], data['sn']['value']]
        마코 = [data['mk']['amount'], data['mk']['value']]
        윤아 = [data['ua']['amount'], data['ua']['value']]
        냐룽 = [data['nl']['amount'], data['nl']['value']]
        판다 = [data['pd']['amount'], data['pd']['value']]
        가온 = [data['go']['amount'], data['go']['value']]
        티칩 = [data['tc']['amount'], data['tc']['value']]
        시루 = [data['sl']['amount'], data['sl']['value']]
        코어 = [data['ce']['amount'], data['ce']['value']]

        pg = find_now_value(dic['pg'])
        sn = find_now_value(dic['sn'])
        mk = find_now_value(dic['mk'])
        ua = find_now_value(dic['ua'])
        nl = find_now_value(dic['nl'])
        pd = find_now_value(dic['pd'])
        go = find_now_value(dic['go'])
        tc = find_now_value(dic['tc'])
        sl = find_now_value(dic['sl'])
        ce = find_now_value(dic['ce'])



        await ctx.send('**%s 님의 주식 정보예요.**```md\n  회사.     보유량.\n============================\n- 펭귄증권   <%s 주>\n  손익: < %s >\n- 시네제약   <%s 주>\n  손익: < %s >\n- 마코분식   <%s 주>\n  손익: < %s >\n- 윤아마켓   <%s 주>\n  손익: < %s >\n- 냐룽제과   <%s 주>\n  손익: < %s >\n- 판다은행   <%s 주>\n  손익: < %s >\n- 가온그룹   <%s 주>\n  손익: < %s >\n- 티칩화학   <%s 주>\n  손익: < %s >\n- 시루전자   <%s 주>\n  손익: < %s >\n- 코어건설   <%s 주>\n  손익: < %s >```'
        %(nickname, 
        replace_amount(펭귄[0]), find_plus_or_minus(펭귄[1],pg,펭귄[0]), 
        replace_amount(시네[0]), find_plus_or_minus(시네[1],sn,시네[0]), 
        replace_amount(마코[0]), find_plus_or_minus(마코[1],mk,마코[0]), 
        replace_amount(윤아[0]), find_plus_or_minus(윤아[1],ua,윤아[0]), 
        replace_amount(냐룽[0]), find_plus_or_minus(냐룽[1],nl,냐룽[0]), 
        replace_amount(판다[0]), find_plus_or_minus(판다[1],pd,판다[0]), 
        replace_amount(가온[0]), find_plus_or_minus(가온[1],go,가온[0]), 
        replace_amount(티칩[0]), find_plus_or_minus(티칩[1],tc,티칩[0]), 
        replace_amount(시루[0]), find_plus_or_minus(시루[1],sl,시루[0]), 
        replace_amount(코어[0]), find_plus_or_minus(코어[1],ce,코어[0])))
      
    elif order == '구매' or order == 'ㄱㅁ' or order == 'ra':
      ref = db.reference()
      dic = ref.get()

      for i in dic.keys():
        user_keys.append(i)

      if str(user_id) not in user_keys:
        await ctx.send("`$가입 (닉네임)`을 통해 시스템에 가입 후 이용바랍니다.")
      
      else:
        if len(text) != 3:
          await ctx.send('잘못된 명령어입니다.\n예시 : `$주식 구매 펭귄증권 100`')
        else:
          company = text[1]
          amount = text[2]
          if type(company) != str:
            await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
          else:
            com = find_company(company)
            re_company = return_TF_company(com)
            
            if re_company == 'F':
              await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
            
            else:
              if amount == '다' or amount == 'ㄷ' or amount == 'all' or amount == 'e':
                com = find_company(company)
                kr_com = kr_company(com)

                ref = db.reference()
                dic = ref.get()
                data = dic[str(user_id)]
                money = data['money']
                taked = data[com]['amount']
                now_num = find_now_num(dic[com])
                now_value = dic[com][now_num]['value']

                amount = int(money / now_value)

                if amount == 0:
                  await ctx.send('보유 금액이 부족합니다.')

                else:
                  ref = db.reference()
                  
                  ref.child(str(user_id)).child(com).child('value').set(now_value)
                  ref.child(str(user_id)).child(com).child('amount').set(amount + taked)
                  ref.child(str(user_id)).child('money').set((money-(amount*now_value)))

                  await ctx.send(
                    '주식을 구매했어요.\n`- %s 코인`\n`+ %s %s 주`'
                    %(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                    )

              else:
                try:
                  amount = int(amount)
                  if amount <= 0:
                    await ctx.send('수량 부분에 자연수만 입력해주십시오.')
                  else:
                    com = find_company(company)
                    kr_com = kr_company(com)

                    ref = db.reference()
                    dic = ref.get()
                    data = dic[str(user_id)]
                    money = data['money']
                    taked = data[com]['amount']
                    now_num = find_now_num(dic[com])
                    now_value = dic[com][now_num]['value']
                    

                    if (amount * now_value) > money:
                      await ctx.send('보유 금액이 부족합니다.')
                    else:
                      ref = db.reference()
                      dic = ref.get()
                      
                      ref.child(str(user_id)).child(com).child('value').set(now_value)
                      ref.child(str(user_id)).child(com).child('amount').set(amount + taked)
                      ref.child(str(user_id)).child('money').set((money-(amount*now_value)))
                      await ctx.send(
                        '주식을 구매했어요.\n`- %s 코인`\n`+ %s %s 주`'
                        %(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                        )
                except:
                  await ctx.send('수량 부분이 자연수가 아니거나 오류가 발생했습니다.\n```diff\n+++ 오류 발생 시 개발자에게 문의 바랍니다.```')

    elif order == '판매' or order == 'ㅍㅁ' or order == 'va':
      ref = db.reference()
      dic = ref.get()

      for i in dic.keys():
        user_keys.append(i)

      if str(user_id) not in user_keys:
        await ctx.send("`$가입 (닉네임)`을 통해 시스템에 가입 후 이용바랍니다.")
      
      else:
        if len(text) != 3:
          await ctx.send('잘못된 명령어입니다.\n예시 : `$주식 판매 펭귄증권 100`')
        else:
          company = text[1]
          amount = text[2]
          if type(company) != str:
            await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
          else:
            com = find_company(company)
            re_company = return_TF_company(com)
            
            if re_company == 'F':
              await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
            
            else:
              if amount == '다' or amount == 'ㄷ' or amount == 'all' or amount == 'e':
                com = find_company(company)
                kr_com = kr_company(com)

                ref = db.reference()
                dic = ref.get()
                data = dic[str(user_id)]
                money = data['money']
                taked = data[com]['amount']
                now_num = find_now_num(dic[com])
                now_value = dic[com][now_num]['value']

                amount = taked

                ref.child(str(user_id)).child(com).child('amount').set(taked - amount)
                ref.child(str(user_id)).child('money').set((money+(amount*now_value)))

                await ctx.send(
                  '주식을 판매했어요.\n`+ %s 코인`\n`- %s %s 주`'
                      %(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                      )
              else:
                try:
                  amount = int(amount)
                  if amount <= 0:
                    await ctx.send('수량 부분에 자연수만 입력해주십시오.')
                  else:
                    com = find_company(company)
                    kr_com = kr_company(com)

                    ref = db.reference()
                    dic = ref.get()
                    data = dic[str(user_id)]
                    money = data['money']
                    taked = data[com]['amount']
                    now_num = find_now_num(dic[com])
                    now_value = dic[com][now_num]['value']

                    if amount > taked:
                      await ctx.send('보유 수량이 입력하신 판매 수량보다 적습니다.')
                    else:
                      ref = db.reference()
                      dic = ref.get()
                      ref.child(str(user_id)).child(com).child('amount').set(taked - amount)
                      ref.child(str(user_id)).child('money').set((money+(amount*now_value)))
                      await ctx.send(
                        '주식을 판매했어요.\n`+ %s 코인`\n`- %s %s 주`'
                        %(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                        )
                except:
                  await ctx.send('수량 부분이 자연수가 아니거나 오류가 발생했습니다.\n```diff\n+++ 오류 발생 시 개발자에게 문의 바랍니다.```')

    elif order == '그래프' or order == 'ㄱㄿ' or order == 'ㄱㄹㅍ' or order == 'rfv' or order == 'graph':
      if len(text) > 2:
        await ctx.send('잘못된 명령어입니다.\n예시 : `$주식 그래프 펭귄증권`')
      else:
        if len(text) == 1:
            save_graph('all')

            with open('%s.png'%'all', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
        else:
            company = text[1]
            if type(company) != str:
                await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
            else:
                com = find_company(company)
                re_company = return_TF_company(com)
                
                if re_company == 'F':
                    await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
                
                else:
                    ref = db.reference()
                    dic = ref.get()
                    com = find_company(company)

                    save_graph(com)
                    
                    with open('%s.png'%com, 'rb') as f:
                        picture = discord.File(f)
                        await ctx.send(file=picture)

    elif len(text) == 1:
      nick = order
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
          user_id = i
          money = dic[str(i)]['money']
          amount = dic[str(i)]['ce']['amount'] + dic[str(i)]['go']['amount'] + dic[str(i)]['mk']['amount'] + dic[str(i)]['nl']['amount'] + dic[str(i)]['pd']['amount'] + dic[str(i)]['sl']['amount'] + dic[str(i)]['sn']['amount'] + dic[str(i)]['tc']['amount'] + dic[str(i)]['ua']['amount'] + dic[str(i)]['pg']['amount']
      
      if money == '' and amount == '':
        await ctx.send('입력하신 닉네임은 존재하지 않는 유저입니다.')
      else:
        ref = db.reference()
        dic = ref.get()
        data = dic[str(user_id)]
        nickname = data['nickname']

        펭귄 = [data['pg']['amount'], data['pg']['value']]
        시네 = [data['sn']['amount'], data['sn']['value']]
        마코 = [data['mk']['amount'], data['mk']['value']]
        윤아 = [data['ua']['amount'], data['ua']['value']]
        냐룽 = [data['nl']['amount'], data['nl']['value']]
        판다 = [data['pd']['amount'], data['pd']['value']]
        가온 = [data['go']['amount'], data['go']['value']]
        티칩 = [data['tc']['amount'], data['tc']['value']]
        시루 = [data['sl']['amount'], data['sl']['value']]
        코어 = [data['ce']['amount'], data['ce']['value']]

        pg = find_now_value(dic['pg'])
        sn = find_now_value(dic['sn'])
        mk = find_now_value(dic['mk'])
        ua = find_now_value(dic['ua'])
        nl = find_now_value(dic['nl'])
        pd = find_now_value(dic['pd'])
        go = find_now_value(dic['go'])
        tc = find_now_value(dic['tc'])
        sl = find_now_value(dic['sl'])
        ce = find_now_value(dic['ce'])



        await ctx.send('**%s 님의 주식 정보예요.**```md\n  회사.     보유량.\n============================\n- 펭귄증권   <%s 주>\n  손익: < %s >\n- 시네제약   <%s 주>\n  손익: < %s >\n- 마코분식   <%s 주>\n  손익: < %s >\n- 윤아마켓   <%s 주>\n  손익: < %s >\n- 냐룽제과   <%s 주>\n  손익: < %s >\n- 판다은행   <%s 주>\n  손익: < %s >\n- 가온그룹   <%s 주>\n  손익: < %s >\n- 티칩화학   <%s 주>\n  손익: < %s >\n- 시루전자   <%s 주>\n  손익: < %s >\n- 코어건설   <%s 주>\n  손익: < %s >```'
        %(nickname, 
        replace_amount(펭귄[0]), find_plus_or_minus(펭귄[1],pg,펭귄[0]), 
        replace_amount(시네[0]), find_plus_or_minus(시네[1],sn,시네[0]), 
        replace_amount(마코[0]), find_plus_or_minus(마코[1],mk,마코[0]), 
        replace_amount(윤아[0]), find_plus_or_minus(윤아[1],ua,윤아[0]), 
        replace_amount(냐룽[0]), find_plus_or_minus(냐룽[1],nl,냐룽[0]), 
        replace_amount(판다[0]), find_plus_or_minus(판다[1],pd,판다[0]), 
        replace_amount(가온[0]), find_plus_or_minus(가온[1],go,가온[0]), 
        replace_amount(티칩[0]), find_plus_or_minus(티칩[1],tc,티칩[0]), 
        replace_amount(시루[0]), find_plus_or_minus(시루[1],sl,시루[0]), 
        replace_amount(코어[0]), find_plus_or_minus(코어[1],ce,코어[0])))


@client.command(name="wt")
async def reg(ctx, *text):
  user_keys = []
  if text == ():
    ref = db.reference()
    dic = ref.get()
    펭귄 = dic['pg'] # 펭귄 = {1 : {'time':'12:02', 'value' : 1500, 'now' = 0 or 1}, 2 : {...}, ...}
    시네 = dic['sn']
    마코 = dic['mk']
    윤아 = dic['ua']
    냐룽 = dic['nl']
    판다 = dic['pd']
    가온 = dic['go']
    티칩 = dic['tc']
    시루 = dic['sl']
    코어 = dic['ce']
    pg = get_value(펭귄) # pg = {'value' : now_value, 'pm' : '+', 'gap' : '▲'+str(value_gap)}
    sn = get_value(시네)
    mk = get_value(마코)
    ua = get_value(윤아)
    nl = get_value(냐룽)
    pd = get_value(판다)
    go = get_value(가온)
    tc = get_value(티칩)
    sl = get_value(시루)
    ce = get_value(코어)


    time_gap = re_time() # time_gap = {'gap' : time_gap, 'type' : 'min'}
    now_time = get_time()
    now_time = now_time['clock']
    
    if time_gap['type'] == 'min':
      await ctx.send('주식 정보는 %d분 전 변동됐어요. `%s`\n```diff\n+++ <회사명>  <현재 가치>  <변동량>\n\n%s   펭귄증권     %s    (%s)\n%s   시네제약     %s    (%s)\n%s   마코분식     %s    (%s)\n%s   윤아마켓     %s    (%s)\n%s   냐룽제과     %s    (%s)\n%s   판다은행     %s    (%s)\n%s   가온그룹     %s    (%s)\n%s   티칩화학     %s    (%s)\n%s   시루전자     %s    (%s)\n%s   코어건설     %s    (%s)```\n다음 변동: `%d분 후`'
      %(time_gap['gap'], now_time, pg['pm'], pg['value'], pg['gap'], sn['pm'], sn['value'], sn['gap'], mk['pm'], mk['value'], mk['gap'], ua['pm'], ua['value'], ua['gap'], nl['pm'], nl['value'], nl['gap'], pd['pm'], pd['value'], pd['gap'], go['pm'], go['value'], go['gap'], tc['pm'], tc['value'], tc['gap'], sl['pm'], sl['value'], sl['gap'], ce['pm'], ce['value'], ce['gap'], 4-time_gap['gap']))

    elif time_gap['type'] == 'sec':
      await ctx.send('주식 정보는 %d초 전 변동됐어요. `%s`\n```diff\n+++ <회사명>  <현재 가치>  <변동량>\n\n%s   펭귄증권     %s    (%s)\n%s   시네제약     %s    (%s)\n%s   마코분식     %s    (%s)\n%s   윤아마켓     %s    (%s)\n%s   냐룽제과     %s    (%s)\n%s   판다은행     %s    (%s)\n%s   가온그룹     %s    (%s)\n%s   티칩화학     %s    (%s)\n%s   시루전자     %s    (%s)\n%s   코어건설     %s    (%s)```\n다음 변동: `%d분 후`'
      %(time_gap['gap'], now_time, pg['pm'], pg['value'], pg['gap'], sn['pm'], sn['value'], sn['gap'], mk['pm'], mk['value'], mk['gap'], ua['pm'], ua['value'], ua['gap'], nl['pm'], nl['value'], nl['gap'], pd['pm'], pd['value'], pd['gap'], go['pm'], go['value'], go['gap'], tc['pm'], tc['value'], tc['gap'], sl['pm'], sl['value'], sl['gap'], ce['pm'], ce['value'], ce['gap'], 4))

  else:
    order = text[0]
    user_id = ctx.author.id
    user_name = ctx.author.name

    if order == '나' or order == 'ㄴ' or order=='s':
      ref = db.reference()
      dic = ref.get()

      for i in dic.keys():
        user_keys.append(i)

      if str(user_id) not in user_keys:
        await ctx.send("`$가입 (닉네임)`을 통해 시스템에 가입 후 이용바랍니다.")
      
      else:
        data = dic[str(user_id)]
        nickname = data['nickname']

        펭귄 = [data['pg']['amount'], data['pg']['value']]
        시네 = [data['sn']['amount'], data['sn']['value']]
        마코 = [data['mk']['amount'], data['mk']['value']]
        윤아 = [data['ua']['amount'], data['ua']['value']]
        냐룽 = [data['nl']['amount'], data['nl']['value']]
        판다 = [data['pd']['amount'], data['pd']['value']]
        가온 = [data['go']['amount'], data['go']['value']]
        티칩 = [data['tc']['amount'], data['tc']['value']]
        시루 = [data['sl']['amount'], data['sl']['value']]
        코어 = [data['ce']['amount'], data['ce']['value']]

        pg = find_now_value(dic['pg'])
        sn = find_now_value(dic['sn'])
        mk = find_now_value(dic['mk'])
        ua = find_now_value(dic['ua'])
        nl = find_now_value(dic['nl'])
        pd = find_now_value(dic['pd'])
        go = find_now_value(dic['go'])
        tc = find_now_value(dic['tc'])
        sl = find_now_value(dic['sl'])
        ce = find_now_value(dic['ce'])



        await ctx.send('**%s 님의 주식 정보예요.**```md\n  회사.     보유량.\n============================\n- 펭귄증권   <%s 주>\n  손익: < %s >\n- 시네제약   <%s 주>\n  손익: < %s >\n- 마코분식   <%s 주>\n  손익: < %s >\n- 윤아마켓   <%s 주>\n  손익: < %s >\n- 냐룽제과   <%s 주>\n  손익: < %s >\n- 판다은행   <%s 주>\n  손익: < %s >\n- 가온그룹   <%s 주>\n  손익: < %s >\n- 티칩화학   <%s 주>\n  손익: < %s >\n- 시루전자   <%s 주>\n  손익: < %s >\n- 코어건설   <%s 주>\n  손익: < %s >```'
        %(nickname, 
        replace_amount(펭귄[0]), find_plus_or_minus(펭귄[1],pg,펭귄[0]), 
        replace_amount(시네[0]), find_plus_or_minus(시네[1],sn,시네[0]), 
        replace_amount(마코[0]), find_plus_or_minus(마코[1],mk,마코[0]), 
        replace_amount(윤아[0]), find_plus_or_minus(윤아[1],ua,윤아[0]), 
        replace_amount(냐룽[0]), find_plus_or_minus(냐룽[1],nl,냐룽[0]), 
        replace_amount(판다[0]), find_plus_or_minus(판다[1],pd,판다[0]), 
        replace_amount(가온[0]), find_plus_or_minus(가온[1],go,가온[0]), 
        replace_amount(티칩[0]), find_plus_or_minus(티칩[1],tc,티칩[0]), 
        replace_amount(시루[0]), find_plus_or_minus(시루[1],sl,시루[0]), 
        replace_amount(코어[0]), find_plus_or_minus(코어[1],ce,코어[0])))
      
    elif order == '구매' or order == 'ㄱㅁ' or order == 'ra':
      ref = db.reference()
      dic = ref.get()

      for i in dic.keys():
        user_keys.append(i)

      if str(user_id) not in user_keys:
        await ctx.send("`$가입 (닉네임)`을 통해 시스템에 가입 후 이용바랍니다.")
      
      else:
        if len(text) != 3:
          await ctx.send('잘못된 명령어입니다.\n예시 : `$주식 구매 펭귄증권 100`')
        else:
          company = text[1]
          amount = text[2]
          if type(company) != str:
            await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
          else:
            com = find_company(company)
            re_company = return_TF_company(com)
            
            if re_company == 'F':
              await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
            
            else:
              if amount == '다' or amount == 'ㄷ' or amount == 'all' or amount == 'e':
                com = find_company(company)
                kr_com = kr_company(com)

                ref = db.reference()
                dic = ref.get()
                data = dic[str(user_id)]
                money = data['money']
                taked = data[com]['amount']
                now_num = find_now_num(dic[com])
                now_value = dic[com][now_num]['value']

                amount = int(money / now_value)

                if amount == 0:
                  await ctx.send('보유 금액이 부족합니다.')

                else:
                  ref = db.reference()
                  
                  ref.child(str(user_id)).child(com).child('value').set(now_value)
                  ref.child(str(user_id)).child(com).child('amount').set(amount + taked)
                  ref.child(str(user_id)).child('money').set((money-(amount*now_value)))

                  await ctx.send(
                    '주식을 구매했어요.\n`- %s 코인`\n`+ %s %s 주`'
                    %(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                    )

              else:
                try:
                  amount = int(amount)
                  if amount <= 0:
                    await ctx.send('수량 부분에 자연수만 입력해주십시오.')
                  else:
                    com = find_company(company)
                    kr_com = kr_company(com)

                    ref = db.reference()
                    dic = ref.get()
                    data = dic[str(user_id)]
                    money = data['money']
                    taked = data[com]['amount']
                    now_num = find_now_num(dic[com])
                    now_value = dic[com][now_num]['value']
                    

                    if (amount * now_value) > money:
                      await ctx.send('보유 금액이 부족합니다.')
                    else:
                      ref = db.reference()
                      dic = ref.get()
                      
                      ref.child(str(user_id)).child(com).child('value').set(now_value)
                      ref.child(str(user_id)).child(com).child('amount').set(amount + taked)
                      ref.child(str(user_id)).child('money').set((money-(amount*now_value)))
                      await ctx.send(
                        '주식을 구매했어요.\n`- %s 코인`\n`+ %s %s 주`'
                        %(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                        )
                except:
                  await ctx.send('수량 부분이 자연수가 아니거나 오류가 발생했습니다.\n```diff\n+++ 오류 발생 시 개발자에게 문의 바랍니다.```')

    elif order == '판매' or order == 'ㅍㅁ' or order == 'va':
      ref = db.reference()
      dic = ref.get()

      for i in dic.keys():
        user_keys.append(i)

      if str(user_id) not in user_keys:
        await ctx.send("`$가입 (닉네임)`을 통해 시스템에 가입 후 이용바랍니다.")
      
      else:
        if len(text) != 3:
          await ctx.send('잘못된 명령어입니다.\n예시 : `$주식 판매 펭귄증권 100`')
        else:
          company = text[1]
          amount = text[2]
          if type(company) != str:
            await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
          else:
            com = find_company(company)
            re_company = return_TF_company(com)
            
            if re_company == 'F':
              await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
            
            else:
              if amount == '다' or amount == 'ㄷ' or amount == 'all' or amount == 'e':
                com = find_company(company)
                kr_com = kr_company(com)

                ref = db.reference()
                dic = ref.get()
                data = dic[str(user_id)]
                money = data['money']
                taked = data[com]['amount']
                now_num = find_now_num(dic[com])
                now_value = dic[com][now_num]['value']

                amount = taked

                ref.child(str(user_id)).child(com).child('amount').set(taked - amount)
                ref.child(str(user_id)).child('money').set((money+(amount*now_value)))

                await ctx.send(
                  '주식을 판매했어요.\n`+ %s 코인`\n`- %s %s 주`'
                      %(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                      )
              else:
                try:
                  amount = int(amount)
                  if amount <= 0:
                    await ctx.send('수량 부분에 자연수만 입력해주십시오.')
                  else:
                    com = find_company(company)
                    kr_com = kr_company(com)

                    ref = db.reference()
                    dic = ref.get()
                    data = dic[str(user_id)]
                    money = data['money']
                    taked = data[com]['amount']
                    now_num = find_now_num(dic[com])
                    now_value = dic[com][now_num]['value']

                    if amount > taked:
                      await ctx.send('보유 수량이 입력하신 판매 수량보다 적습니다.')
                    else:
                      ref = db.reference()
                      dic = ref.get()
                      ref.child(str(user_id)).child(com).child('amount').set(taked - amount)
                      ref.child(str(user_id)).child('money').set((money+(amount*now_value)))
                      await ctx.send(
                        '주식을 판매했어요.\n`+ %s 코인`\n`- %s %s 주`'
                        %(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                        )
                except:
                  await ctx.send('수량 부분이 자연수가 아니거나 오류가 발생했습니다.\n```diff\n+++ 오류 발생 시 개발자에게 문의 바랍니다.```')

    elif order == '그래프' or order == 'ㄱㄿ' or order == 'ㄱㄹㅍ' or order == 'rfv' or order == 'graph':
      if len(text) > 2:
        await ctx.send('잘못된 명령어입니다.\n예시 : `$주식 그래프 펭귄증권`')
      else:
        if len(text) == 1:
            save_graph('all')

            with open('%s.png'%'all', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
        else:
            company = text[1]
            if type(company) != str:
                await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
            else:
                com = find_company(company)
                re_company = return_TF_company(com)
                
                if re_company == 'F':
                    await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
                
                else:
                    ref = db.reference()
                    dic = ref.get()
                    com = find_company(company)

                    save_graph(com)
                    
                    with open('%s.png'%com, 'rb') as f:
                        picture = discord.File(f)
                        await ctx.send(file=picture)

    elif len(text) == 1:
      nick = order
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
          user_id = i
          money = dic[str(i)]['money']
          amount = dic[str(i)]['ce']['amount'] + dic[str(i)]['go']['amount'] + dic[str(i)]['mk']['amount'] + dic[str(i)]['nl']['amount'] + dic[str(i)]['pd']['amount'] + dic[str(i)]['sl']['amount'] + dic[str(i)]['sn']['amount'] + dic[str(i)]['tc']['amount'] + dic[str(i)]['ua']['amount'] + dic[str(i)]['pg']['amount']
      
      if money == '' and amount == '':
        await ctx.send('입력하신 닉네임은 존재하지 않는 유저입니다.')
      else:
        ref = db.reference()
        dic = ref.get()
        data = dic[str(user_id)]
        nickname = data['nickname']

        펭귄 = [data['pg']['amount'], data['pg']['value']]
        시네 = [data['sn']['amount'], data['sn']['value']]
        마코 = [data['mk']['amount'], data['mk']['value']]
        윤아 = [data['ua']['amount'], data['ua']['value']]
        냐룽 = [data['nl']['amount'], data['nl']['value']]
        판다 = [data['pd']['amount'], data['pd']['value']]
        가온 = [data['go']['amount'], data['go']['value']]
        티칩 = [data['tc']['amount'], data['tc']['value']]
        시루 = [data['sl']['amount'], data['sl']['value']]
        코어 = [data['ce']['amount'], data['ce']['value']]

        pg = find_now_value(dic['pg'])
        sn = find_now_value(dic['sn'])
        mk = find_now_value(dic['mk'])
        ua = find_now_value(dic['ua'])
        nl = find_now_value(dic['nl'])
        pd = find_now_value(dic['pd'])
        go = find_now_value(dic['go'])
        tc = find_now_value(dic['tc'])
        sl = find_now_value(dic['sl'])
        ce = find_now_value(dic['ce'])



        await ctx.send('**%s 님의 주식 정보예요.**```md\n  회사.     보유량.\n============================\n- 펭귄증권   <%s 주>\n  손익: < %s >\n- 시네제약   <%s 주>\n  손익: < %s >\n- 마코분식   <%s 주>\n  손익: < %s >\n- 윤아마켓   <%s 주>\n  손익: < %s >\n- 냐룽제과   <%s 주>\n  손익: < %s >\n- 판다은행   <%s 주>\n  손익: < %s >\n- 가온그룹   <%s 주>\n  손익: < %s >\n- 티칩화학   <%s 주>\n  손익: < %s >\n- 시루전자   <%s 주>\n  손익: < %s >\n- 코어건설   <%s 주>\n  손익: < %s >```'
        %(nickname, 
        replace_amount(펭귄[0]), find_plus_or_minus(펭귄[1],pg,펭귄[0]), 
        replace_amount(시네[0]), find_plus_or_minus(시네[1],sn,시네[0]), 
        replace_amount(마코[0]), find_plus_or_minus(마코[1],mk,마코[0]), 
        replace_amount(윤아[0]), find_plus_or_minus(윤아[1],ua,윤아[0]), 
        replace_amount(냐룽[0]), find_plus_or_minus(냐룽[1],nl,냐룽[0]), 
        replace_amount(판다[0]), find_plus_or_minus(판다[1],pd,판다[0]), 
        replace_amount(가온[0]), find_plus_or_minus(가온[1],go,가온[0]), 
        replace_amount(티칩[0]), find_plus_or_minus(티칩[1],tc,티칩[0]), 
        replace_amount(시루[0]), find_plus_or_minus(시루[1],sl,시루[0]), 
        replace_amount(코어[0]), find_plus_or_minus(코어[1],ce,코어[0])))

@client.command(name="ㅈㅅ")
async def reg(ctx, *text):
  user_keys = []
  if text == ():
    ref = db.reference()
    dic = ref.get()
    펭귄 = dic['pg'] # 펭귄 = {1 : {'time':'12:02', 'value' : 1500, 'now' = 0 or 1}, 2 : {...}, ...}
    시네 = dic['sn']
    마코 = dic['mk']
    윤아 = dic['ua']
    냐룽 = dic['nl']
    판다 = dic['pd']
    가온 = dic['go']
    티칩 = dic['tc']
    시루 = dic['sl']
    코어 = dic['ce']
    pg = get_value(펭귄) # pg = {'value' : now_value, 'pm' : '+', 'gap' : '▲'+str(value_gap)}
    sn = get_value(시네)
    mk = get_value(마코)
    ua = get_value(윤아)
    nl = get_value(냐룽)
    pd = get_value(판다)
    go = get_value(가온)
    tc = get_value(티칩)
    sl = get_value(시루)
    ce = get_value(코어)


    time_gap = re_time() # time_gap = {'gap' : time_gap, 'type' : 'min'}
    now_time = get_time()
    now_time = now_time['clock']
    
    if time_gap['type'] == 'min':
      await ctx.send('주식 정보는 %d분 전 변동됐어요. `%s`\n```diff\n+++ <회사명>  <현재 가치>  <변동량>\n\n%s   펭귄증권     %s    (%s)\n%s   시네제약     %s    (%s)\n%s   마코분식     %s    (%s)\n%s   윤아마켓     %s    (%s)\n%s   냐룽제과     %s    (%s)\n%s   판다은행     %s    (%s)\n%s   가온그룹     %s    (%s)\n%s   티칩화학     %s    (%s)\n%s   시루전자     %s    (%s)\n%s   코어건설     %s    (%s)```\n다음 변동: `%d분 후`'
      %(time_gap['gap'], now_time, pg['pm'], pg['value'], pg['gap'], sn['pm'], sn['value'], sn['gap'], mk['pm'], mk['value'], mk['gap'], ua['pm'], ua['value'], ua['gap'], nl['pm'], nl['value'], nl['gap'], pd['pm'], pd['value'], pd['gap'], go['pm'], go['value'], go['gap'], tc['pm'], tc['value'], tc['gap'], sl['pm'], sl['value'], sl['gap'], ce['pm'], ce['value'], ce['gap'], 4-time_gap['gap']))

    elif time_gap['type'] == 'sec':
      await ctx.send('주식 정보는 %d초 전 변동됐어요. `%s`\n```diff\n+++ <회사명>  <현재 가치>  <변동량>\n\n%s   펭귄증권     %s    (%s)\n%s   시네제약     %s    (%s)\n%s   마코분식     %s    (%s)\n%s   윤아마켓     %s    (%s)\n%s   냐룽제과     %s    (%s)\n%s   판다은행     %s    (%s)\n%s   가온그룹     %s    (%s)\n%s   티칩화학     %s    (%s)\n%s   시루전자     %s    (%s)\n%s   코어건설     %s    (%s)```\n다음 변동: `%d분 후`'
      %(time_gap['gap'], now_time, pg['pm'], pg['value'], pg['gap'], sn['pm'], sn['value'], sn['gap'], mk['pm'], mk['value'], mk['gap'], ua['pm'], ua['value'], ua['gap'], nl['pm'], nl['value'], nl['gap'], pd['pm'], pd['value'], pd['gap'], go['pm'], go['value'], go['gap'], tc['pm'], tc['value'], tc['gap'], sl['pm'], sl['value'], sl['gap'], ce['pm'], ce['value'], ce['gap'], 4))

  else:
    order = text[0]
    user_id = ctx.author.id
    user_name = ctx.author.name

    if order == '나' or order == 'ㄴ' or order=='s':
      ref = db.reference()
      dic = ref.get()

      for i in dic.keys():
        user_keys.append(i)

      if str(user_id) not in user_keys:
        await ctx.send("`$가입 (닉네임)`을 통해 시스템에 가입 후 이용바랍니다.")
      
      else:
        data = dic[str(user_id)]
        nickname = data['nickname']

        펭귄 = [data['pg']['amount'], data['pg']['value']]
        시네 = [data['sn']['amount'], data['sn']['value']]
        마코 = [data['mk']['amount'], data['mk']['value']]
        윤아 = [data['ua']['amount'], data['ua']['value']]
        냐룽 = [data['nl']['amount'], data['nl']['value']]
        판다 = [data['pd']['amount'], data['pd']['value']]
        가온 = [data['go']['amount'], data['go']['value']]
        티칩 = [data['tc']['amount'], data['tc']['value']]
        시루 = [data['sl']['amount'], data['sl']['value']]
        코어 = [data['ce']['amount'], data['ce']['value']]

        pg = find_now_value(dic['pg'])
        sn = find_now_value(dic['sn'])
        mk = find_now_value(dic['mk'])
        ua = find_now_value(dic['ua'])
        nl = find_now_value(dic['nl'])
        pd = find_now_value(dic['pd'])
        go = find_now_value(dic['go'])
        tc = find_now_value(dic['tc'])
        sl = find_now_value(dic['sl'])
        ce = find_now_value(dic['ce'])



        await ctx.send('**%s 님의 주식 정보예요.**```md\n  회사.     보유량.\n============================\n- 펭귄증권   <%s 주>\n  손익: < %s >\n- 시네제약   <%s 주>\n  손익: < %s >\n- 마코분식   <%s 주>\n  손익: < %s >\n- 윤아마켓   <%s 주>\n  손익: < %s >\n- 냐룽제과   <%s 주>\n  손익: < %s >\n- 판다은행   <%s 주>\n  손익: < %s >\n- 가온그룹   <%s 주>\n  손익: < %s >\n- 티칩화학   <%s 주>\n  손익: < %s >\n- 시루전자   <%s 주>\n  손익: < %s >\n- 코어건설   <%s 주>\n  손익: < %s >```'
        %(nickname, 
        replace_amount(펭귄[0]), find_plus_or_minus(펭귄[1],pg,펭귄[0]), 
        replace_amount(시네[0]), find_plus_or_minus(시네[1],sn,시네[0]), 
        replace_amount(마코[0]), find_plus_or_minus(마코[1],mk,마코[0]), 
        replace_amount(윤아[0]), find_plus_or_minus(윤아[1],ua,윤아[0]), 
        replace_amount(냐룽[0]), find_plus_or_minus(냐룽[1],nl,냐룽[0]), 
        replace_amount(판다[0]), find_plus_or_minus(판다[1],pd,판다[0]), 
        replace_amount(가온[0]), find_plus_or_minus(가온[1],go,가온[0]), 
        replace_amount(티칩[0]), find_plus_or_minus(티칩[1],tc,티칩[0]), 
        replace_amount(시루[0]), find_plus_or_minus(시루[1],sl,시루[0]), 
        replace_amount(코어[0]), find_plus_or_minus(코어[1],ce,코어[0])))
      
    elif order == '구매' or order == 'ㄱㅁ' or order == 'ra':
      ref = db.reference()
      dic = ref.get()

      for i in dic.keys():
        user_keys.append(i)

      if str(user_id) not in user_keys:
        await ctx.send("`$가입 (닉네임)`을 통해 시스템에 가입 후 이용바랍니다.")
      
      else:
        if len(text) != 3:
          await ctx.send('잘못된 명령어입니다.\n예시 : `$주식 구매 펭귄증권 100`')
        else:
          company = text[1]
          amount = text[2]
          if type(company) != str:
            await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
          else:
            com = find_company(company)
            re_company = return_TF_company(com)
            
            if re_company == 'F':
              await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
            
            else:
              if amount == '다' or amount == 'ㄷ' or amount == 'all' or amount == 'e':
                com = find_company(company)
                kr_com = kr_company(com)

                ref = db.reference()
                dic = ref.get()
                data = dic[str(user_id)]
                money = data['money']
                taked = data[com]['amount']
                now_num = find_now_num(dic[com])
                now_value = dic[com][now_num]['value']

                amount = int(money / now_value)

                if amount == 0:
                  await ctx.send('보유 금액이 부족합니다.')

                else:
                  ref = db.reference()
                  
                  ref.child(str(user_id)).child(com).child('value').set(now_value)
                  ref.child(str(user_id)).child(com).child('amount').set(amount + taked)
                  ref.child(str(user_id)).child('money').set((money-(amount*now_value)))

                  await ctx.send(
                    '주식을 구매했어요.\n`- %s 코인`\n`+ %s %s 주`'
                    %(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                    )

              else:
                try:
                  amount = int(amount)
                  if amount <= 0:
                    await ctx.send('수량 부분에 자연수만 입력해주십시오.')
                  else:
                    com = find_company(company)
                    kr_com = kr_company(com)

                    ref = db.reference()
                    dic = ref.get()
                    data = dic[str(user_id)]
                    money = data['money']
                    taked = data[com]['amount']
                    now_num = find_now_num(dic[com])
                    now_value = dic[com][now_num]['value']
                    

                    if (amount * now_value) > money:
                      await ctx.send('보유 금액이 부족합니다.')
                    else:
                      ref = db.reference()
                      dic = ref.get()
                      
                      ref.child(str(user_id)).child(com).child('value').set(now_value)
                      ref.child(str(user_id)).child(com).child('amount').set(amount + taked)
                      ref.child(str(user_id)).child('money').set((money-(amount*now_value)))
                      await ctx.send(
                        '주식을 구매했어요.\n`- %s 코인`\n`+ %s %s 주`'
                        %(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                        )
                except:
                  await ctx.send('수량 부분이 자연수가 아니거나 오류가 발생했습니다.\n```diff\n+++ 오류 발생 시 개발자에게 문의 바랍니다.```')

    elif order == '판매' or order == 'ㅍㅁ' or order == 'va':
      ref = db.reference()
      dic = ref.get()

      for i in dic.keys():
        user_keys.append(i)

      if str(user_id) not in user_keys:
        await ctx.send("`$가입 (닉네임)`을 통해 시스템에 가입 후 이용바랍니다.")
      
      else:
        if len(text) != 3:
          await ctx.send('잘못된 명령어입니다.\n예시 : `$주식 판매 펭귄증권 100`')
        else:
          company = text[1]
          amount = text[2]
          if type(company) != str:
            await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
          else:
            com = find_company(company)
            re_company = return_TF_company(com)
            
            if re_company == 'F':
              await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
            
            else:
              if amount == '다' or amount == 'ㄷ' or amount == 'all' or amount == 'e':
                com = find_company(company)
                kr_com = kr_company(com)

                ref = db.reference()
                dic = ref.get()
                data = dic[str(user_id)]
                money = data['money']
                taked = data[com]['amount']
                now_num = find_now_num(dic[com])
                now_value = dic[com][now_num]['value']

                amount = taked

                ref.child(str(user_id)).child(com).child('amount').set(taked - amount)
                ref.child(str(user_id)).child('money').set((money+(amount*now_value)))

                await ctx.send(
                  '주식을 판매했어요.\n`+ %s 코인`\n`- %s %s 주`'
                      %(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                      )
              else:
                try:
                  amount = int(amount)
                  if amount <= 0:
                    await ctx.send('수량 부분에 자연수만 입력해주십시오.')
                  else:
                    com = find_company(company)
                    kr_com = kr_company(com)

                    ref = db.reference()
                    dic = ref.get()
                    data = dic[str(user_id)]
                    money = data['money']
                    taked = data[com]['amount']
                    now_num = find_now_num(dic[com])
                    now_value = dic[com][now_num]['value']

                    if amount > taked:
                      await ctx.send('보유 수량이 입력하신 판매 수량보다 적습니다.')
                    else:
                      ref = db.reference()
                      dic = ref.get()
                      ref.child(str(user_id)).child(com).child('amount').set(taked - amount)
                      ref.child(str(user_id)).child('money').set((money+(amount*now_value)))
                      await ctx.send(
                        '주식을 판매했어요.\n`+ %s 코인`\n`- %s %s 주`'
                        %(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                        )
                except:
                  await ctx.send('수량 부분이 자연수가 아니거나 오류가 발생했습니다.\n```diff\n+++ 오류 발생 시 개발자에게 문의 바랍니다.```')

    elif order == '그래프' or order == 'ㄱㄿ' or order == 'ㄱㄹㅍ' or order == 'rfv' or order == 'graph':
      if len(text) > 2:
        await ctx.send('잘못된 명령어입니다.\n예시 : `$주식 그래프 펭귄증권`')
      else:
        if len(text) == 1:
            save_graph('all')

            with open('%s.png'%'all', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
        else:
            company = text[1]
            if type(company) != str:
                await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
            else:
                com = find_company(company)
                re_company = return_TF_company(com)
                
                if re_company == 'F':
                    await ctx.send('잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오')
                
                else:
                    ref = db.reference()
                    dic = ref.get()
                    com = find_company(company)

                    save_graph(com)
                    
                    with open('%s.png'%com, 'rb') as f:
                        picture = discord.File(f)
                        await ctx.send(file=picture)

    elif len(text) == 1:
      nick = order
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
          user_id = i
          money = dic[str(i)]['money']
          amount = dic[str(i)]['ce']['amount'] + dic[str(i)]['go']['amount'] + dic[str(i)]['mk']['amount'] + dic[str(i)]['nl']['amount'] + dic[str(i)]['pd']['amount'] + dic[str(i)]['sl']['amount'] + dic[str(i)]['sn']['amount'] + dic[str(i)]['tc']['amount'] + dic[str(i)]['ua']['amount'] + dic[str(i)]['pg']['amount']
      
      if money == '' and amount == '':
        await ctx.send('입력하신 닉네임은 존재하지 않는 유저입니다.')
      else:
        ref = db.reference()
        dic = ref.get()
        data = dic[str(user_id)]
        nickname = data['nickname']

        펭귄 = [data['pg']['amount'], data['pg']['value']]
        시네 = [data['sn']['amount'], data['sn']['value']]
        마코 = [data['mk']['amount'], data['mk']['value']]
        윤아 = [data['ua']['amount'], data['ua']['value']]
        냐룽 = [data['nl']['amount'], data['nl']['value']]
        판다 = [data['pd']['amount'], data['pd']['value']]
        가온 = [data['go']['amount'], data['go']['value']]
        티칩 = [data['tc']['amount'], data['tc']['value']]
        시루 = [data['sl']['amount'], data['sl']['value']]
        코어 = [data['ce']['amount'], data['ce']['value']]

        pg = find_now_value(dic['pg'])
        sn = find_now_value(dic['sn'])
        mk = find_now_value(dic['mk'])
        ua = find_now_value(dic['ua'])
        nl = find_now_value(dic['nl'])
        pd = find_now_value(dic['pd'])
        go = find_now_value(dic['go'])
        tc = find_now_value(dic['tc'])
        sl = find_now_value(dic['sl'])
        ce = find_now_value(dic['ce'])



        await ctx.send('**%s 님의 주식 정보예요.**```md\n  회사.     보유량.\n============================\n- 펭귄증권   <%s 주>\n  손익: < %s >\n- 시네제약   <%s 주>\n  손익: < %s >\n- 마코분식   <%s 주>\n  손익: < %s >\n- 윤아마켓   <%s 주>\n  손익: < %s >\n- 냐룽제과   <%s 주>\n  손익: < %s >\n- 판다은행   <%s 주>\n  손익: < %s >\n- 가온그룹   <%s 주>\n  손익: < %s >\n- 티칩화학   <%s 주>\n  손익: < %s >\n- 시루전자   <%s 주>\n  손익: < %s >\n- 코어건설   <%s 주>\n  손익: < %s >```'
        %(nickname, 
        replace_amount(펭귄[0]), find_plus_or_minus(펭귄[1],pg,펭귄[0]), 
        replace_amount(시네[0]), find_plus_or_minus(시네[1],sn,시네[0]), 
        replace_amount(마코[0]), find_plus_or_minus(마코[1],mk,마코[0]), 
        replace_amount(윤아[0]), find_plus_or_minus(윤아[1],ua,윤아[0]), 
        replace_amount(냐룽[0]), find_plus_or_minus(냐룽[1],nl,냐룽[0]), 
        replace_amount(판다[0]), find_plus_or_minus(판다[1],pd,판다[0]), 
        replace_amount(가온[0]), find_plus_or_minus(가온[1],go,가온[0]), 
        replace_amount(티칩[0]), find_plus_or_minus(티칩[1],tc,티칩[0]), 
        replace_amount(시루[0]), find_plus_or_minus(시루[1],sl,시루[0]), 
        replace_amount(코어[0]), find_plus_or_minus(코어[1],ce,코어[0])))


################################################################################################################################################

@client.command(name='도움말')
async def help(ctx):
  await ctx.send('`$가입 (닉네임)`  : 시스템에 가입합니다.\n`$탈퇴` : 시스템에서 탈퇴합니다.\n`$주식` : 현재 주식 현황을 확인합니다.\n`$주식 구매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 구매합니다.\n`$주식 판매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 판매합니다.\n`$주식 나` : 현재 본인이 보유중인 주식을 확인할 수 있습니다.\n`$주식 그래프 (회사명)` : 해당 회사의 주식 변동 그래프를 확인할 수 있습니다.\n`$돈` : 본인 정보를 확인할 수 있습니다.\n```diff\n+ 위 명령어는 자음 또는 영어로 입력할 수 있습니다.```')

@client.command(name='명령어')
async def help(ctx):
  await ctx.send('`$가입 (닉네임)`  : 시스템에 가입합니다.\n`$탈퇴` : 시스템에서 탈퇴합니다.\n`$주식` : 현재 주식 현황을 확인합니다.\n`$주식 구매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 구매합니다.\n`$주식 판매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 판매합니다.\n`$주식 나` : 현재 본인이 보유중인 주식을 확인할 수 있습니다.\n`$주식 그래프 (회사명)` : 해당 회사의 주식 변동 그래프를 확인할 수 있습니다.\n`$돈` : 본인 정보를 확인할 수 있습니다.\n```diff\n+ 위 명령어는 자음 또는 영어로 입력할 수 있습니다.```')

@client.command(name='?')
async def help(ctx):
  await ctx.send('`$가입 (닉네임)`  : 시스템에 가입합니다.\n`$탈퇴` : 시스템에서 탈퇴합니다.\n`$주식` : 현재 주식 현황을 확인합니다.\n`$주식 구매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 구매합니다.\n`$주식 판매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 판매합니다.\n`$주식 나` : 현재 본인이 보유중인 주식을 확인할 수 있습니다.\n`$주식 그래프 (회사명)` : 해당 회사의 주식 변동 그래프를 확인할 수 있습니다.\n`$돈` : 본인 정보를 확인할 수 있습니다.\n```diff\n+ 위 명령어는 자음 또는 영어로 입력할 수 있습니다.```')

@client.command(name='command')
async def help(ctx):
  await ctx.send('`$가입 (닉네임)`  : 시스템에 가입합니다.\n`$탈퇴` : 시스템에서 탈퇴합니다.\n`$주식` : 현재 주식 현황을 확인합니다.\n`$주식 구매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 구매합니다.\n`$주식 판매 (회사명) (수량)` : 해당 회사의 주식을 수량만큼 판매합니다.\n`$주식 나` : 현재 본인이 보유중인 주식을 확인할 수 있습니다.\n`$주식 그래프 (회사명)` : 해당 회사의 주식 변동 그래프를 확인할 수 있습니다.\n`$돈` : 본인 정보를 확인할 수 있습니다.\n```diff\n+ 위 명령어는 자음 또는 영어로 입력할 수 있습니다.```')

##############################################################################################################################

@client.command(name='돈')
async def myself(ctx, *text):
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
    await ctx.send(embed=embed)
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
      await ctx.send('입력하신 닉네임은 존재하지 않는 유저ㅇ입니다.')
    else:
      embed = discord.Embed(
      color = discord.Color.blue()
      )
      embed.add_field(name=":dollar: 보유 자금", value="**%s**" %replace_amount(money), inline=False)
      embed.add_field(name=":chart_with_upwards_trend: 총 보유 주", value="**%s**" %replace_amount(amount), inline=False)
      embed.set_footer(text='%s님의 정보' %nick)
      await ctx.send(embed=embed)

@client.command(name='ㄷ')
async def myself(ctx, *text):
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
    await ctx.send(embed=embed)
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
      await ctx.send('입력하신 닉네임은 존재하지 않는 유저ㅇ입니다.')
    else:
      embed = discord.Embed(
      color = discord.Color.blue()
      )
      embed.add_field(name=":dollar: 보유 자금", value="**%s**" %replace_amount(money), inline=False)
      embed.add_field(name=":chart_with_upwards_trend: 총 보유 주", value="**%s**" %replace_amount(amount), inline=False)
      embed.set_footer(text='%s님의 정보' %nick)
      await ctx.send(embed=embed)

@client.command(name='e')
async def myself(ctx, *text):
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
    await ctx.send(embed=embed)
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
      await ctx.send('입력하신 닉네임은 존재하지 않는 유저ㅇ입니다.')
    else:
      embed = discord.Embed(
      color = discord.Color.blue()
      )
      embed.add_field(name=":dollar: 보유 자금", value="**%s**" %replace_amount(money), inline=False)
      embed.add_field(name=":chart_with_upwards_trend: 총 보유 주", value="**%s**" %replace_amount(amount), inline=False)
      embed.set_footer(text='%s님의 정보' %nick)
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
