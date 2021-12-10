def replace_e(amount):
    
    amount = amount.split('e+')
    real = amount[0].split('.')
    real = str(int(real[0])) + str(int(real[1]))
    if len(real) < (int(amount[1])+1):
        diff = (int(amount[1])+1) - len(real)
        real = real + ('0'*diff)
    return real


def remove_zero(num):
    #num는 문자열인 숫자
    if num == '0000':
        return num
    elif num[0:3] == '000':
        return num[3:]
    elif num[0:2] == '00':
        return num[2:]
    elif num[0] == '0':
        return num[1:]
    else:
        return num

def replace_amount(amount):
    #amount는 정수
    amount = str(amount)
    if 'e' in amount:
        amount = replace_e(amount)
        print(amount)

    dud = str()
    aks = str()
    djr = str()
    wh = str()
    rud = str()

    tnlist = []

    if len(amount) >= 1 and len(amount) <= 4: #일,십,백,천
        dud = amount
        tnlist.append(dud)

        re = ''
        for i in tnlist:
            re = re + i
        return re

    elif len(amount) >= 5 and len(amount) <= 8: #만,십만,백만,천만
        dud = amount[-4:]
        aks = amount[:-4]
        dud = remove_zero(dud)
        tnlist = [aks, '만 ', dud]

        if dud == '0000':
            tnlist.remove(dud)

        re = ''
        for i in tnlist:
            re = re + i
        return re
        

    elif len(amount) >= 9 and len(amount) <= 12: #억,십억,백억,천억
        dud = amount[-4:]
        aks = amount[-8:-4]
        djr = amount[:-8]
        aks = remove_zero(aks)
        dud = remove_zero(dud)
        tnlist = [djr, '억 ', aks, '만 ', dud]

        if aks == '0000':
            tnlist.remove(aks)
            tnlist.remove('만 ')
        if dud == '0000':
            tnlist.remove(dud)

        re = ''
        for i in tnlist:
            re = re + i
        return re
            

    elif len(amount) >= 13 and len(amount) <= 16: #조,십조,백조,천조
        dud = amount[-4:]
        aks = amount[-8:-4]
        djr = amount[-12:-8]
        wh = amount[:-12]
        djr = remove_zero(djr)
        aks = remove_zero(aks)
        dud = remove_zero(dud)
        tnlist = [wh,'조 ',djr,'억 ',aks,'만 ',dud]

        if aks == '0000':
            tnlist.remove(aks)
            tnlist.remove('만 ')
        if dud == '0000':
            tnlist.remove(dud)
        if djr == '0000':
            tnlist.remove(djr)
            tnlist.remove('억 ')

        re = ''
        for i in tnlist:
            re = re + i
        return re

    elif len(amount) >= 17 and len(amount) <= 20: #경,십경,백경,천경
        dud = amount[-4:]
        aks = amount[-8:-4]
        djr = amount[-12:-8]
        wh = amount[-16:-12]
        rud = amount[:-16]
        wh = remove_zero(wh)
        djr = remove_zero(djr)
        aks = remove_zero(aks)
        dud = remove_zero(dud)
        tnlist = [rud,'경 ',wh,'조 ',djr,'억 ',aks,'만 ',dud]

        if aks == '0000':
            tnlist.remove(aks)
            tnlist.remove('만 ')
        if dud == '0000':
            tnlist.remove(dud)
        if djr == '0000':
            tnlist.remove(djr)
            tnlist.remove('억 ')
        if wh == '0000':
            tnlist.remove(wh)
            tnlist.remove('조 ')
        
        re = ''
        for i in tnlist:
            re = re + i
        return re

    elif len(amount) > 20:
        amount = int(amount)
        amount = format(amount, ',d')
        return(amount)


