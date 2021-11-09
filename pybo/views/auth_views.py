from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm
from pybo.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth') # 블루프린트 auth 추가 -> /auth/라는 접두어로 시작하는 url이 호출되면 auth_views.py 파일의
# 함수들이 호출
# url이 호출되면 auth_views.py파일의 함수들이 호출

@bp.route('/signup/', methods=('GET', 'POST'))
def signup(): # signup함수는 POST방식요청에는 계정등록을, GET방식요청에는 계정등록을 하는 템플릿을 렌더링한다
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() # 이미 회원가입 해서 유저DB에서 검색해서 있으면 가장 첫번째 정보를 가져옴
        if not user: # 유저 db에 유저 정보가 없으면(회원등록 안되어있으면)
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data), # pw를 암호화함. 암호화한 데이터는 복호화x -> 암호화하여 저장된
                        # 비번과 비교해야 함
                        email=form.email.data)
            db.session.add(user) # 유저 db에 저장, 커밋
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다')
    return render_template('auth/signup.html', form=form)

@bp.route('/login/', methods=('GET', 'POST')) # post 방식 요청:로그인, get: 로그인 템플릿 렌더링
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username= form.username.data).first() # form.username.data : 입력받은 유저네임으로 해당 사용자가 있는지 검사
        if not user: # 사용자가 db에 없으면
            error = "존재하지 않는 사용자입니다"
        elif not check_password_hash(user.password, form.password.data): # 사용자가 존재한다면 db의 비번과 일치하는지 비교
            # db에 저장된 비번은 암호회되어, check_password_hash 함수로 똑같이 암호화해서 비교해야한다
            error = "비밀번호가 올바르지 않습니다"
        if error is None: # 사용자도 존재하고, 비번도올바르다면 세션에 키, 키값을 저장한다
            session.clear() # 세션은 플라스크가 자동 생서, 제공하는 변수이다.
            # request는 요청,응답이라는 과정에서만 사용할수있는 값인반면, 세션은 플라스크 서버를 구동하는 동안 영구히 사용 가능
            session['user_id'] = user.id # 키: user_id, 키값:db에서 조회된 사용자의 id값 저장
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/login.html', form=form)

# 웹프로그램은 웹브라우저 요청 -> 서버응답 순서로 실행, 서버 응답 완료 후 웹브라우저, 서버사이 연결은 끊어짐
# 쿠키: 웹브라우저를 구별하는 값. 웹브라우저가 요청하면 서버는 쿠키를 생성하여 전송하고, 웹브라우저는 서버에서 받은 쿠키를 저장한다
# 이후 서버에 다시 요청할때는 쿠키를 전송하면, 서버는 웹브라우저가 보낸 쿠키를 보고 이전에 보냈던 쿠키와 비교한다
# 세션은 쿠키1개당 생성되는 서버의 메모리 공간이다

@bp.before_app_request # 이 애너테이션이 적용된 함수는 라우트 함수보다 먼저 실행된다. load_logged_in_user 함수는 모든 라우트함수보다 먼저 실행
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None # g는 컨텍슽트 변수이다 
    else:
        g.user = User.query.get(user_id) # session 변수에 user_id 값이 있으면 db에서 이를 조회하여 g.user에 저장해서, 로그인 검사시
        # session을 조사할 필요가 없이, g.user에 값이 있는지만 알아내면 된다
        # g.user에는 User 객체가 저장되어 있어, 유저네임, 이메일 등을 추가로 얻어내는 이점이 있다

@bp.route('/logout/')
def logout():
    session.clear() # 세션의 모든 값을 삭제 -> userid는 삭제될것이며, g.user가 None이 된다
    return redirect(url_for('main.index'))














































