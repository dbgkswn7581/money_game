import sqlite3

def setting(ctx, text):
    user_id = ctx.author.id
    
    

    if text == ():
        ctx_text = '`$설정 주식 (번호)` : \n(번호)에 1을 입력 시 모든 주식 정보가 표시되고, \n2를 입력 시 JJISI 주식 정보만 표시되고, \n3을 입력 시 KOSPI 주식 정보만 표시됩니다.'
        return ctx_text

    elif len(text) == 1:
        order = text[0]
        if order == '주식' or order == 'wt' or order == 'ㅈㅅ' or order == 'stock':
            ctx_text = '(번호)를 입력하지 않으셨습니다. \n사용 예시 : `$설정 주식 2`'

    elif len(text) == 2:
        order = text[0]
        choose = text[1]

        if order == '주식' or order == 'wt' or order == 'ㅈㅅ' or order == 'stock':
            if choose == '1':
                conn = sqlite3.connect('user.db', isolation_level=None)
                c = conn.cursor()
                c.execute('UPDATE user SET choose=? WHERE id=?', (1,str(user_id)))

                ctx_text = '이제부터 `모든 주식` 정보가 표시됩니다.'
                return ctx_text

            elif choose == '2':
                conn = sqlite3.connect('user.db', isolation_level=None)
                c = conn.cursor()
                c.execute('UPDATE user SET choose=? WHERE id=?', (2,str(user_id)))
                ctx_text = '이제부터 `NNSTG` 정보만 표시됩니다.'
                return ctx_text

            elif choose == '3':
                conn = sqlite3.connect('user.db', isolation_level=None)
                c = conn.cursor()
                c.execute('UPDATE user SET choose=? WHERE id=?', (3,str(user_id)))
                ctx_text = '이제부터 `KOSPI` 정보만 표시됩니다.'
                return ctx_text