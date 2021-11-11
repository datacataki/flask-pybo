from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from .. import db
from pybo.models import Question
from ..forms import QuestionForm, AnswerForm

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list/')
def _list(): # list는 파이썬 예약어 -> _list
    page = request.args.get('page', type=int, default=1)
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page, per_page=10) # page는 현재 조회할 페이지의 번호, per_page는 페이지마다 보여줄 게시물이 10건
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    db.create_all()
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit(): # 전송된 폼 데이터의 정합성을 점검함
        # 폼을 생성할때 각필드에 지정한 DataRequired() 같은 점검 항목에 이상이 없는지 확인
        # db.create_all()
        question = Question(subject=form.subject.data, content=form.content.data, create_date = datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form=form)



