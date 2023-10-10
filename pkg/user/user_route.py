from flask import session,render_template,redirect,url_for

from pkg.user import userobj #pkg.admin is anoher way to specify the __init__.py within admin folder


@userobj.route("/")
def user_home():
    return render_template("user/index.html")