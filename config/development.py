# 개발환경에서 사용하는 환경변수 정의
from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'android_login.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'dev'