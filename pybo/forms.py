from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
# from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력항목입니다')]) # 글자수 제한있음, validators는 필수항목 체크
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력항목입니다')]) # 글자수 제한 없음

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력항목입니다')])

class UserCreateForm(FlaskForm): # 계정생성을 위한 폼의 클래스명
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)]) # Length 문자열의 최소, 최대 길이
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = StringField('이메일', validators=[DataRequired()]) # EmailField는 해당 값이 이메일 형식과 일치하는지 검증
    
class UserLoginForm(FlaskForm): # 로그인 폼
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])







