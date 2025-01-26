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


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        date_of_birth = request.form['date_of_birth']
        address = request.form['address']
        phone = request.form['phone']
        project = request.form['project']
        hours = request.form['hours']
        error = None

        if not first_name:
            error = 'First name is required.'

        if not last_name:
            error = 'Last name is required.'

        if not date_of_birth:
            error = 'Date of birth is required.'

        if not address:
            error = 'Address is required.'

        if not phone:
            error = 'Phone is required.'

        if not project:
            error = 'Project name is required.'

        if not hours:
            error = 'Hours are required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO entry (first_name, last_name, date_of_birth, address, phone, project, hours, employee_id)'
                ' VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (first_name,last_name,date_of_birth,address, phone, project, hours, g.user['id'])
            )
            db.commit()
            return redirect(url_for('timesheet.index'))

    return render_template('timesheet/create.html')


def get_entry(id, check_author=True):
    entry = get_db().execute(
        'SELECT e.id, first_name, last_name, date_of_birth, address, phone, project, hours, employee_id, username'
        ' FROM entry e JOIN user u ON e.employee_id = u.id'
        ' WHERE e.id = ?',
        (id,)
    ).fetchone()

    if entry is None:
        abort(404, f"Timesheet id {id} doesn't exist.")

    if check_author and entry['employee_id'] != g.user['id']:
        abort(403)

    return entry


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    entry = get_entry(id)

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        date_of_birth = request.form['date_of_birth']
        address = request.form['address']
        phone = request.form['phone']
        project = request.form['project']
        hours = request.form['hours']
        error = None

        if not first_name:
            error = 'First name is required.'

        if not last_name:
            error = 'Last name is required.'

        if not date_of_birth:
            error = 'Date of birth is required.'

        if not address:
            error = 'Address is required.'

        if not phone:
            error = 'Phone is required.'

        if not project:
            error = 'Project name is required.'

        if not hours:
            error = 'Hours are required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE entry SET first_name = ?, last_name = ?, date_of_birth = ?, address = ?, phone = ?, project = ?, hours = ?'
                ' WHERE id = ?',
                (first_name, last_name, date_of_birth, address, phone, project, hours, id)
            )
            db.commit()
            return redirect(url_for('timesheet.index'))

    return render_template('timesheet/update.html', entry=entry)