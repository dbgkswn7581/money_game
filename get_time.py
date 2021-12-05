import datetime as dt
import pytz

def get_time():
    UTC = pytz.timezone('Asia/Seoul')
    time = dt.datetime.now(UTC)
    time = str(time)
    date = time[:10]
    clock = time[11:19]
    dic = {'date' : date, 'clock' : clock}
    return dic
