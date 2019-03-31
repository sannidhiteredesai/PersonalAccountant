from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from pa.ui import app
from pa.ui.bank.forms import AddBankBranchForm

@login_required
@app.route('/bank', methods=['GET', 'POST'])
def bank():
    form = AddBankBranchForm()
    banks = [
        {
            'name': 'BANK'+str(i),
            'branch': 'BRANCH'+str(i),
            'address': 'ADDRESS line 1, line 2, line 3 '+str(i),
            'timings': 'timings'+str(i),
        }
        for i in range (1,6)
    ]
    if form.validate_on_submit():
        return 'Trying to save : '+str(form.data)
    return render_template('bank/bank.html', title='Bank Branches', form=form, banks=banks)
