import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


# range 써서 Date list 만들고 < 오늘날짜 자동적으로 빠지게?

import datetime

x = datetime.datetime.now()
today = x.strftime("%Y%m%d")

#print(today)

                #from datetime import timedelta, date

                #date1 = '20210101'
                #date2 = '20210117'

                #startDate = datetime.datetime.strptime(date1, "%Y%m%d")
                #endDate = datetime.datetime.strptime(date2, "%Y%m%d")
                #step = datetime.timedelta(days=1)

                #while startDate <= endDate:
                    #print(startDate.date())
                    #startDate += step

                #def daterange(startDate, endDate):
                    #for n in range(int ((endDate - startDate).days)+1):
                        #yield startDate + timedelta(n)

                #for dt in daterange(startDate, endDate):
                    #date = dt.strftime("%Y%m%d")
                    #print(date)

from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2021, 1, 1)
end_dt = date(2021, 1, 17)
#end_dt = x.strftime("%Y, %m, %d")
#print(end_dt)

for dt in daterange(start_dt, end_dt):
    date = dt.strftime("%Y%m%d")
    #print(date)

# DB에 저장할 기사 출처 url 가져오기 / <url에 있는 date 변수 바까가면서?

    url = f'https://sports.news.naver.com/kbaseball/news/list.nhn?date={date}&isphoto=N&type=team&team=SS'
    #url = f'https://sports.news.naver.com/kbaseball/news/list.nhn?date={today}&isphoto=N&type=team&team=SS' < 이전의 날자는 추가 했으니까- 이제 진행할때마다 그 뉴스를 한번씩 중복없게 가져오려면?

    response_data = requests.get(url)
    response = response_data.json()
    newsList = response['list']

    for news in newsList:
        if news['sectionName'] == 'KBO리그':
            #print(news['oid'], news['aid'], news['officeName'], news['title'], news['subContent'], news['thumbnail'])

            urlOid = news['oid']
            urlAid = news['aid']
            newsBaseUrl = f'https://sports.news.naver.com/news.nhn?oid={urlOid}&aid={urlAid}'

            #print(newsBaseUrl)

            bs_news_sl = {
                'date': date,
                'newsUrl': newsBaseUrl,
                'publisher': news['officeName'],
                'title': news['title'],
                'desc': news['subContent'],
                'imgUrl': news['thumbnail']
            }
            #print(bs_news_sl)

#newslist 가져와서 bs_news_sl에 저장

            db.bs_news_sl.insert_one(bs_news_sl)
            #print('완료', news['title'])



#하루에 한번씩 그날 뉴스 가져오기

import schedule
import time

def update():
    print("I'm working now")

    schedule.every().day.at("10:30").do(update)
while True:
    schedule.run_pending()
    time.sleep(1)

import datetime

y = datetime.datetime.now()
todaydate = y.strftime("%Y%m%d")

print(todaydate)

#def updateNews():

updateUrl = f'https://sports.news.naver.com/kbaseball/news/list.nhn?date={todaydate}&isphoto=N&type=team&team=SS'

response_data = requests.get(updateUrl)
response = response_data.json()
updateNewsList = response['list']

for updateNews in updateNewsList:
    if updateNews['sectionName'] == 'KBO리그':
        print(news['oid'], news['aid'], news['officeName'], news['title'], news['subContent'], news['thumbnail'])

        updateUrlOid = news['oid']
        updateUrlAid = news['aid']
        updateNewsBaseUrl = f'https://sports.news.naver.com/news.nhn?oid={updateUrlOid}&aid={updateUrlAid}'

        print(updateNewsBaseUrl)

        bs_news_sl = {
            'date': date,
            'newsUrl': newsBaseUrl,
            'publisher': news['officeName'],
            'title': news['title'],
            'desc': news['subContent'],
            'imgUrl': news['thumbnail']
        }

        #print(bs_news_sl)

#내용 가져온 후, 크롤링하여 DB에 저장기 (<- API 있으니까 필요없지?)

            #def insert_all():
                #db.bs_news_sl.drop()

#실행하기 << 이 두단계는 뭔 차인지 이해가 잘 안간다.
