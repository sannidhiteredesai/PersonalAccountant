from flask import render_template
from pa.ui import app

@app.route('/info', methods=['GET'])
def info():
    return render_template('info/info.html', title='About Us')
