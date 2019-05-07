from flask import render_template
from flask_login import login_required
from pa.ui import app


@login_required
@app.route('/notifications', methods=['GET'])
def notifications():
    return render_template('notifications/notifications.html', title='Notifications')
