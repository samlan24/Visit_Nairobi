from flask import Blueprint

business = Blueprint('business', __name__)

from . import routes
from . import models

