from flask import render_template
from flask_login import login_required
from pa.ui import app


@app.route('/notifications', methods=['GET'])
@login_required
def notifications():
    return render_template('notifications/notifications.html', title='Notifications')
