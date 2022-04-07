import pytest

def test_openna_nosql(collection):
    """
    주어진 openna 데이터가 몽고디비에 들어가 있는지 확인합니다.
    """
    openna_nosql = collection.find({"meta.name":"openaq-api"})
    assert openna_nosql.__sizeof__() >= 4