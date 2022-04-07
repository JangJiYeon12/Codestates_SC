import os
import pytest
from pymongo import MongoClient
from src.Part_2 import MONGO_URI, DATABASE_NAME, COLLECTION_NAME

try:
    from src import Part_2 as na
except AttributeError as e:
    print('Skipping src import...')

@pytest.fixture
def get_results_func():
    def return_func():
        return na.get_results

    return return_func

@pytest.fixture(scope='module')
def connection():
    conn = MongoClient(MONGO_URI)
    yield conn
    conn.close()

@pytest.fixture
def database_conn(connection):
    database = connection[f"{DATABASE_NAME}"]
    yield database

@pytest.fixture
def collection(database_conn):
    collection = database_conn[f"{COLLECTION_NAME}"]
    yield collection