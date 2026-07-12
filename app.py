from flask import Flask, render_template, request, redirect, url_for
from expenses import add_expense, view_expenses, remove_expense, get_expense, update_expense, summarized_expenses

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    rows= None 
    rows = view_expenses()
    print(rows[0])
    if request.method == 'POST':
        action = request.form.get("action")
        if action == "add":
            name = request.form['name']
            category = request.form['category']
            date = request.form['date']
            amount = request.form['amount']
            add_expense(name, category, date, amount)
            return redirect(url_for("home"))

        elif ID:=request.form.get("delete"):
            remove_expense(ID)
            return redirect(url_for("home"))
        
        elif ID:=request.form.get("edit"):
            ...
    return render_template("index.html", rows=rows)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_expense(id):

    if request.method == "GET":
        # Load this expense from the database
        expense = get_expense(id)
        print(expense)

        return render_template("edit.html", expense=expense)

    else:
        # User clicked Save
        name = request.form["name"]
        category = request.form["category"]
        date = request.form["date"]
        amount = request.form["amount"]

        update_expense(id, name, category, date, amount)

        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)