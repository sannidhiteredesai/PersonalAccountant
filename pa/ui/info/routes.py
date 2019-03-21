from pa.ui import app
from flask import render_template

@app.route('/info', methods=['GET'])
def info():
    return render_template('info/info.html', title='About Us')
