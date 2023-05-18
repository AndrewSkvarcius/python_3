
from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.exceptions import Unauthorized
from models import connect_db, db, User, Feedback
from form import UserForm, Login, Deleted, FeedForm

app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///user_feedback"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"

toolbar = DebugToolbarExtension(app)
connect_db(app)

@app.route("/")
def index():
    return redirect("/register")

@app.route("/register", methods=["GET", "POST"])
def register_home():
    if "username" in session:
        return redirect("/users/{session['username']}")
    
    form = UserForm()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        
        user = User.register(username, password,first_name,last_name,email)

        db.session.commit()
        session['username'] = user.username
        return redirect(f"/users/{user.username}")

    return render_template('users/register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    if "username" in session:
        return redirect(f"/users/{session['username']}")
    form = Login()

    if form.validate_on_submit():
       username = form.username.data
       password = form.password.data

       user = User.authenticate(username, password)
       if user:
            session["username"] = user.username
            return redirect(f'users/{user.username}')
       else:
            form.username.errors = ["Invalid username or password"]
            return render_template("users/login.html", form=form)
    
    return render_template('users/login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/login')

@app.route("/users/<username>")
def user_shown(username):
    
    if "username" not in session or username != session['username']:
        raise Unauthorized()

    user = User.query.get(username)
    form = Deleted()

    return render_template("users/show.html", user=user, form=form)

@app.route("/users/<username>/delete", methods=["POST"])
def user_removal(username):

    if "username" not in session or username != session['username']:
        raise Unauthorized()

    user = User.query.get(username)
    db.session.delete(user)
    db.session.commit()
    session.pop("username")

    return redirect("/login")

@app.route("/users/<username>/feedback/new", methods=["GET", "POST"])
def feedback_new(username):

    if "username" not in session or username != session["username"]:
        raise Unauthorized()

    form = FeedForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        feedback = Feedback(
            title=title, content=content, username=username
        )
        
        db.session.add(feedback)
        db.session.commit()      

        return redirect(f"/users/{feedback.username}")
    else:
        return render_template("feedback/new.html", form=form)

@app.route("/feedback/<int:feedback_id>/update", methods=["GET", "POST"])
def update_feedback(feedback_id):

    feedback = Feedback.query.get(feedback_id)
    if "username" not in session or feedback.username != session["username"]:
        raise Unauthorized()

    form = FeedForm(obj=feedback)
    
    if form.validate_on_submit():
        feedback.title = form.title.data
        feedback.content = form.content.data

        db.session.commit()
        
        return redirect(f"/users/{feedback.username}")
    return render_template("/feedback/edit.html", form=form , feedback=feedback)

@app.route("/feedback/<int:feedback_id>/delete", methods=["POST"])
def delete_feed(feedback_id):
    
    feedback = Feedback.query.get(feedback_id)

    if "username" not in session or feedback.username != session["username"]:
        raise Unauthorized()

    form = Deleted()

    if form.validate_on_submit():
        db.session.delete(feedback)
        db.session.commit()

    return redirect(f"/users/{feedback.username}")


