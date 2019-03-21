from flask import render_template
from flask_login import login_required, current_user
from pa.ui import app
from pa.ui.auth import routes
from pa.ui.info import routes
from pa.ui.members import routes

@app.route('/')
@login_required
def index():
    return render_template('index/index.html', username=current_user.username)
