from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from threading import Thread
from threading import Event
import json
import time

import warnings
from werkzeug.exceptions import abort



bp = Blueprint('pages', __name__)


@bp.route('/')
def logar():
    return render_template('./auth/login.html')

@bp.route('/#')
def index():
    return render_template('./pages/index.html')
