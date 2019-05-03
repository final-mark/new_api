from flask import Flask
from flask_restful import Api
from api_controllers import RefreshController

application = Flask(__name__)
api = Api(application)

api.add_resource(RefreshController, '/')

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)
