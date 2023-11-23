from flask import Blueprint, current_app, flash, request, redirect, url_for, render_template, send_file, make_response, session
from werkzeug.utils import secure_filename
import os
import logging
from flask_login import login_user, login_required, current_user
import io
from typing import List, Tuple
from datetime import date


views = Blueprint('views', __name__)

@views.route("/")
def index():
    data = current_app.config["DATA"]
    return render_template('index.html', data=data)