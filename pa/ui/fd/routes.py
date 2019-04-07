from flask import render_template
from flask_login import login_required, current_user
from pa.ui import app
from pa.ui.fd.forms import FDForm
from pa.pa.bank import Banks
from pa.pa.member import Members


@login_required
@app.route('/fd', methods=['GET', 'POST'])
def fd():
    banks = Banks()
    members = Members()
    bank_branches = banks.get_all_bank_branch_names(for_user=current_user.username)
    form = FDForm(banks.get_all_bank_branch_names(for_user=current_user.username),
                  members.get_members_of_user(user=current_user.username))

    if form.validate_on_submit():
        return f'Trying to save: {form.data}'

    fds = [{
        'fd_bank': 'This is bank name',
        'bank_branch': 'This is Bank Branch Name',
        'first_name': 'MEMBER1',
        'joint_name': 'MEMBER2',
        'mode': 'Ei/Sur',
        'type': 'Quarterly',
        'interest_account': '12456789012345678' + str(i),
        'fd_number': 'FD12456789012345678/' + str(i),
        'start_date': '01/01/2019',
        'end_date': '01/01/2020',
        'days': '1Y',
        'roi': '8.25',
        'princpal_amount': '100000',
        'maturity_amount': '100000',
    } for i in range(1, 5)]
    return render_template('fd/fd.html', title='Fixed Deposits', form=form,
                           fds=fds, branches=bank_branches)
