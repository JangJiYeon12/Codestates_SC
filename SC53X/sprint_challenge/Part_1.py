# SHA(Secure Hash Algorithm) : 고정값을 반환하는 함수로 Hashing 적용
# sha256개념을 이해하는 것이 아닌 결과값을 반환해주는 적절한 메소드를 활용하세요.
# 결과값을 리스트 형태로 반환해주세요.

import hashlib

def sha_hash_function():
  h = hashlib.sha256()
  a = 'Test Name'
  retult = []

  h.update(a.encode('utf-8'))

  result = h.hexdigest().split(' ')

  return result


