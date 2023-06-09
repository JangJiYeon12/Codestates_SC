import json
import pickle

def json_to_pickle(path):
    """
    path 경로로 입력받은 json 파일을 pickle 로 반환하는 함수입니다.
    테스트를 진행하면 path 에 아래 세 개의 값이 전달됩니다.
    - ./sprint_challenge/sample1.json
    - ./sprint_challenge/sample2.json
    - ./sprint_challenge/sample3.json
    """

    dict = json.loads(path)

    with open('filename.pickle', 'wb') as handle:
        pickle.dump(dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('filename.pickle', 'rb') as handle:
        answer_pickle = pickle.load(handle)

    return answer_pickle
