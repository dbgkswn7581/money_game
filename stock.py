from firebase_admin import db
from get_time import get_time
from replace import replace_amount
from graph import save_graph
import discord



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

def get_value(dic):
  for i in range(1,11):
    now = dic[i]['now']
    if now == 1:
      if i > 1 and i <= 10:
        j = i-1
        before_value = dic[j]['value']
        now_value = dic[i]['value']
        value_gap = now_value - before_value

        now_value = format(now_value, ',d')

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

        now_value = format(now_value, ',d')

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

def return_TF_company(company):
  companys = ['pg', 'sn', 'mk', 'ua', 'nl', 'pd', 'go', 'tc', 'sl' ,'ce']
  if company in companys:
    return 'T'
  else:
    return 'F'

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


def stock(ctx, text):
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
            if time_gap['gap'] < 0:
                time_gap['gap'] = time_gap['gap'] * (-1)
                time_gap['gap'] = 60 - time_gap['gap']
            
            
            ctx_text = '주식 정보는 %d분 전 변동됐어요. `%s`\n```diff\n+++ <회사명>  <현재 가치>  <변동량>\n\n%s   펭귄증권     %s    (%s)\n%s   시네제약     %s    (%s)\n%s   마코분식     %s    (%s)\n%s   윤아마켓     %s    (%s)\n%s   냐룽제과     %s    (%s)\n%s   판다은행     %s    (%s)\n%s   가온그룹     %s    (%s)\n%s   티칩화학     %s    (%s)\n%s   시루전자     %s    (%s)\n%s   코어건설     %s    (%s)```\n다음 변동: `%d분 후`'%(time_gap['gap'], now_time, pg['pm'], pg['value'], pg['gap'], sn['pm'], sn['value'], sn['gap'], mk['pm'], mk['value'], mk['gap'], ua['pm'], ua['value'], ua['gap'], nl['pm'], nl['value'], nl['gap'], pd['pm'], pd['value'], pd['gap'], go['pm'], go['value'], go['gap'], tc['pm'], tc['value'], tc['gap'], sl['pm'], sl['value'], sl['gap'], ce['pm'], ce['value'], ce['gap'], 4-time_gap['gap'])
            return ctx_text

            
        elif time_gap['type'] == 'sec':
            ctx_text = '주식 정보는 %d초 전 변동됐어요. `%s`\n```diff\n+++ <회사명>  <현재 가치>  <변동량>\n\n%s   펭귄증권     %s    (%s)\n%s   시네제약     %s    (%s)\n%s   마코분식     %s    (%s)\n%s   윤아마켓     %s    (%s)\n%s   냐룽제과     %s    (%s)\n%s   판다은행     %s    (%s)\n%s   가온그룹     %s    (%s)\n%s   티칩화학     %s    (%s)\n%s   시루전자     %s    (%s)\n%s   코어건설     %s    (%s)```\n다음 변동: `%d분 후`'%(time_gap['gap'], now_time, pg['pm'], pg['value'], pg['gap'], sn['pm'], sn['value'], sn['gap'], mk['pm'], mk['value'], mk['gap'], ua['pm'], ua['value'], ua['gap'], nl['pm'], nl['value'], nl['gap'], pd['pm'], pd['value'], pd['gap'], go['pm'], go['value'], go['gap'], tc['pm'], tc['value'], tc['gap'], sl['pm'], sl['value'], sl['gap'], ce['pm'], ce['value'], ce['gap'], 4)
            return ctx_text
            

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
                ctx_text = "`$가입 (닉네임)`을 통해 시스템에 가입 후 이용바랍니다."
                return ctx_text
                
            
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

                ctx_text = '**%s 님의 주식 정보예요.**```md\n  회사.     보유량.\n============================\n- 펭귄증권   <%s 주>\n  손익: < %s >\n- 시네제약   <%s 주>\n  손익: < %s >\n- 마코분식   <%s 주>\n  손익: < %s >\n- 윤아마켓   <%s 주>\n  손익: < %s >\n- 냐룽제과   <%s 주>\n  손익: < %s >\n- 판다은행   <%s 주>\n  손익: < %s >\n- 가온그룹   <%s 주>\n  손익: < %s >\n- 티칩화학   <%s 주>\n  손익: < %s >\n- 시루전자   <%s 주>\n  손익: < %s >\n- 코어건설   <%s 주>\n  손익: < %s >```'%(nickname, 
                replace_amount(펭귄[0]), find_plus_or_minus(펭귄[1],pg,펭귄[0]), 
                replace_amount(시네[0]), find_plus_or_minus(시네[1],sn,시네[0]), 
                replace_amount(마코[0]), find_plus_or_minus(마코[1],mk,마코[0]), 
                replace_amount(윤아[0]), find_plus_or_minus(윤아[1],ua,윤아[0]), 
                replace_amount(냐룽[0]), find_plus_or_minus(냐룽[1],nl,냐룽[0]), 
                replace_amount(판다[0]), find_plus_or_minus(판다[1],pd,판다[0]), 
                replace_amount(가온[0]), find_plus_or_minus(가온[1],go,가온[0]), 
                replace_amount(티칩[0]), find_plus_or_minus(티칩[1],tc,티칩[0]), 
                replace_amount(시루[0]), find_plus_or_minus(시루[1],sl,시루[0]), 
                replace_amount(코어[0]), find_plus_or_minus(코어[1],ce,코어[0]))
                

                return ctx_text
        
        elif order == '구매' or order == 'ㄱㅁ' or order == 'ra':
            ref = db.reference()
            dic = ref.get()

            for i in dic.keys():
                user_keys.append(i)

            if str(user_id) not in user_keys:
                ctx_text = "`$가입 (닉네임)`을 통해 시스템에 가입 후 이용바랍니다."
                return ctx_text
                
            
            else:
                if len(text) != 3:
                    ctx_text = '잘못된 명령어입니다.\n예시 : `$주식 구매 펭귄증권 100`'
                    return ctx_text
                    
                else:
                    company = text[1]
                    amount = text[2]
                    if type(company) != str:
                        ctx_text = '잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오'
                        return ctx_text
                    else:
                        com = find_company(company)
                        re_company = return_TF_company(com)
                        
                        if re_company == 'F':
                            ctx_text = '잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오'
                            return ctx_text
                            
                        
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
                                    ctx_text = '보유 금액이 부족합니다.'
                                    return ctx_text
                                    

                                else:
                                    ref = db.reference()
                                    
                                    ref.child(str(user_id)).child(com).child('value').set(now_value)
                                    ref.child(str(user_id)).child(com).child('amount').set(amount + taked)
                                    ref.child(str(user_id)).child('money').set((money-(amount*now_value)))
                                    
                                    ctx_text = '주식을 구매했어요.\n`- %s 코인`\n`+ %s %s 주`'%(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                                        
                                    return ctx_text

                            else:
                                try:
                                    amount = int(amount)
                                    if amount <= 0:
                                        ctx_text = '수량 부분에 자연수만 입력해주십시오.'
                                        return ctx_text
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
                                            ctx_text = '보유 금액이 부족합니다.'
                                            return ctx_text
                                            
                                        else:
                                            ref = db.reference()
                                            dic = ref.get()
                                            
                                            ref.child(str(user_id)).child(com).child('value').set(now_value)
                                            ref.child(str(user_id)).child(com).child('amount').set(amount + taked)
                                            ref.child(str(user_id)).child('money').set((money-(amount*now_value)))

                                            ctx_text = '주식을 구매했어요.\n`- %s 코인`\n`+ %s %s 주`'%(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                                            return ctx_text
                                                
                                except:
                                    ctx_text = '수량 부분이 자연수가 아니거나 오류가 발생했습니다.\n```diff\n+++ 오류 발생 시 개발자에게 문의 바랍니다.```'
                                    return ctx_text
                                    

        elif order == '판매' or order == 'ㅍㅁ' or order == 'va':
            ref = db.reference()
            dic = ref.get()

            for i in dic.keys():
                user_keys.append(i)

            if str(user_id) not in user_keys:
                ctx_text = "`$가입 (닉네임)`을 통해 시스템에 가입 후 이용바랍니다."
                return ctx_text
        
            else:
                if len(text) != 3:
                    ctx_text = '잘못된 명령어입니다.\n예시 : `$주식 판매 펭귄증권 100`'
                    return ctx_text
                else:
                    company = text[1]
                    amount = text[2]
                    if type(company) != str:
                        ctx_text = '잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오'
                        return ctx_text
                        
                    else:
                        com = find_company(company)
                        re_company = return_TF_company(com)
                        
                        if re_company == 'F':
                            ctx_text = '잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오'
                            return ctx_text
                        
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

                                ctx_text = '주식을 판매했어요.\n`+ %s 코인`\n`- %s %s 주`'%(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                                    
                                return ctx_text
                            

                            else:
                                try:
                                    amount = int(amount)
                                    if amount <= 0:
                                        ctx_text = '수량 부분에 자연수만 입력해주십시오.'
                                        return ctx_text
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
                                            ctx_text = '보유 수량이 입력하신 판매 수량보다 적습니다.'
                                            return ctx_text
                                            
                                        else:
                                            ref = db.reference()
                                            dic = ref.get()
                                            ref.child(str(user_id)).child(com).child('amount').set(taked - amount)
                                            ref.child(str(user_id)).child('money').set((money+(amount*now_value)))
                                            ctx_text = '주식을 판매했어요.\n`+ %s 코인`\n`- %s %s 주`'%(replace_amount(amount*now_value), kr_com, replace_amount(amount))
                                            return ctx_text
                                                

                                except:
                                    ctx_text = '수량 부분이 자연수가 아니거나 오류가 발생했습니다.\n```diff\n+++ 오류 발생 시 개발자에게 문의 바랍니다.```'
                                    return ctx_text

        elif order == '그래프' or order == 'ㄱㄿ' or order == 'ㄱㄹㅍ' or order == 'rfv' or order == 'graph':
            if len(text) > 2:
                ctx_text = '잘못된 명령어입니다.\n예시 : `$주식 그래프 펭귄증권`'
                return ctx_text
            else:
                if len(text) == 1:
                    save_graph('all')

                    with open('%s.png'%'all', 'rb') as f:
                        picture = discord.File(f)
                        ctx_text = [picture,'file']
                        return ctx_text
                else:
                    company = text[1]
                    if type(company) != str:
                        ctx_text = '잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오'
                        return ctx_text
                    else:
                        com = find_company(company)
                        re_company = return_TF_company(com)
                        
                        if re_company == 'F':
                            ctx_text = '잘못된 회사명입니다.\n`$주식`을 통해 회사명을 확인해주십시오'
                            return ctx_text
                        
                        else:
                            ref = db.reference()
                            dic = ref.get()
                            com = find_company(company)

                            save_graph(com)
                            
                            with open('%s.png'%com, 'rb') as f:
                                picture = discord.File(f)
                                ctx_text = [picture,'file']
                                return ctx_text

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
            del dic['samsung']
            del dic['kakao']
            del dic['naver']
            del dic['korean']
            del dic['kolon']
            del dic['hyundai']

            money = str()
            amount = str()

            user_ids = list(dic.keys())
            for i in user_ids:
                if nick == dic[str(i)]['nickname']:
                    user_id = i
                    money = dic[str(i)]['money']
                    amount = dic[str(i)]['ce']['amount'] + dic[str(i)]['go']['amount'] + dic[str(i)]['mk']['amount'] + dic[str(i)]['nl']['amount'] + dic[str(i)]['pd']['amount'] + dic[str(i)]['sl']['amount'] + dic[str(i)]['sn']['amount'] + dic[str(i)]['tc']['amount'] + dic[str(i)]['ua']['amount'] + dic[str(i)]['pg']['amount']
            
            if money == '' and amount == '':
                ctx_text = '입력하신 닉네임은 존재하지 않는 유저입니다.'
                return ctx_text
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

                ctx_text = '**%s 님의 주식 정보예요.**```md\n  회사.     보유량.\n============================\n- 펭귄증권   <%s 주>\n  손익: < %s >\n- 시네제약   <%s 주>\n  손익: < %s >\n- 마코분식   <%s 주>\n  손익: < %s >\n- 윤아마켓   <%s 주>\n  손익: < %s >\n- 냐룽제과   <%s 주>\n  손익: < %s >\n- 판다은행   <%s 주>\n  손익: < %s >\n- 가온그룹   <%s 주>\n  손익: < %s >\n- 티칩화학   <%s 주>\n  손익: < %s >\n- 시루전자   <%s 주>\n  손익: < %s >\n- 코어건설   <%s 주>\n  손익: < %s >```'%(nickname, 
                replace_amount(펭귄[0]), find_plus_or_minus(펭귄[1],pg,펭귄[0]), 
                replace_amount(시네[0]), find_plus_or_minus(시네[1],sn,시네[0]), 
                replace_amount(마코[0]), find_plus_or_minus(마코[1],mk,마코[0]), 
                replace_amount(윤아[0]), find_plus_or_minus(윤아[1],ua,윤아[0]), 
                replace_amount(냐룽[0]), find_plus_or_minus(냐룽[1],nl,냐룽[0]), 
                replace_amount(판다[0]), find_plus_or_minus(판다[1],pd,판다[0]), 
                replace_amount(가온[0]), find_plus_or_minus(가온[1],go,가온[0]), 
                replace_amount(티칩[0]), find_plus_or_minus(티칩[1],tc,티칩[0]), 
                replace_amount(시루[0]), find_plus_or_minus(시루[1],sl,시루[0]), 
                replace_amount(코어[0]), find_plus_or_minus(코어[1],ce,코어[0]))
                

                return ctx_text
