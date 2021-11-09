import os # ORM을 적용하려면 설정 파일이 필요함

BASE_DIR = os.path.dirname(__file__)
print('base_dir',BASE_DIR) # 결과: C:/projects/myproject

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))
# SQLALCHEMY_DATABASE_URI는 데이터베이스 접속주소, 결과: sqlite:///C:/projects/myproject\pybo.db
# pybo.db라는 db파일을 프로젝트의 루트 디렉터리에 저장
print('SQLALCHEMY_DATABASE_URI',SQLALCHEMY_DATABASE_URI)

SQLALCHEMY_TRACK_MODIFICTIONS = False # SQLALCHEMY의 이벤트를 처리하는 옵션. 파이보에 필요하지않아 비활성화
SECRET_KEY = "dev"