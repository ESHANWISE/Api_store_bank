from flask import Blueprint


# instantiating an object of blueprint
userobj = Blueprint("bpuser",__name__,template_folder="templates",static_folder="static")

# load routes for blueprint

from pkg.user import user_route