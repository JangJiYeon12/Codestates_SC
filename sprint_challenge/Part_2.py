import os
from flask import Flask, jsonify


app = Flask(__name__)
DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'fruit.db')

@app.route('/')
def get_hello():
    """
    /product 로 접속할 수 있도록 함수를 수정하세요.
    화면에 'This is Product' 를 출력합니다.
    """

    answer_1 = 'This is Product'
    return answer_1

@app.route('/all')
def get_fruits():
    """
    /all 로 접속할 수 있도록 함수를 수정하세요.
    DB_FILEPATH 의 Part2_table 테이블에 작성되어 있는 모든 과일의 name 리스트를 가져옵니다.
    - DB 엔진은 SQLite 입니다.
    - 모든 과일의 이름을 a, b, c ... z 순으로 가져옵니다.
    - jsonify 로 결과를 반환합니다.
    """
    import sqlite3

    fruit = sqlite3.connect("fruit.db")
    
    cur = fruit.cursor()

    cur.execute("SELECT * FROM Part2_table, ORDER BY name")

    rows = cur.fetchall()

    answer_2 = rows

    return jsonify(answer_2)


    if __name__ == "__main__":
        app.run(debug=True)