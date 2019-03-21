from pa.ui import app
from pa.ui.members.forms import MemberForm
from flask import render_template, flash
from flask_login import login_required


@login_required
@app.route('/allMembers', methods=['GET', 'POST'])
def allMembers():
    form = MemberForm()

    if form.validate_on_submit():
        flash('Trying to save the nre member: ' + form.member_name.data)
        return render_template('members/allMembers.html', title='Members', form=form)

    return render_template('members/allMembers.html', title='Members', form=form)
