from flask import Blueprint

auth = Blueprint('reviews', __name__)

from . import routes
from . import models


