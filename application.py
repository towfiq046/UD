"""This module creates route and has the functionalities"""

from flask import Flask, render_template, request, redirect, url_for, flash
from env import PASSWORD, DATABASE, USERNAME
from model import db, Parent, Child
from form_valid import ParentForm, ChildForm


app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' +USERNAME+ ':' +PASSWORD+ '@localhost/' +DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def index():
    """Sends data to index.html"""
    # parent = Parent.query.order_by(Parent.id.asc())
    parents = Parent.query.all()
    return render_template("index.html", parents=parents)


@app.route('/create', methods=["GET", "POST"])
def create():
    """Validates and stores parent data"""
    parent_form = ParentForm(request.form)
    if request.method == "POST" and parent_form.validate():
        first_name = parent_form.first_name.data
        last_name = parent_form.last_name.data
        street = parent_form.street.data
        city = parent_form.city.data
        state = parent_form.state.data
        zip_code = parent_form.zip_code.data

        parent = Parent(first_name, last_name, street, city, state, zip_code)

        db.session.add(parent)
        db.session.commit()

        flash("Parent created successfully!")
        return redirect(url_for("index"))
    return render_template("create.html", parent_form=parent_form)


@app.route('/create_child', methods=["GET", "POST"])
def create_child():
    """Sends data to create_child.html"""
    parents = Parent.query.all()
    child_form = ChildForm(request.form)
    if request.method == "POST" and child_form.validate():
        first_name = child_form.first_name.data
        last_name = child_form.last_name.data

        # Check no parent and incorrect value
        if not parents:
            flash("Please create a Parent user first")
            return redirect(url_for("index"))
        try:
            parent_id = int(request.form["parent_id"])
        except ValueError:
            flash("Invalid parent!")
            return render_template("error.html")

        parent = Parent.query.get(parent_id)
        if parent is None:
            flash("No such user")
            return render_template("error.html")

        parent.add_child(first_name, last_name)
        flash("Child created successfully")
        return redirect(url_for("index"))
    return render_template("create_child.html", parents=parents, child_form=child_form)


@app.route('/update/<int:parent_id>', methods=["GET", "POST"])
def update(parent_id):
    """Updates parent table"""
    parent = Parent.query.get(parent_id)
    if parent is None:
        flash("No such user")
        return render_template("error.html")
    parent_form = ParentForm(request.form)
    if request.method == "POST" and parent_form.validate():
        parent.first_name = parent_form.first_name.data
        parent.last_name = parent_form.last_name.data
        parent.street = parent_form.street.data
        parent.city = parent_form.city.data
        parent.state = parent_form.state.data
        parent.zip_code = parent_form.zip_code.data
        db.session.commit()

        flash("Parent created successfully!")
        return redirect(url_for("index"))
    return render_template("update.html", parent=parent, parent_form=parent_form)


@app.route('/update_child/<int:child_id>', methods=["GET", "POST"])
def update_child(child_id):
    """Updates child table"""
    child = Child.query.get(child_id)
    if child is None:
        flash("No such user")
        return render_template("error.html")
    child_form = ChildForm(request.form)
    if request.method == "POST" and child_form.validate():
        child.first_name = child_form.first_name.data
        child.last_name = child_form.last_name.data
        db.session.commit()
        flash("Child updated successfully!")
        return redirect(url_for("index"))

    return render_template("update_child.html", child=child, child_form=child_form)


@app.route('/detail/<int:parent_id>')
def detail(parent_id):
    """Shows detail about single parent"""
    parent = Parent.query.get(parent_id)
    if parent is None:
        flash("No such user")
        return render_template("error.html")

    children = parent.child_relation
    return render_template("detail.html", parent=parent, children=children)


@app.route('/delete/<int:parent_id>/')
def delete(parent_id):
    """Deletes a parent user"""
    parent = Parent.query.get(parent_id)
    if parent is None:
        flash("No such user")
        return render_template("error.html")

    db.session.delete(parent)
    db.session.commit()
    flash("Parent deleted successfully!")
    return redirect(url_for("index"))



@app.route('/delete_child/<int:child_id>/')
def delete_child(child_id):
    """Deletes a child user"""
    child = Child.query.get(child_id)
    if child is None:
        flash("No such user")
        return render_template("error.html")
    db.session.delete(child)
    db.session.commit()
    flash("Child deleted successfully!")
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(e):
    """Error handle 404 page"""
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
