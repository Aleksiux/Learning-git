from flask import Flask, render_template, request
import os
from app import db, Income, Expenses, app
from forms import IncomeForm, ExpensesForm
from crud import result

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def main():
    form1 = IncomeForm()
    form2 = ExpensesForm()
    income_data = Income.query.all()
    expenses_data = Expenses.query.all()

    return render_template('index.html', income_data=income_data, expenses_data=expenses_data, form1=form1, form2=form2,
                           result=result)


@app.route("/income", methods=['GET', 'POST'])
def income():
    form = IncomeForm()
    if form.validate_on_submit():
        val = request.form['val']
        sender = request.form['sender']
        extra_info = request.form['extra_info']
        income = Income(val, sender, extra_info)
        db.session.add(income)
        db.session.commit()
        return render_template('income_form.html', form=form)
    return render_template('income_form.html', form=form)


@app.route("/expenses", methods=['GET', 'POST'])
def expenses():
    form = ExpensesForm()
    if form.validate_on_submit():
        val = request.form['val']
        payment_method = request.form['payment_method']
        product_service = request.form['product_service']
        expenses = Expenses(val, payment_method, product_service)
        db.session.add(expenses)
        db.session.commit()
        return render_template('expenses_form.html', form=form)
    return render_template('expenses_form.html', form=form)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
