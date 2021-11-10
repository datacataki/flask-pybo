# 서버환경에서 사용하는 환경변수 정의
from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'android_login.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'Zb3\x81\xdb\xf1\xd9\xd7-Knb\x8eB\xa5\x18'

"""
(myproject) c:\projects\myproject>python -c "import os; print(os.urandom(16))"
을 터미널에 입력하여 얻은 무작위 수 를 key 값으로 사용
"""