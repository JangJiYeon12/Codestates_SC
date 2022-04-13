import os
import json
import pytest
import pickle
import sqlite3

from flask import url_for
from sprint_challenge.Part_2 import DB_FILEPATH


def test_product(get_app):
    """
    product에 접속하게 되면, 영어 문자열을 출력합니다.
    1. 접속에 성공
    2. 문자열 확인
    """
    app = get_app
    
    with app.test_client() as test_client:
        response = test_client.get('/product')
        assert response.status_code == 200    
        
def test_anwser_1(get_app):
    app = get_app
    
    with app.test_client() as test_client:
        response = test_client.get('/product')
        assert response.get_data().decode() == 'This is Product' 

def test_all(get_app):
    """
    product에 접속하게 되면, 영어 문자열을 출력합니다.
    1. 접속에 성공
    2. 문자열 확인
    """
    app = get_app
    
    with app.test_client() as test_client:
        response = test_client.get('/all')
        assert response.status_code == 200    

conn = sqlite3.connect(DB_FILEPATH)

def test_post(get_app):
    """
    post 로 apple 이란 문자열을 전달합니다.
    - database : fruit 
    - table : Part2_table
    """
    DATA_FILEPATH = os.path.join(os.path.dirname(__file__), 'part2_data')
    data = []
    with open(DATA_FILEPATH,'rb') as f:
        data = pickle.load(f)

    app = get_app
    with app.test_client() as test_client:
        response = test_client.get('/all')
        assert json.loads(response.get_data()) == data
    


