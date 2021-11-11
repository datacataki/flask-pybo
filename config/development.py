from config.default import *
# development.py에서 default.py의 BASE_DIR 환경 변수의 값을 그대로 사용 가능하다

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))
# SQLALCHEMY_DATABASE_URI는 데이터베이스 접속주소, 결과: sqlite:///C:\projects\myproject\pybo.db
# pybo.db라는 db파일을 프로젝트의 루트 디렉터리에 저장
print(SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLALCHEMY의 이벤트를 처리하는 옵션. 파이보에 필요하지않아 비활성화
SECRET_KEY = "dev"




