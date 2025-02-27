from flask import (
    Blueprint, g, render_template, request
)

from cupcakes.auth import login_required
from cupcakes.db import get_db

bp = Blueprint('cupcakes', __name__)

@bp.route('/')
@login_required
def home():
    # db = get_db()  # not yet needed
    return render_template('cupcakes/home.html', home_page=True)

@bp.route('/other')
@login_required
def other():
    return render_template('cupcakes/other.html')