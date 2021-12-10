from firebase_admin import db
from randoms import random_value
from get_time import get_time

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


def refresh():
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