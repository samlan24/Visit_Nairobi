from flask import Blueprint

auth = Blueprint('search', __name__)

from . import routes
from . import models


