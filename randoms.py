import random
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


db_url = 'https://moneygame-34830-default-rtdb.firebaseio.com/'

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "moneygame-34830",
  "private_key_id": "cd18119563a0eafff8d2e124bbcbee364b116b5b",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDIB/0SO+D7GHPF\nioolG1ktlYe18s1ssyA3cfAyJlnM+ojakAcc5ztwL8VQo/7WskAYov3Ex0VxWt/W\noH54ymS/y1BDGKCl8npkzBVZIiiZ6nrBnbP1HINWOPfIRuQYeoX2PyjXK8+2mhs1\nyssROIFAcNxDVw21qPJNgLjbKgFabFOcOExfGTkOJfOV3c50zM6pg3q021fqs4dB\ngfEqP5YmTTxtomIz+kjNRTL493YsEwUOTFeTPf4mo4zX6Mvn81QluA4tAPbOAbUo\nKaWzv23T5bOBqJtkkAzgBSfOSeZsdfl6q5GyqzHC0v+tMX3J6u3KQyJqMJB5Zu9a\n37Rh2tDLAgMBAAECggEAQWMTH9XBCnOIzKcn109kTFlX3ms7KXA4dMdi/BG7Qx0W\nhVOVb6ZKsLZ86ophMG9eMm99Qsjc81wAVZlrHjMS0fs1BmnTgcuMpMxtohBfc0jJ\nzeauP86NRC8lGCvMPhA3IDKvN/8TTB5+DIx46u0smxMJfV3EloBejGUqiEHn5VV1\n2QSr+n8O8YFrZbVRVQmoZEpCuyvFp29qLrpT3py28vAs2mVRIoZU3FEwbze79xRg\nhlfUZgywQwDfDN5HqCYNT/sYrIFTjoNqg7u9L9PDFIP+5naEti2HErr+bRgMI8W0\nG8HOJH0r667DWyklHaq3PxXJVSssRJ3mGaT5kJqiUQKBgQDnIybDGPfeQDBuTl+/\noiHTFD8hSQ1WkLle20yOMZXkv75PFrVnJfg8CVKp8HsQEhl2WQG7Zf+8hR5i7ZPH\njrjfto+IdPGrqOsBLG8Vi/KG4ASBLbe6pG78WvruI9mlZloojvaopkIEO8hSH93Z\nM+DdKKfkI8HNlFHQHy/05YcLwwKBgQDdjEP8+0nV1SkStxtRAisaY+UJo6blUJiF\nUakpK8bqWG6kLRyFwfQ+Rww68s6ZYVKl0oc/Dbf5GXhstKx1iyuACXwXWwruXmZu\nflxUAWgJBKTw3I7EqQPzroprqZ7Im6+Tk7i2Ka8dbtLDtTWGs7Ne0i6OGaOM2Tnx\nUM0Fvk++WQKBgCJkwKfXV0rjElHXp7fEUHQwVxSE4k83Sd4rk8C08DERtyfdoTCw\nHbgRSxOujSFfEBrkM7XG/771sAfYglz3h9sCN2l+vVdl01JhYkY6hOQ9AW6Xdvd2\n8GzsvNoiy4gpKtFONLXzx28J1k0iIMjpR1ShcBoql/QXVfU6LtCqNuYxAoGBAKQW\nDgjhqMbqEHifC2lNPNVX5TvlbGfs8HnViH9IwBOzGYcZLkXW5+n0Pxet29x323mb\nWrYVmAuzlKCWlCCeycITxEecE5WGb0Eo74L8Y6xCN1N5V3hKYfXqcPTadRLJVBnu\nT+EDMIKRISL4JEO29oOlEfwG+z4HaUXUfXTihjdJAoGAdmgCbrA4ll5uUkSW2/j+\nJglBqeEHIO5XjPeEB23XzO8o/kIl8PqVU7ZE0x3uCiLd41JxVG/3iFt1r7sKtRYf\nRX4hgi8wpAXGGzJ5QEY0VPYhvsIZNwef3xDKEEDV67BUKAfLQsbsRhn/I18DpuW8\n06GDHpzjVWYw4pMcsImqgFs=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-9nu82@moneygame-34830.iam.gserviceaccount.com",
  "client_id": "115266264813716255876",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-9nu82%40moneygame-34830.iam.gserviceaccount.com"
}
)

firebase_admin.initialize_app(cred,{
    'databaseURL' : db_url
}) 

def random_value(value):
    li = ['plus', 'zero', 'minus']
    cho = np.random.choice(li, 1, p=[0.48,0.04,0.48])

    lli = ['vs','s','m','b','vb','sp']

    llii = np.random.choice(lli, 1, p=[0.1,0.2,0.39,0.2,0.1,0.01])
    print(llii)
    if llii == 'vs':
        num = random.randrange(1,60)
    elif llii == 's':
        num = random.randrange(61,120)
    elif llii == 'm':
        num = random.randrange(121,180)
    elif llii == 'b':
        num = random.randrange(181,240)
    elif llii == 'vb':
        num = random.randrange(241,300)
    elif llii == 'sp':
        ref = db.reference()
        dic = ref.get()
        sp = [0.25,0.5,0.75,1,1.25,1.5,1.75,2]
        e = random.choice(sp)
        vjtpsxm = str(int(e*100))+'%'
        before = dic['admin']['sp'][vjtpsxm]
        ref.child('admin').child('sp').child(vjtpsxm).set(before+1)


    if llii == 'sp':
        return value * e
    else:
        if cho == 'plus':
            return value + num
        elif cho == 'minus':
            if (value-num) <= 0:
                return value
            else:
                return value - num
        elif cho == 'zero':
            return value