from flask import render_template, request
from flask_login import login_required, current_user
from pa.ui import app
from pa.pa.member import Members
from pa.pa.report15g import generate_15g_report, get_financial_year


@app.route('/report15g', methods=['GET', 'POST'])
@login_required
def report_15g():
    members = Members()

    if request.method == 'GET':
        return render_template('report15g/report15g.html', title='15G Report',
                               members=members.get_members_of_user(current_user.username))

    if request.method == 'POST':
        fy_start, fy_end = get_financial_year()
        return render_template('report15g/report15g.html', title='15G Report',
                               members=members.get_members_of_user(current_user.username),
                               report=(generate_15g_report(for_member=(request.form['member']),
                                                           for_user=current_user.username)),
                               member=request.form['member'],
                               fy=f'{fy_start} - {fy_end}')
