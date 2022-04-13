from sprint_challenge.Part_1 import json_to_pickle
import pickle
import os

TEST_PATH_1 = os.path.join(os.getcwd(), 'tests', __name__, 'sample1.pkl') 
TEST_PATH_2 = os.path.join(os.getcwd(), 'tests', __name__, 'sample2.pkl') 
TEST_PATH_3 = os.path.join(os.getcwd(), 'tests', __name__, 'sample3.pkl') 

def load_pickle(path):
    """
    path 에 있는 pickle 파일을 읽어서, Pickle 의 byte 형태로 반환합니다.
    """
    with open(path, 'rb') as file:
        read_pickle = pickle.load(file)
        byte_pickle = pickle.dumps(read_pickle)
    return byte_pickle

def test_json():
    assert load_pickle(TEST_PATH_1) == json_to_pickle("./sprint_challenge/sample1.json")
    assert load_pickle(TEST_PATH_2) == json_to_pickle("./sprint_challenge/sample2.json")
    assert load_pickle(TEST_PATH_3) == json_to_pickle("./sprint_challenge/sample3.json")
