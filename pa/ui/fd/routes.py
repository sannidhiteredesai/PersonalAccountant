from flask import render_template
from flask_login import login_required, current_user
from pa.ui import app
from pa.ui.fd.forms import FDForm


@login_required
@app.route('/fd', methods=['GET', 'POST'])
def fd():
    form = FDForm(current_user)
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
    } for i in range(1, 11)]
    return render_template('fd/fd.html', title='Fixed Deposits', form=form,
                           fds=fds)
