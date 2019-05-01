from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


# Define a class and pass it a Resource.
class Add(Resource):
    @staticmethod
    def post():
        request_payload = request.get_json()
        x = request_payload["x"]
        y = request_payload["y"]

        return str(x + y), 200


# Add a resource to the api. You need to give the class name and the URI.
api.add_resource(Add, "/add")

if __name__ == "__main__":
    app.run(debug=True)
