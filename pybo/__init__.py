from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # 전역변수로 db,migrate 객체 생성
migrate = Migrate() # db객체를 create_app함수안에서 생성하면 블루프린트같은 다른 모듈에서 불러올 수 없어서 전역변수로 생성

# app = Flask(__name__) # 플라스크 애플리케이션 생성. __name__변수에는 모듈명(pybo)가 담긴다.
# # app객체를 전역으로 사용하면 프로젝트 규모가 커질수록 순환참조 등 문제 발생할 확률이 높아진다
#
# @app.route('/') # urtl이 / 일 때, url에 접속하면 다음줄에 있는 함수를 호출하는 플라스크의 데코레이터
# def hello_pybo():
#     return 'Hello, Pybo!'
def create_app(): # app 객체를 생성해 반환. create_app 함수가 어플리케이션 팩토리이다
    app = Flask(__name__)
    # app.config.from_object(config) # config.py 에서 작성한 항목을 app.config 환경변수로 부르기위해 app.config.from_object(config)코드를 추가함
    app.config.from_envvar('APP_CONFIG_FILE') # 환경변수 APP_CONFIG_FILE에 정의된 파일을 환경파일로 사용하겠다
    # APP_CONFIG_FILE=c:\projects\myproject\config\development.py

    # @app.route('/') # 라우트함수(@app.route 같이 애너테이션으로 매핑되는 함수)
    # def hello_pybo(): # url에서 /에 매핑되는 함수. 새로운 url이 생길 떄 라우트함수를 create_app 함수 안에 계속 추가해야하는 불편함이 있음
    #     return 'Hello, Pybo!'
    
    # ORM
    db.init_app(app) # 전역변수로 db,migrate 객체 생성해서 create_app 함수안에서 init_app 매서드를 이용해서 초기화함
    migrate.init_app(app, db)
    from . import models
    # .은 현재 패키지
    
    # 블루프린트
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp) # create_app함수에 등록되었던 hello_pybo함수 대신 블루프린트를 사용하도록 변경함
    # blueprint를 사용하려면 main_views.py파일에서 생성한 블루프린트 객체인 bp를 등록하면 된다.
    app.register_blueprint(question_views.bp) # question_views.py파일에서 생서한 블루프린트 객체인 bp를 등록
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime  # datetime이라는 이름으로 필터를 등록함

    return app
