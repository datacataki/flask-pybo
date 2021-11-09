from pybo import db

class Question(db.Model): # Question 클래스는 db.Model을 상속받았다. db는 __init__.py에서 생성한 SQLAlchemy객체
    # 테이블명은 question이 된다
    id = db.Column(db.Integer, primary_key=True) # 고유번호. PK는 기본키로, 중복된 값을 가질 수 없다
    subject = db.Column(db.String(200), nullable=False) # 질문
    content = db.Column(db.Text(), nullable=False) # 내용/ Text는 글자수 제한할 수 없는 텍스트
    create_date = db.Column(db.DateTime(), nullable=False) # 생성일

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE')) # db.Foreign key: 다른 모델과 연결
    # question 모델의 id와 연결해서, 어떤 질문에 대한 답인지 알수있다
    # ondelete='CASCADE' 에 의해 질문을 삭제하면 답변도 삭제된다
    question = db.relationship('Question', backref=db.backref('answer_set'))
    # db.relationship(참조할 모델명, 역참조 설정-예:한질문에는 여러개의 답변이 달릴수있는데, 역참조는 이 질문에 달린 답변을 참조하게함)
    # 답변 모델에서 질문 모델을 참조하기 위해 추가함
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # User 모델의 기본키, id는 자동 증가. 따로 폼에서 인풋받지않음
    username = db.Column(db.String(150), unique=True, nullable=False) # unique=True는 같은값을 저장할수없다
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)  # unique=True는 같은값을 저장할수없다
    
    



































