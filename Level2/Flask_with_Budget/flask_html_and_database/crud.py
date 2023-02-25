from app import db, app, Income, Expenses

app.app_context().push()

query_income = Income.query.all()
query_expenses = Expenses.query.all()
income_sum = sum([income.val for income in query_income])
expenses_sum = sum([expenses.val for expenses in query_expenses])

result = income_sum - expenses_sum








