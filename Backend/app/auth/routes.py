from . import auth


@auth.route('/login', methods=['POST', 'GET'])
def index():
    return 'Hello, World!'