from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_news_list():
    # db에서 목록 전체를 검색합니다. ID는 제외하고 date가 최순으로 정렬
    news_lists = list(db.bs_news_sl.find({}, {'_id': False}).sort('date', -1))
    # 성공하면 success 메시지와 함께 news_lists 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success', 'msg': 'list 연결되었습니다!', 'news_list': news_lists})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
