from flask_restful import Resource
from flask import request
from requests import post


class RefreshController(Resource):

    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"Username or password were not provided"}, 400

        request_data = {
            "plugin": "finalmark",
            "action": "refresh_user",
            "username": username,
            "password": password
        }
        response = post('http://scaler_api', json=request_data)
        return response.json(), response.status_code
