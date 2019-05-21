from datetime import datetime, timedelta
from flask import render_template
from flask_login import login_required, current_user
from pa.ui import app
from pa.pa.notifications import get_maturing_fds


@app.route('/notifications', methods=['GET'])
@login_required
def notifications():
    maturing_fds = []
    todays_date = datetime.today()
    today = todays_date.strftime('%Y%m%d')
    today_plus_45_days = (todays_date + timedelta(days=45)).strftime('%Y%m%d')
    for fd in get_maturing_fds(for_user=current_user.username, till_date=today_plus_45_days):

        title = 'FD Matured' if fd['end_date'] <= today else 'FD Maturing'

        end_date = datetime.strptime(fd['end_date'], '%Y%m%d').strftime('%d/%m/%Y')
        if fd['end_date'] == today:
            difference = 'today'
        elif fd['end_date'] < today:
            difference = str((datetime.strptime(today, '%Y%m%d') -
                              datetime.strptime(fd['end_date'], '%Y%m%d')).days) + ' days ago'
        else:
            difference = 'in ' + str((datetime.strptime(fd['end_date'], '%Y%m%d') -
                                      datetime.strptime(today, '%Y%m%d')).days) + ' days'
        description = [f"FD number: {fd['fd_number']}",
                       f"Bank: {fd['bank_name']} ({fd['bank_branch']})",
                       f"First Name:{fd['first_name']}"]

        maturing_fds.append({
            'title': title,
            'description': description,
            'date': f"Maturity date: {end_date} ({difference})",
        })

    return render_template('notifications/notifications.html', title='Notifications', notifications=maturing_fds)
