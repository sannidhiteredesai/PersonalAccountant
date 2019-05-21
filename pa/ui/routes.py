from flask import render_template
from flask_login import login_required, current_user
from pa.ui import app
from pa.ui.auth import routes
from pa.ui.info import routes
from pa.ui.members import routes
from pa.ui.bank import routes
from pa.ui.fd import routes
from pa.ui.report15g import routes
from pa.ui.notifications import routes

@app.route('/home')
@login_required
def home():
    return render_template('index/home.html', username=current_user.username)
