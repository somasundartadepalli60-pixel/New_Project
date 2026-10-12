from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from urllib.parse import urlsplit
from ..extensions import db
from ..models import User
from .forms import RegisterForm, LoginForm

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.index"))
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data.strip()
        email = form.email.data.strip().lower()
        if User.query.filter_by(username=username).first():
            flash("That username is already registered.", "error")
        elif User.query.filter_by(email=email).first():
            flash("That email is already registered.", "error")
        else:
            user = User(username=username, email=email)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash("Your account is ready. Start with Unit I.", "success")
            return redirect(url_for("dashboard.index"))
    return render_template("auth/register.html", form=form)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.strip().lower()).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            # Only accept same-site absolute paths; never redirect to an external host.
            next_url = request.args.get("next", "")
            parsed_next = urlsplit(next_url)
            safe_next = (
                bool(next_url)
                and not parsed_next.scheme
                and not parsed_next.netloc
                and parsed_next.path.startswith("/")
                and not parsed_next.path.startswith("//")
                and "\\" not in parsed_next.path
            )
            return redirect(next_url if safe_next else url_for("dashboard.index"))
        flash("Email or password is incorrect.", "error")
    return render_template("auth/login.html", form=form)

@auth_bp.post("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("main.index"))
