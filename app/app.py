from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flask import Flask
import os


server = Flask(__name__)
server.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=('./db/db.sqlite'))


from db  import db
db.init_app(server)

from users import auth
server.register_blueprint(auth.bp)

from pages import pages
server.register_blueprint(pages.bp)

from agents import agents
server.register_blueprint(agents.bp)
    
from services import services
server.register_blueprint(services.bp)

from devices import devices
server.register_blueprint(devices.bp)

from setup import setup
server.register_blueprint(setup.bp)

from subscription import subscription
server.register_blueprint(subscription.bp)