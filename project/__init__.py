from flask import Flask
from .config import DevConfig
from project.adapters.assembly import Container
import os
import sys

def create_app():

    # app = Flask(__name__,instance_relative_config=True)
    app = Flask(__name__,instance_relative_config=True)
    
    if config=="development":
        app.config.from_object(DevConfig())
    else:
        app.logger.info("FLASK_ENV is NUL!!!");
        
    container = Container(app=app)
    app.container = container 
    container.wire(modules=[sys.modules[__name__]]) # wire container

    # register blueprint 
    from .blueprints.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
   
    return app

