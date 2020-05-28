import os
import pandas as pd
import requests
import pymysql
import json
import time
from datetime import datetime
import threading

list_url= "http://15.165.21.105:5000/stockcodes?market=kospi"

base_url= "http://15.165.21.105:5000/stockcandles?code=" # 035420&date_from=20000101 "
# conn = pymysql.connect(host="3.34.96.193", user="ttt", password="a105A!)%",
#                        db="TTT", charset="utf8")  # 1. DB 연결
# cur = conn.cursor() # 2. 커서 생성 (트럭, 연결로프)


list_result = requests.get(list_url).json()
# print(list_result.keys())
list_key = list_result.keys()
print(list_key)
for i in  enumerate(list_key):

    current = i[1] # 현재 종목 코드
    code= current[1:]
    name  = list_result[current]['종목명']
    
    print('current   ',current)
    print('code   ',code)
    print('name   ',name)
    stock_url = base_url+code+"&date_from=20000101"
    print(stock_url)
    
    # stock_result = requests.get(list_url).json()
    # print(stock_result)

    # print(list_result[i[1]]['현재가'])



# print(list_key)
# # print(result)

#         "거래량": 1096498,
#         "대비": -500,
#         "대비부호": 53,
#         "상장주식수": 27931470,
#         "시간": 1559,
#         "종목명": "동화약품",
#         "현재가": 10800


# sql = ""
# cur.execute(sql)
# conn.commit() 


