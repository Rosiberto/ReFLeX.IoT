from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


bp = Blueprint('age', __name__, url_prefix='/age')


@bp.route('/agent', methods=['GET'])
def agent():
    return render_template('./agents/agent.html')

