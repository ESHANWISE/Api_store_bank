from flask import Blueprint


# instantiating an object of blueprint
apiobj = Blueprint("bpapi",__name__,template_folder="templates",static_folder="static",url_prefix="/api/v1.0")

# load routes for blueprint

from pkg.api import api_route