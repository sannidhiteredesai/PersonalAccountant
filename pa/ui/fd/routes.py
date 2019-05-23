from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from pa.ui import app
from pa.ui.fd.forms import FDForm
from pa.pa.bank import Banks
from pa.pa.member import Members
from pa.pa.fd import FDs
from .format import append_serial_number


@app.route('/fd', methods=['GET', 'POST'])
@login_required
def fd():
    fds = FDs()
    banks = Banks()
    members = Members()
    bank_branches = banks.get_all_bank_branch_names(for_user=current_user.username)
    form = FDForm(banks.get_all_bank_branch_names(for_user=current_user.username),
                  members.get_members_of_user(user=current_user.username))

    if form.validate_on_submit():
        fd = {
            'bank_name': form.bank_name.data,
            'bank_branch': form.bank_branch.data,
            'first_name': form.first_name.data,
            'joint_name': form.joint_name.data,
            'mode': form.mode.data,
            'type': form.type.data,
            'interest_account': form.interest_account.data,
            'fd_number': form.fd_number.data,
            'start_date': form.start_date.data,
            'end_date': form.end_date.data,
            'period': form.period.data,
            'roi': form.roi.data,
            'principal_amount': form.principal_amount.data,
            'maturity_amount': form.maturity_amount.data
        }
        fds.add(fd=fd, for_user=current_user.username)
        flash('New FD added successfully !!')
        return redirect(url_for('fd'))

    all_fds = fds.get_all_fds(current_user.username)
    append_serial_number(all_fds)
    return render_template('fd/fd.html', title='Fixed Deposits', form=form,
                           fds=all_fds, branches=bank_branches,
                           total_fds=len(all_fds))


@app.route('/deleteFD/<fd_number>/<bank_name>/<bank_branch>', methods=['GET'])
@login_required
def delete_fd(fd_number, bank_name, bank_branch):
    fds = FDs()
    fds.delete_fd(fd_number=fd_number, bank_name=bank_name, bank_branch=bank_branch, for_user=current_user.username)
    flash(f'Deleted fd( {fd_number} ) from bank( {bank_name} ), branch( {bank_branch} ) successfully !!')
    return redirect(url_for('fd'))
