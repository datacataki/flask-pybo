from config.default import *
# 서버 환경을 production이라고 칭함

SQLALCHEMY_DATABASE_RUI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'byn\xa47Z\xb6\x9a\x9c\xa4\\\x88p\xc7&\xb1'

# 커맨드창
# python -c "import os; print(os.urandom(16))" # -c command 로 호출되면, command로 주어지는 파이썬 문장을 실행
# 무작위로 16자리 바이트 문자열 출력 b'byn\xa47Z\xb6\x9a\x9c\xa4\\\x88p\xc7&\xb1'
