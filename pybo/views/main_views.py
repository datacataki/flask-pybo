from flask import Blueprint, url_for
from werkzeug.utils import redirect
# 블루프린트를 사용해서 함수를 구조적으로 관리한다. URL과 호출되는 함수의 관계를 확인 가능하다

bp = Blueprint('main', __name__, url_prefix='/') # 블루프린트의 객체 bp 생성 (이름, 모듈명, url프리픽스값)
# main은 나중에 함수명으로 url을 찾아주는 url_for 함수에서 사용됨

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list')) # question(블루프린트이름), _list(블루프린트에 등록된 함수명) 순서로 해석, 함수명을 찾아줌
    # bp의 접두어인 /question/과 /list/가 더해진 /question/list/ url을 반환
    
    # question_list = Question.query.order_by(Question.create_date.desc()) # 질문목록 데이터
    # # 조회된 데이터를 작성일시 기준으로 역순으로 정렬
    # # 역순이 아닌 작성일시 순 조회는 asc()
    # return render_template('question/question_list.html', question_list=question_list)
    # # 템플릿 파일을 화면으로 렌더링 하는 함수
    # # question/question_list.html 파일: 템플릿

# @bp.route('/detail/<int:question_id>/') # localhost:5000/detail/2/ 페이지를 요청하면 detail 함수가 실행되고
# # 매개변수 question_id에는 2가 전달된다
# def detail(question_id):
#     question = Question.query.get(question_id)
#     return render_template('question/question_detail.html', question=question)
#
# @bp.route('detail/<int:question_id>') # 404: 서버가 요청한 페이지 없음
# def detail(question_id):
#     question = Question.query.get_or_404(question_id)
#     # get_or_404함수는 해당 데이터를 찾을 수 없는 경우 404페이지를 출력해줌
#     return render_template('question/question_detail.html', question=question)





