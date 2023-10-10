from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from flask_mail import Mail,Message



# local importation
from pkg.admin import adminobj
from pkg.user import userobj
from pkg.api import apiobj
# exempt the 

csrf = CSRFProtect()
mail = Mail()

def create_app():
    """keep all imports that may cause conflict within function so that anytime we write 
    "from pkg.. import.. none of these statements will be executed"""
    from pkg.models import db
    app = Flask(__name__,instance_relative_config=True)
    # let app know about your blueprint
    app.register_blueprint(adminobj)
    app.register_blueprint(userobj)
    app.register_blueprint(apiobj)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    migrate = Migrate(app,db)
    csrf.init_app(app)
    #exempt the route from csrf protection
    csrf.exempt(apiobj)
    mail.init_app(app)
    return (app)


app = create_app()

# we no longer need to import routes here... they are bbeing loaded in the respective blueprints
from pkg.forms import *