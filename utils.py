import pandas as pd 

from datetime import date, datetime

def to_csv(df):
    now_date = str(date.today()).replace('-', '')
    now_time = str(datetime.now().time())[:8].replace(':', '')
    now_datetime = now_date + '_' + now_time
    
    df.to_csv(f'./output_{now_datetime}.csv')