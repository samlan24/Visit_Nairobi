from flask import Blueprint

location = Blueprint('location', __name__)

from . import routes
from . import models


