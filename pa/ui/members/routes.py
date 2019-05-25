from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from pa.ui import app
from pa.ui.members.forms import MemberForm
from pa.pa.member import Members
from pa.pa.fd import FDs


@app.route('/allMembers', methods=['GET', 'POST'])
@login_required
def allMembers():
    members = Members()

    form = MemberForm()
    if form.validate_on_submit():
        members.add(member=form.membername.data, for_user=current_user.username)
        flash('Member {} saved successfully !!'.format(form.membername.data))
        return redirect(url_for('allMembers'))

    members_for_user = members.get_members_of_user(user=current_user.username)
    return render_template('members/allMembers.html', title='Members', form=form, members=members_for_user)


@app.route('/deleteMember/<member>', methods=['GET'])
@login_required
def delete_member(member):
    fds = FDs()
    if fds.fds_exists_for_member(member=member, for_user=current_user.username):
        flash(f'Member( {member} ) has first name / joint name in some FDs, first delete the FDs to delete this member.')
        return redirect(url_for('allMembers'))

    members = Members()
    members.delete(member=member, for_user=current_user.username)
    flash(f'Deleted member( {member} ) successfully !!')
    return redirect(url_for('allMembers'))
