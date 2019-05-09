from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from pa.ui import app
from pa.ui.bank.forms import AddBankBranchForm
from pa.pa.bank import Banks


@app.route('/bank', methods=['GET', 'POST'])
@login_required
def bank():
    banks = Banks()
    form = AddBankBranchForm()

    if form.validate_on_submit():
        banks.add({
            'bank_name': form.bank_name.data,
            'bank_branch': form.bank_branch.data,
            'branch_address': form.branch_address.data,
            'timings': form.timings.data,
        }, for_user=current_user.username)
        return redirect(url_for('bank'))
    
    return render_template('bank/bank.html', title='Bank Branches', form=form,
                           banks=banks.get_all_banks(for_user=current_user.username))


@app.route('/deleteBankBranch/<bank>/<branch>', methods=['GET'])
@login_required
def delete_bank_branch(bank, branch):
    banks = Banks()
    banks.delete_bank_branch(bank_name=bank, bank_branch=branch, username=current_user.username)
    flash(f'Deleted bank( {bank} ), branch( {branch} ) successfully !!')
    return redirect(url_for('bank'))

