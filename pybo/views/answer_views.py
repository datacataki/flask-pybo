from datetime import datetime
from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect

from .. import db
from ..forms import AnswerForm
from ..models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>', methods=('POST',)) # question_detail.html의 form이 post -> 같은 형태 지정
def create(question_id): # question_id 는 URL에서 전달된다
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now())
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    return render_template('question/question_detail.html', question=question, form=form)

    # question = Question.query.get_or_404(question_id)
    # content = request.form['content'] # POST폼 방식으로 전송된 데이터 항목중 name 속성이 content인 값
    # # request 객체를 이용해 브라우저에서 요청한 정보를 확인할 수 있다.
    # answer = Answer(content=content, create_date=datetime.now())
    # question.answer_set.append(answer) # question.answer_set은 질문에 달린 답변들을 의미함
    # db.session.commit()
    # return redirect(url_for('question.detail', question_id=question_id))
    # # 답변을 생성한 후 화면을 이동하도록 redirect 함수를 사용함






