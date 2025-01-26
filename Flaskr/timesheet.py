from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Flaskr.auth import login_required
from Flaskr.db import get_db

bp = Blueprint('timesheet', __name__)


@bp.route('/')
def index():
    db = get_db()
    entries = db.execute(
        'SELECT e.id, first_name, last_name, date_of_birth, address, phone, project, hours, employee_id, username'
        ' FROM entry e JOIN user u ON e.employee_id = u.id'
        ' ORDER BY last_name ASC'
    ).fetchall()
    return render_template('timesheet/index.html', entries=entries)