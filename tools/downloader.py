import time
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine
import requests

cookies = {
    'cookiesu': '221701699251944',
    'device_id': '60606df41d6038f8e464999c75a733a5',
    'remember': '1',
    'xq_is_login': '1',
    'u': '9556330693',
    'xq_a_token': 'b18840fe11faa444aeddec3a1cf69d824a015aa8',
    'xqat': 'b18840fe11faa444aeddec3a1cf69d824a015aa8',
    'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjk1NTYzMzA2OTMsImlzcyI6InVjIiwiZXhwIjoxNzA1ODQ0NjMyLCJjdG0iOjE3MDMyNTI2MzI1MTEsImNpZCI6ImQ5ZDBuNEFadXAifQ.O7Vdq6vUHSP7_J4wux34vjOQ9oDwti0E6LCvvOgPx56BiRpiVqsVlU48eFLHDcMdvzEz8SbA0l9RI8m_ETKiVPv-Y1n6y9g4KoQWugWhmjJRbmRE_4yDTY4PDMWn69adgQsFib3n7lndnQoUroT7yTDS_rBFi7rXaZwvT3wBqsAMrI5P1TWYc2X-WCEup0FE_13DIFRLnJlODW6BCIAdeDjIPMmmj61BurTLX-sMypHLgr8tzuYmAumZBXi1-u4yhCK7cQqHfc2s1y7_8HCFMSXW6YLGM9yYeVv3KvQgwCNY30qXkJXPWoD4RGNJejMzUeeRgcIijBTkjLrQ5xW7uA',
    'xq_r_token': '7fbde5901fe0c7e736dea69b1b5a606d7f045516',
    'is_overseas': '0',
    'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1701699797,1702205998,1703252640',
    'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1703252640',
}

headers = {
    'authority': 'stock.xueqiu.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'cookiesu=221701699251944; device_id=60606df41d6038f8e464999c75a733a5; remember=1; xq_is_login=1; u=9556330693; xq_a_token=b18840fe11faa444aeddec3a1cf69d824a015aa8; xqat=b18840fe11faa444aeddec3a1cf69d824a015aa8; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjk1NTYzMzA2OTMsImlzcyI6InVjIiwiZXhwIjoxNzA1ODQ0NjMyLCJjdG0iOjE3MDMyNTI2MzI1MTEsImNpZCI6ImQ5ZDBuNEFadXAifQ.O7Vdq6vUHSP7_J4wux34vjOQ9oDwti0E6LCvvOgPx56BiRpiVqsVlU48eFLHDcMdvzEz8SbA0l9RI8m_ETKiVPv-Y1n6y9g4KoQWugWhmjJRbmRE_4yDTY4PDMWn69adgQsFib3n7lndnQoUroT7yTDS_rBFi7rXaZwvT3wBqsAMrI5P1TWYc2X-WCEup0FE_13DIFRLnJlODW6BCIAdeDjIPMmmj61BurTLX-sMypHLgr8tzuYmAumZBXi1-u4yhCK7cQqHfc2s1y7_8HCFMSXW6YLGM9yYeVv3KvQgwCNY30qXkJXPWoD4RGNJejMzUeeRgcIijBTkjLrQ5xW7uA; xq_r_token=7fbde5901fe0c7e736dea69b1b5a606d7f045516; is_overseas=0; Hm_lvt_1db88642e346389874251b5a1eded6e3=1701699797,1702205998,1703252640; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1703252640',
    'origin': 'https://xueqiu.com',
    'pragma': 'no-cache',
    'referer': 'https://xueqiu.com/S/SZ000625',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


def timestamp_format(now):
    # 获得当前时间时间戳
    # now = 1666800000000
    #转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    _time = time.localtime(now / 1000)
    date_time = time.strftime("%Y-%m-%d %H:%M:%S", _time)
    print(date_time)
    return date_time

response = requests.get("https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol=SH601318&begin=1306771200000&period=day&type=before&count=-142&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance", headers=headers)
response_data = response.json()["data"]
c = response_data["column"]
d = response_data["item"]
print(response.json())

# Create your engine.
# To connect with SQLAlchemy you use the create_engine() function to create an engine object from database URI.
engine = create_engine("sqlite:///database.db", pool_recycle=3600, echo=True)
data = pd.DataFrame(d, columns=c)
data['timestamp'] = data['timestamp'].apply(lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(x / 1000)))
# if_exists{‘fail’, ‘replace’, ‘append’}, default ‘fail’
data.to_sql("kline_data", con=engine, if_exists="append")
