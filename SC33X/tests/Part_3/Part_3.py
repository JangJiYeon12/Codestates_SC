from sprint_challenge import Part_3
import hashlib


def test_part3():
    answer = Part_3.env_of_sc33()
    result = hashlib.md5(answer.encode())

    assert result.hexdigest() == '93388cfe05a6164eca0fe68b34f3cdfa'