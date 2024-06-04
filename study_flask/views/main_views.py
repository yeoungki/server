from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def study_flask():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))