from openaq import OpenAQ

api = OpenAQ()

"""
Part 1.1 get_results
"""

def get_results():
    # OpenAQ에서 데이터를 불러옵니다. (아래 문장은 수정 X)
    _, body = api.measurements(city='Los Angeles', parameter='pm25')

    # TODO datetime 와 value 를 튜플 형태로 results 에 추가합니다.
    # Hint: 다음의 링크를 들어가면 body에 들어가는 정보를 확인 할 수 있습니다
    # https://api.openaq.org/v1/measurements?city=Los%20Angeles&parameter=pm25

    date = body.get("date")
    value = body.get("value")

    results = dict(date, value)

    # TODO results 리스트를 리턴합니다.
    return results


"""
Part 1.2 MONGODB SETUP
"""
from pymongo import MongoClient

# 자신의 MongoDB 연결정보를 입력합니다.
# COLLECTION_NAME 은 유지합니다.
HOST = 'cluster0.jpu3q.mongodb.net'
USER = 'Jang-Ji-Yeon'
PASSWORD = 'wldus1021'
DATABASE_NAME = 'myFirstDatabase'
COLLECTION_NAME = 'OpenAQ'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)

database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]

insert = get_results()
collection.insert_one(insert)

# MongoDB 에 OpenAQ 에서 받은 body가 입력되어 있어야합니다.