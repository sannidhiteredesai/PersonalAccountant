from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from pa.ui import app
from pa.ui.members.forms import MemberForm
from pa.pa.member import Members

@login_required
@app.route('/allMembers', methods=['GET', 'POST'])
def allMembers():
    members = Members()

    form = MemberForm()
    if form.validate_on_submit():
        members.add(member=form.membername.data, for_user=current_user.username)
        flash('Member {} saved successfully !!'.format(form.membername.data))
        return redirect(url_for('allMembers'))

    members_for_user = members.get_members_of_user(user=current_user.username)
    return render_template('members/allMembers.html', title='Members', form=form, members=members_for_user)
