from flask import session,render_template,redirect,url_for

from pkg.admin import adminobj #pkg.admin is anoher way to specify the __init__.py within admin folder


@adminobj.route("/")
def admin_home():
    return render_template("admin/home.html")