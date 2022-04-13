import os
from flask import Flask, jsonify


app = Flask(__name__)
DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'fruit.db')


def get_hello():
    """
    /product 로 접속할 수 있도록 함수를 수정하세요.
    화면에 'This is Product' 를 출력합니다.
    """

    answer_1 = ''
    return answer_1


def get_fruits():
    """
    /all 로 접속할 수 있도록 함수를 수정하세요.
    DB_FILEPATH 의 Part2_table 테이블에 작성되어 있는 모든 과일의 name 리스트를 가져옵니다.
    - DB 엔진은 SQLite 입니다.
    - 모든 과일의 이름을 a, b, c ... z 순으로 가져옵니다.
    - jsonify 로 결과를 반환합니다.
    """
    import sqlite3
    pass
    answer_2 = ''

    return jsonify(answer_2)

# 아래 주석을 풀고, 웹 애플리케이션을 실행해 보세요.
# if __name__ == "__main__":
#     app.run(debug=True)