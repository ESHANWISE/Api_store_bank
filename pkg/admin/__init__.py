from flask import Blueprint


# instantiating an object of blueprint
adminobj = Blueprint("bpadmin",__name__,template_folder="templates",static_folder="static",url_prefix="/admin")

# load routes for blueprint

from pkg.admin import admin_route